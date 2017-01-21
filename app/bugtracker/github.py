import json
import requests

from .abstract import AbstractTrack, Issue



class Github(Abstract):

    def __init__(self, url, provider):
        super().__init__()
        self.provider = "github"
        self.__github_user = self.url.split("/")[4]
        self.__github_repo = self.url.split("/")[5]

    def issues(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/issues"
                        .format(self.github_user, self.github_repo))
        
        issues = list()
        for val in r.json():
            i = Issue()
            i.title = val["title"]
            i.description = val["description"]
            i.url = val["http_url"]
            i.author = val["user"]
            i.state = val["state"]
            i.created = val["created_at"]
            i.update_at = ["update_at"]
            issues.append(i)

        return issues

    def issues(self, iid):
        return self.issues[iid];

    def users(self, **args):
        return "required authentification"

    def users(self. **iid):
        return "required authentification"

    def milestone(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/milestones"
                        .format(self.github_user, self.github_repo))
        
        milestones = list()
        for val in r.json():
            i = Milestone()
            i.title = val["title"]
            i.description = val["description"]
            i.url = val["http_url"]
            i.state = val["state"]
            i.created = val["created_at"]
            i.close_at = ["update_at"]
            i.open_issue = ["open_issue"]
            i.close_issue = ["close_issue"]
            milestones.append(i)

        return milestones

    def milestone(self, iid):
        return self.milestone()[iid]

    def code(self, **args):
        r = requests.get("https://api.github.com/repos/{}/{}/stats/code_frequency".
                         format(self.github_user, self.github_repo))
        reponse = dict()

        for val in r.json():
            reponse["date"] = datetime(val[0])
            reponse["add"] = datetime(val[1])
            reponse["del"] = datetime(val[2])
