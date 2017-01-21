#ifndef REQUEST_H
#define REQUEST_H
#include <QObject>
#include <QtNetwork>
#include <QJsonObject>
#include <QJsonDocument>
#include "WTools.h"

class Request : public QObject
{
    Q_OBJECT
    Q_PROPERTY(bool isLoading READ isLoading NOTIFY isLoadingChanged)
public:
    explicit Request(QObject *parent = 0);

     QNetworkReply * get(const QNetworkRequest& request);
     QNetworkReply * post(const QNetworkRequest& request,const QByteArray& data = QByteArray() );
     QNetworkReply * put(const QNetworkRequest& request, const QByteArray& data = QByteArray());
     QNetworkReply * deleteResource(const QNetworkRequest& request);

    static QNetworkRequest makeRequest(const QString& resource) ;


    Q_INVOKABLE void get(const QString& uri);
    Q_INVOKABLE void post(const QString& uri, const QJsonObject& data);

    const QJsonDocument& json() const;

    bool isLoading();

    void setLoading(bool enable);

signals :
    void jsonReceived(const QJsonObject& json);
    void isLoadingChanged();


protected Q_SLOTS:
    void received();

private:
    bool mLoading = false;
    QJsonDocument mJson;


};

#endif // REQUEST_H
