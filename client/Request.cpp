#include "Request.h"
#include <QDebug>
Request::Request(QObject *parent) : QObject(parent)
{

}

QNetworkReply * Request::get(const QNetworkRequest &request)
{
    setLoading(true);
    QNetworkReply * reply = WTools::i()->netManager()->get(request);
    connect(reply, SIGNAL(finished()), this,SLOT(received()));
}

QNetworkReply * Request::put(const QNetworkRequest &request, const QByteArray &data)
{
    setLoading(true);    QNetworkReply * reply = WTools::i()->netManager()->put(request, data);
    connect(reply, SIGNAL(finished()), this,SLOT(received()));

}

QNetworkReply * Request::post(const QNetworkRequest &request, const QByteArray &data)
{
    setLoading(true);
    QNetworkReply * reply = WTools::i()->netManager()->post(request,data);
    connect(reply, SIGNAL(finished()), this,SLOT(received()));

}

QNetworkReply * Request::deleteResource(const QNetworkRequest &request)
{
    setLoading(true);
    QNetworkReply * reply = WTools::i()->netManager()->deleteResource(request);
    connect(reply, SIGNAL(finished()), this,SLOT(received()));
}

QNetworkRequest Request::makeRequest(const QString &resource)
{
    QUrl url;
    url.setHost(WTools::i()->host());
    url.setPath(WTools::i()->prefix() + resource);
    url.setScheme("http");
    url.setPort(WTools::i()->port());

    qDebug()<<url;

    QNetworkRequest request(url);


    request.setRawHeader("User-Agent", "My app name v0.1");
    request.setRawHeader("X-Custom-User-Agent", "My app name v0.1");
    request.setRawHeader("Content-Type", "application/json");


    return request;
}

void Request::get(const QString &uri)
{
    qDebug()<<uri;

    QNetworkRequest request = makeRequest(uri);

    get(request);
}

void Request::post(const QString &uri, const QJsonObject &data)
{
    QNetworkRequest request = makeRequest(uri);
    QJsonDocument doc(data);

    qDebug()<<request.url()<<" with " << doc.toJson();

    post(request, doc.toJson());

}

const QJsonDocument &Request::json() const
{
    return mJson;
}

bool Request::isLoading()
{
    return mLoading;
}

void Request::setLoading(bool enable)
{
    mLoading = enable;
    emit isLoadingChanged();
}

void Request::received()
{
    QNetworkReply * reply = qobject_cast<QNetworkReply*>(sender());

    if (reply)
    {
        mJson = QJsonDocument::fromJson(reply->readAll());
        emit jsonReceived(mJson.object());
    }

    setLoading(false);


}
