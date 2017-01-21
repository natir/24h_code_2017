import QtQuick 2.0
import QtCharts 2.0
import Material 0.3

import org.labsquare 1.0


View {
    id : root
    height: 150
    elevation: 2
    property int valA : 0
    property int valB:  0

    function load(projet_id)
    {
        console.debug("debut")
    }

    Rectangle {
        anchors.fill: parent

        Row {
            anchors.fill: parent

            Rectangle {
                width: root.width /2
                height: parent.height
                color: "transparent"
                Icon {
                    name:  "awesome/arrow_circle_up"
                    color:  Palette.colors["green"]["500"]
                    size: 40
                    anchors.centerIn: parent
                    anchors.verticalCenterOffset: -20
                }

                Label {
                    text: root.valA+" lines"
                    style: "display1"
                    anchors.centerIn: parent
                     anchors.verticalCenterOffset: 20

                }
            }

            Rectangle {
                width: 2
                height: parent.height
                color: "lightgray"
            }


            Rectangle {
                width: root.width /2
                height: parent.height
                color: "transparent"

                Icon {
                    name:  "awesome/arrow_circle_down"
                    color:  Palette.colors["red"]["500"]
                    size: 40
                    anchors.centerIn: parent
                    anchors.verticalCenterOffset: -20
                }

                Label {
                    text:root.valB +" lines"
                    style: "display1"
                    anchors.centerIn: parent
                     anchors.verticalCenterOffset: 20

                }

            }
        }
    }




}
