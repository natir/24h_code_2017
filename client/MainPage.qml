import QtQuick 2.4
import Material 0.3
import QtQuick.Layouts 1.1
import Material.ListItems 0.1 as ListItem
import QtCharts 2.0
import org.labsquare 1.0

TabbedPage {
    id: page
    title: "Page with right sidebar"
    property int currentProject : 0
    backAction: navDrawer.action

    // load init
    Component.onCompleted: {
        navDrawer.load()
    }

    function load(project_id)
    {
        console.debug("load projet ID "+project_id)

        tabs.getTab(0).item.load(project_id)
        tabs.getTab(1).item.load(project_id)


    }

    actions : [
        Action {
            text:"Refresh"
            iconName:"awesome/refresh"
            hoverAnimation: true
            onTriggered: load(currentProject)
        },
        Action {
            text: "Fitler"
            iconName: "awesome/filter"
            onTriggered: actionSheet.open()
        }
    ]


    //=============================   Nav
    NavigationDrawer {

        id: navDrawer
        enabled: true

        function load() {
            prjRequest.get("projects/")
        }

        Column {
            width: parent.width
            ListItem.Subheader {  text: "Bug Trackers"  }
            Repeater {
                model: prjModel
                delegate: ListItem.Standard {
                    text: name
                    iconName: "awesome/bug"
                    onClicked: {
                        currentProject = index
                        page.title = title +" in "+provider
                        load(index)
                        navDrawer.close()
                    }
                }
            }
        }

        ListModel { id: prjModel  }
        Request {
            id : prjRequest
            onJsonReceived: {
                prjModel.clear()
                prjModel.append(json["results"])
            }
        }
    }

    //=============================== TAB 1

    Tab {
        id: myTab
        title: "Summmay"
        active : true


        Flickable {
            id: base
            clip: true
            anchors.fill: parent
            anchors.margins: 10
            contentHeight: content.height
            property int compW : 400

            function load(project_id)
            {
                numView.load(project_id)
            }


            Grid {
                id:content
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 20
                columns: page.width < 700 ? 1 : 3
                verticalItemAlignment: Grid.AlignVCenter

                NumComponent {
                    id: numView
                    width: 400
                    valA: page.addValue
                    valB: page.remValue

                }

                StatComponent {
                    id :test
                    width: 400

                }

                StatComponent {
                    width: 400
                }

            }

        }
    }

    //=============================== TAB 1

    Tab {
        title: "Issues"
        active : true



        Item {

            function load(project_id)
            {
                issueReq.get("project/"+project_id+"/issues")
            }



            ProgressCircle {

                anchors.centerIn: parent
                color:Palette.colors["blue"]["500"]
                width: dp(64)
                height: dp(64)
                dashThickness: dp(8)

            }

            ListView {
                anchors.fill: parent
                model : issueModel
                delegate: ListItem.Standard {
                    text:title
                    iconName: "awesome/bug"
                    iconColor:  Palette.colors["green"]["500"]
                    valueText: Date(created)
                }
            }

            ListModel {id:issueModel}
            Request {
                id:issueReq
                onJsonReceived: {
                    issueModel.clear();
                    issueModel.append(json["results"])
                }

            }
        }

    }

    //================================ Sheets
    ActionButton {

        anchors.bottom:  parent.bottom
        anchors.right: parent.right
        anchors.rightMargin: 10
        anchors.bottomMargin: 10

        action: Action {
            id: addContent
            text: "New Track"
            shortcut: "Ctrl+C"
            onTriggered: snackbar.open("We do actions too!")
        }
        iconName: "awesome/plus"
        onClicked: newTrackers.open()
    }

    BottomActionSheet {
        id: actionSheet
        title: "Filter"
        actions: [
            Action {
                iconName: "social/share"
                name: "Last Day"
            },

            Action {
                iconName: "file/file_download"
                name: "Last month"
            },

            Action {
                iconName: "file/file_download"
                name: "Last Years"
            }
        ]
    }

    FormDialog {
        id: newTrackers
        onAccepted: {
            postRequest.post("projects/", {
                                 "name": newTrackers.name,
                                 "description":newTrackers.description,
                                 "provider":newTrackers.provider,
                                 "track_url": newTrackers.track_url})

        }

        Request {
            id: postRequest
            onJsonReceived : {
                console.debug(json["success"]);
            }


        }
    }

    //    ListModel {
    //        id: issueModel
    //    }

    //    Request {
    //        id: issueRequest
    //        onJsonReceived: {
    //            console.debug(json["success"])
    //            issueModel.clear()
    //            issueModel.append(json["results"])
    //        }
    //    }


    //    Request {
    //        id: indicA
    //        onJsonReceived: {
    //            console.debug("received code")
    //            page.addValue = 0
    //            page.remValue = 0
    //            for (var i in json["results"])
    //            {
    //                console.debug(i)
    //                page.addValue  += json["results"][i]["add"]
    //                page.remValue  += json["results"][i]["rem"]



    //            }

    //            console.debug(page.addValue)
    //        }
    //    }




    //    Tab {
    //        title: "Summmay"


    //        Flickable {
    //            id: base
    //            clip: true
    //            anchors.fill: parent
    //            anchors.margins: 10
    //            contentHeight: content.height
    //            property int compW : 400

    //            Grid {
    //                id:content
    //                anchors.horizontalCenter: parent.horizontalCenter
    //                spacing: 20
    //                columns: page.width < 700 ? 1 : 3
    //                verticalItemAlignment: Grid.AlignVCenter

    //                NumComponent {
    //                    id: numView
    //                    width: 400
    //                    valA: page.addValue
    //                    valB: page.remValue

    //                }

    //                StatComponent {
    //                    width: 400

    //                }

    //                StatComponent {
    //                    width: 400
    //                }

    //            }

    //        }
    //    }


    //    Tab {
    //        title: "Issues"
    //        Item {
    //            ProgressCircle {

    //                anchors.centerIn: parent
    //                visible: issueRequest.isLoading
    //                color:Palette.colors["blue"]["500"]
    //                width: dp(64)
    //                height: dp(64)
    //                dashThickness: dp(8)

    //            }

    //            ListView {
    //                anchors.fill: parent
    //                model : issueModel
    //                visible: !issueRequest.isLoading
    //                delegate: ListItem.Standard {
    //                    text:title
    //                    iconName: "awesome/bug"
    //                    iconColor:  Palette.colors["green"]["500"]
    //                    valueText: Date(created)



    //                }
    //            }
    //        }

    //    }


    // Add new trckers

}
