import QtQuick 2.0
import QtCharts 2.0
import Material 0.3


View {
    elevation: 2
    height: 400

    function load(id)
    {
        console.debug("Dans chart")
    }

    ChartView {
        anchors.fill: parent
        theme: ChartView.ChartThemeQt
        antialiasing: true
        backgroundRoundness : 1
        dropShadowEnabled : false
        backgroundColor: "transparent"



        PieSeries {
            id: pieSeries
            PieSlice { label: "eaten"; value: 94.9 }
            PieSlice { label: "not yet eaten"; value: 5.1 }
        }
    }
}
