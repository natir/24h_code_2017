QT += qml quick charts

CONFIG += c++11

SOURCES += main.cpp \
    Request.cpp \
    WTools.cpp

RESOURCES += qml.qrc


#DEFINES += QPM_INIT\\(E\\)=\"E.addImportPath(QStringLiteral(\\\"qrc:/\\\"));\"
#OPTIONS += roboto

#include(material/material.pri)

# Additional import path used to resolve QML modules in Qt Creator's code model
QML_IMPORT_PATH =

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

HEADERS += \
    Request.h \
    WTools.h



