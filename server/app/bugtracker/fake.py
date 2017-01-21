import json
from .abstract import AbstractTrack

class Fake(AbstractTrack):

    def __init__(self, url, provider):
        self.provider = "fake"
        pass

    def issues(self, **args):
        return json.loads("""
{
    "results": [
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/3991375?v=3",
                "events_url": "https://api.github.com/users/natir/events{/privacy}",
                "followers_url": "https://api.github.com/users/natir/followers",
                "following_url": "https://api.github.com/users/natir/following{/other_user}",
                "gists_url": "https://api.github.com/users/natir/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/natir",
                "id": 3991375,
                "login": "natir",
                "organizations_url": "https://api.github.com/users/natir/orgs",
                "received_events_url": "https://api.github.com/users/natir/received_events",
                "repos_url": "https://api.github.com/users/natir/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/natir/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/natir/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/natir"
            },
            "closed_at": null,
            "created": "Fri, 20 Jan 2017 09:10:53 GMT",
            "description": "In some comment we can see reference to QUazip but we replace this by KArchive.\r\n\r\nI little clean up and check if commented code do important think is require.",
            "state": "open",
            "title": "Clean QUazip reference",
            "url": "https://github.com/labsquare/fastQt/issues/29"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Wed, 18 Jan 2017 21:34:25 GMT",
            "description": "Put StatusBar in mainWindow and display the elapsed time ",
            "state": "open",
            "title": "Add StatusBar with elapsed time",
            "url": "https://github.com/labsquare/fastQt/issues/28"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/3991375?v=3",
                "events_url": "https://api.github.com/users/natir/events{/privacy}",
                "followers_url": "https://api.github.com/users/natir/followers",
                "following_url": "https://api.github.com/users/natir/following{/other_user}",
                "gists_url": "https://api.github.com/users/natir/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/natir",
                "id": 3991375,
                "login": "natir",
                "organizations_url": "https://api.github.com/users/natir/orgs",
                "received_events_url": "https://api.github.com/users/natir/received_events",
                "repos_url": "https://api.github.com/users/natir/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/natir/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/natir/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/natir"
            },
            "closed_at": null,
            "created": "Wed, 18 Jan 2017 19:19:42 GMT",
            "description": "Maybe just add fonction for save and load the future report format.",
            "state": "open",
            "title": "Save / Load result",
            "url": "https://github.com/labsquare/fastQt/issues/27"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Wed, 18 Jan 2017 08:48:52 GMT",
            "description": "@ysard help me to create a snap file from master branch !\r\nhttp://snapcraft.io/create/",
            "state": "open",
            "title": "Create a Snap package",
            "url": "https://github.com/labsquare/fastQt/issues/25"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Mon, 16 Jan 2017 14:19:50 GMT",
            "description": "See : \r\nhttps://github.com/labsquare/fastQt/wiki/Command%20Line%20Argument",
            "state": "open",
            "title": "Do Argument parser",
            "url": "https://github.com/labsquare/fastQt/issues/22"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Mon, 16 Jan 2017 14:19:21 GMT",
            "description": "Set a Thread parmaters for the analysis Runner model, to allow if fixed number of file which can be process simultanously. \r\n",
            "state": "open",
            "title": "Make Thread as arguments",
            "url": "https://github.com/labsquare/fastQt/issues/21"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Fri, 13 Jan 2017 15:26:23 GMT",
            "description": "Here is how I made the main view for the next release 0.2. \r\ntell me what do you thinks ? \r\n\r\n![fastqc_newfeature](https://cloud.githubusercontent.com/assets/1911063/21935206/f542fdf6-d9ac-11e6-8624-fc99f299966e.gif)\r\n",
            "state": "open",
            "title": "Stack list analysis view",
            "url": "https://github.com/labsquare/fastQt/issues/20"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Fri, 13 Jan 2017 10:55:16 GMT",
            "description": "Exporting graph each graph as png . \r\nExporting all analyse as pdf ",
            "state": "open",
            "title": "Export Graph as picture",
            "url": "https://github.com/labsquare/fastQt/issues/19"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Fri, 13 Jan 2017 10:54:41 GMT",
            "description": "we should be able to run FastQt from console . \r\nThat's mean exporting graph into png.",
            "state": "open",
            "title": "Add console argument command",
            "url": "https://github.com/labsquare/fastQt/issues/18"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Fri, 13 Jan 2017 09:55:41 GMT",
            "description": "Using Qt linguistic it would be easy. ",
            "state": "open",
            "title": "Translate App in French",
            "url": "https://github.com/labsquare/fastQt/issues/17"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Thu, 12 Jan 2017 23:42:57 GMT",
            "description": "Try to run fastqt on windows. \r\nYou need to compile KArchive first. Then create a win32/ folder and put the library inside. \r\nSee :\r\nhttps://github.com/labsquare/CuteVCF/tree/master/win32\r\nhttps://github.com/labsquare/CuteVCF/blob/master/CuteVcf.pro#L29",
            "state": "open",
            "title": "Compile master branch on windows",
            "url": "https://github.com/labsquare/fastQt/issues/16"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/1911063?v=3",
                "events_url": "https://api.github.com/users/dridk/events{/privacy}",
                "followers_url": "https://api.github.com/users/dridk/followers",
                "following_url": "https://api.github.com/users/dridk/following{/other_user}",
                "gists_url": "https://api.github.com/users/dridk/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/dridk",
                "id": 1911063,
                "login": "dridk",
                "organizations_url": "https://api.github.com/users/dridk/orgs",
                "received_events_url": "https://api.github.com/users/dridk/received_events",
                "repos_url": "https://api.github.com/users/dridk/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/dridk/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/dridk/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/dridk"
            },
            "closed_at": null,
            "created": "Thu, 12 Jan 2017 23:25:18 GMT",
            "description": "add recent files in File Menu \r\nsee http://doc.qt.io/qt-4.8/qt-mainwindows-recentfiles-example.html",
            "state": "open",
            "title": "Add recent files menu",
            "url": "https://github.com/labsquare/fastQt/issues/14"
        },
        {
            "author": {
                "avatar_url": "https://avatars.githubusercontent.com/u/3991375?v=3",
                "events_url": "https://api.github.com/users/natir/events{/privacy}",
                "followers_url": "https://api.github.com/users/natir/followers",
                "following_url": "https://api.github.com/users/natir/following{/other_user}",
                "gists_url": "https://api.github.com/users/natir/gists{/gist_id}",
                "gravatar_id": "",
                "html_url": "https://github.com/natir",
                "id": 3991375,
                "login": "natir",
                "organizations_url": "https://api.github.com/users/natir/orgs",
                "received_events_url": "https://api.github.com/users/natir/received_events",
                "repos_url": "https://api.github.com/users/natir/repos",
                "site_admin": false,
                "starred_url": "https://api.github.com/users/natir/starred{/owner}{/repo}",
                "subscriptions_url": "https://api.github.com/users/natir/subscriptions",
                "type": "User",
                "url": "https://api.github.com/users/natir"
            },
            "closed_at": null,
            "created": "Wed, 11 Jan 2017 13:17:01 GMT",
            "description": "Hi,\r\n\r\nI work with 3th generation of sequencing, in this generation all read didn't have the same length.\r\n\r\nSo for Per Base Content graph (its an example) the end of graph become chaotic because the information is support just by a little bit of sequence.\r\n\r\n![an example](https://pageshot.net/images/26768c94-4520-403a-b0cf-3b5fe6c6cf37.png)\r\n\r\nMay be we can add coverage information by color gradiant on background of the graph.\r\n\r\nThank for your work.",
            "state": "open",
            "title": "Add coverage information",
            "url": "https://github.com/labsquare/fastQt/issues/3"
        }
    ],
    "success": true,
    "total": 13
}
        """)

    def issue(self, iid):
        return self.issues()[iid]

    def commits(self, **args):
        return json.loads("""
  
{
    "results": [
        {
            "author": "dridk",
            "date": "Wed, 18 Jan 2017 23:53:04 GMT",
            "message": "Merge branch 'master' of https://github.com/labsquare/fastQt"
        },
        {
            "author": "dridk",
            "date": "Wed, 18 Jan 2017 23:52:44 GMT",
            "message": "add gitter hook in travis"
        },
        {
            "author": "sacha schutz",
            "date": "Wed, 18 Jan 2017 22:39:28 GMT",
            "message": "Update README.md\n\nadd gitter logo"
        },
        {
            "author": "sacha schutz",
            "date": "Wed, 18 Jan 2017 19:33:16 GMT",
            "message": "Update README.md\n\nAdd Qt badge"
        },
        {
            "author": "sacha schutz",
            "date": "Wed, 18 Jan 2017 11:41:11 GMT",
            "message": "Update README.md"
        },
        {
            "author": "sacha schutz",
            "date": "Wed, 18 Jan 2017 11:35:47 GMT",
            "message": "Merge pull request #26 from StuntsPT/master\n\nUpdated the docs to match #24."
        },
        {
            "author": "Francisco Pina Martins",
            "date": "Wed, 18 Jan 2017 10:56:58 GMT",
            "message": "Updated the docs to match #24."
        },
        {
            "author": "sacha schutz",
            "date": "Tue, 17 Jan 2017 23:09:24 GMT",
            "message": "Update README.md"
        },
        {
            "author": "dridk",
            "date": "Tue, 17 Jan 2017 20:33:42 GMT",
            "message": "Publish version 0.1"
        },
        {
            "author": "Marijon Pierre",
            "date": "Tue, 17 Jan 2017 07:45:03 GMT",
            "message": "QThread::terminate is dicouraged by the documentation, see https://doc.qt.io/qt-5/qthread.html#managing-threads"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 23:37:52 GMT",
            "message": "Merge branch 'master' of https://github.com/labsquare/fastQt"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 23:37:20 GMT",
            "message": "update FastQt screencast gif"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 20:00:53 GMT",
            "message": "Update README.md"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 19:59:02 GMT",
            "message": "add temporary icons and add desktop file to install on Linux desktop"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 16:42:28 GMT",
            "message": "all analysis add now Q_OBJECT macro for localisation"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 16:24:30 GMT",
            "message": "make all analysis as a QObject"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 16:10:39 GMT",
            "message": "fix font size problem in PerBaseAnalysis"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 16:04:13 GMT",
            "message": "Merge branch 'master' of http://github.com/labsquare/fastQt"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 16:03:58 GMT",
            "message": "add antialiasing"
        },
        {
            "author": "Marijon Pierre",
            "date": "Mon, 16 Jan 2017 16:01:44 GMT",
            "message": "remove compilation warning"
        },
        {
            "author": "dridk",
            "date": "Mon, 16 Jan 2017 14:43:39 GMT",
            "message": "Fix #23 . Concatenate integer to String was the problem"
        },
        {
            "author": "Marijon Pierre",
            "date": "Mon, 16 Jan 2017 13:41:32 GMT",
            "message": "Add fedora install instruction"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 13:01:14 GMT",
            "message": "Update AUTHORS"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 12:57:55 GMT",
            "message": "Update CREDITS"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 11:22:08 GMT",
            "message": "Update README.md"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 10:56:41 GMT",
            "message": "Update README.md\n\nadd travis logo"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 10:51:01 GMT",
            "message": "Update .travis.yml\n\nI thinks it will works now !"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 10:48:01 GMT",
            "message": "Update .travis.yml"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 10:40:15 GMT",
            "message": "Update .travis.yml"
        },
        {
            "author": "sacha schutz",
            "date": "Mon, 16 Jan 2017 10:37:51 GMT",
            "message": "Update .travis.yml"
        }
    ],
    "success": true,
    "total": 30
}
    """)

    def commit(self, idd):
        return self.commit()[iid]

    def users(self, **args):
        return "required authentification"

    def user(self, iid):
        return "required authentification"

    def milestones(self, **args):
        return json.loads("""            
{
    "results": [
        {
            "close_issue": 2,
            "closed_at": null,
            "created": "Wed, 11 Jan 2017 15:37:10 GMT",
            "description": "New feature which doesn't exist in FastQC",
            "open_issue": 12,
            "state": "open",
            "title": "0.2",
            "url": "https://github.com/labsquare/fastQt/milestone/2"
        },
        {
            "close_issue": 0,
            "closed_at": null,
            "created": "Wed, 18 Jan 2017 19:21:08 GMT",
            "description": "Serialization of analysis",
            "open_issue": 1,
            "state": "open",
            "title": "0.3",
            "url": "https://github.com/labsquare/fastQt/milestone/3"
        },
        {
            "close_issue": 10,
            "closed_at": null,
            "created": "Wed, 11 Jan 2017 15:36:46 GMT",
            "description": "Common FastQC analyis are avaible",
            "open_issue": 0,
            "state": "open",
            "title": "0.1",
            "url": "https://github.com/labsquare/fastQt/milestone/1"
        }
    ],
    "success": true,
    "total": 3
}
                          """)

    def milestones(self, idd):
        return milestones()[iid]

    def code(self, **args):
        return json.loads("""
    {
    "results": [
        {
            "add": 0,
            "date": "Sun, 25 Dec 2016 01:00:00 GMT",
            "del": 0
        },
        {
            "add": 0,
            "date": "Sun, 01 Jan 2017 01:00:00 GMT",
            "del": 0
        },
        {
            "add": 3259,
            "date": "Sun, 08 Jan 2017 01:00:00 GMT",
            "del": -292
        },
        {
            "add": 533,
            "date": "Sun, 15 Jan 2017 01:00:00 GMT",
            "del": -162
        }
    ],
    "success": true,
    "total": 4
}
                          """)


