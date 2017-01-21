import QtQuick 2.4
import Material 0.3
import QtQuick.Layouts 1.1
import Material.ListItems 0.1 as ListItem
import QtCharts 2.0
import org.labsquare 1.0

Page {
    id: page
    title: "Page with right sidebar"
    backAction: navDrawer.action

    actions : [
        Action {
            text:"Refresh"
            iconName:"awesome/refresh"
            hoverAnimation: true
            onTriggered: {
                prjRequest.get("projects/")

            }
        }
,

        Action {
            text: "Fitler"
            iconName: "awesome/filter"
            onTriggered: actionSheet.open()

        }

    ]
    NavigationDrawer {

        id: navDrawer
        enabled: true

        Column {
            width: parent.width
            ListItem.Subheader {
                text: "Bug Trackers"

            }

            Repeater {
                model: prjModel
                delegate: ListItem.Standard {
                    text: name
                    iconName: "awesome/bug"
                }

            }


        }

        ListModel {
            id: prjModel
        }



        Request {
            id : prjRequest

            onJsonReceived: {
                prjModel.append(json["results"])
            }

        }

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
        Flickable {
            anchors.left: page.left
            clip: true
            anchors.fill: parent
            contentHeight: content.height
            Grid {
                id:content
                anchors.horizontalCenter: parent.horizontalCenter
                spacing: 20
                columns: page.width < 700 ? 1 : 3
                Repeater {
                    model: 10
                    View {
                        width : (page.width / content.columns) - (content.columns*10)
                        height: width
                        elevation : 2

                        StatComponent {
                                anchors.fill: parent
                        }
                    }

                }
            }

        }

}
