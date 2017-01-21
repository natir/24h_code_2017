import QtQuick 2.4
import Material 0.3
import Material.ListItems 0.1 as ListItem


ApplicationWindow {
    id: app

    title: "24h du Man"
    // Necessary when loading the window from C++
    visible: true
    width : 1200
    height : 600



    theme {
        primaryColor: "blue"
        accentColor: "red"
        tabHighlightColor: "white"
    }


    initialPage: TestPage{}

}
