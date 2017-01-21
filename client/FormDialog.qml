import QtQuick 2.4
import Material 0.3
import QtQuick.Layouts 1.1
import Material.ListItems 0.1 as ListItem


Dialog {
    id:root
    width: 600
    height: 400
    title: "Add Your tracker URL"
    property alias name : nameField.text
    property string description : descriptionField.text
    property string provider : providerFied.text
    property string track_url : trackfield.text


    Column {
        anchors.fill: parent
        anchors.margins: 5

            ListItem.Standard {
                action: Icon {
                    anchors.centerIn: parent
                    name: "awesome/tag"
                }

                content: TextField {
                    id: nameField
                    anchors.centerIn: parent
                    width: parent.width

                    placeholderText: "Name ..."

                    text: ""
                }
            }
            //============================================
            ListItem.Standard {
                action: Icon {
                    anchors.centerIn: parent
                    name: "awesome/tag"
                }

                content: TextField {
                    id: descriptionField
                    anchors.centerIn: parent
                    width: parent.width
                    placeholderText: "Description ..."
                    text: ""
                }
            }
            //============================================
            ListItem.Standard {
                action: Icon {
                    anchors.centerIn: parent
                    name: "awesome/tag"
                }

                content: TextField {
                    id: providerFied
                    anchors.centerIn: parent
                    width: parent.width

                    text: ""
                    placeholderText: "Provider ..."
                }
            }
            //============================================
            ListItem.Standard {
                action: Icon {
                    anchors.centerIn: parent
                    name: "awesome/tag"
                }

                content: TextField {
                    id: trackfield
                    anchors.centerIn: parent
                    width: parent.width
                    placeholderText: "Traker url ..."

                    text: ""
                }
            }
        }

    }

