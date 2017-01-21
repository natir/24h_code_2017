import QtQuick 2.0
import QtCharts 2.0

ChartView {

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
