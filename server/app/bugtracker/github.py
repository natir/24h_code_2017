import json
import requests
from datetime import datetime
from .abstract import AbstractTrack, Issue, Milestone, Commit

class Github(AbstractTrack):

    def __init__(self, url, provider):
        super().__init__(url, provider)
        self.provider = "github"
        self.__github_user = self.url.split("/")[3]
        self.__github_repo = self.url.split("/")[4]

    def issues(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/issues?sate=all"
                        .format(self.__github_user, self.__github_repo))
        
        issues = list()
        for val in r.json():
            i = Issue()
            i.title = val["title"]
            i.description = val["body"]
            i.url = val["html_url"]
            i.author = val["user"]
            i.state = val["state"]
            i.created = datetime.strptime(val["created_at"],
                                          "%Y-%m-%dT%H:%M:%SZ")
            if val["closed_at"] == None:
                i.closed_at = None
            else:
                i.closed_at = datetime.strptime(val["closed_at"],
                                                "%Y-%m-%dT%H:%M:%SZ")

            issues.append(i.to_dict())

        return issues

    def issue(self, iid):
        return self.issues()[iid];

    def commits(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/commits"
                         .format(self.__github_user, self.__github_repo))

        commits = list()
        for val in r.json():
            c = Commit()
            c.message = val["commit"]["message"]
            c.author = val["commit"]["author"]["name"]
            c.date = datetime.strptime(val["commit"]["author"]["date"],
                                       "%Y-%m-%dT%H:%M:%SZ")
            commits.append(c.to_dict())

        return commits

    def commit(self, iid):
        return self.commits()[iid]

    def users(self, **args):
        return "required authentification"

    def user(self, iid):
        return "required authentification"

    def milestones(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/milestones"
                        .format(self.__github_user, self.__github_repo))
        
        milestones = list()
        for val in r.json():
            i = Milestone()
            i.title = val["title"]
            i.description = val["description"]
            i.url = val["html_url"]
            i.state = val["state"]
            i.created = datetime.strptime(val["created_at"],
                                          "%Y-%m-%dT%H:%M:%SZ")
            if val["closed_at"] == None:
                i.closed_at = None
            else:
                i.closed_at = datetime.strptime(val["closed_at"],
                                            "%Y-%m-%dT%H:%M:%SZ")
            i.open_issue = val["open_issues"]
            i.close_issue = val["closed_issues"]
            milestones.append(i.to_dict())

        return milestones

    def milestone(self, iid):
        return self.milestones()[iid]

    def code(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/stats/code_frequency".
                         format(self.__github_user, self.__github_repo))
        reponse = list()

        for val in r.json():
            r = dict()
            r["date"] = datetime.fromtimestamp(val[0])
            r["add"] = val[1]
            r["del"] = val[2]
            reponse.append(r)

        return reponse

