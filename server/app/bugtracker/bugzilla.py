import json
import requests
from datetime import datetime
from .abstract import AbstractTrack, Issue, Milestone

class Bugzilla(AbstractTrack):

    def __init__(self, url, provider):
        super().__init__(url, provider)
        self.provider = "bugzilla"
        self.__bugzilla_product_name = self.url.split("=")[1]
        self.__bugzilla_url = "/".join(self.url.split("/")[:-1]) 
        self.__bugzila_api_url = self.__bugzilla_url+"/rest/"

    def issues(self, **args):
        r = requests.get("{}bug"
                         .format(self.__bugzila_api_url),
                         params={'product': self.__bugzilla_product_name})

        issues = list()
        for val in r.json():
            i = Issue()
            i.title = val["summary"]
            i.description = ""
            i.url = self.__bugzilla_url + "/show_bug.cgi?id=" + val["id"]
            i.author = val["creator"]
            i.state = "open" if val["is_open"] == "true" else "close"
            i.created = datetime.strptime(val["created_at"],
                                          "%Y-%m-%dT%H:%M:%SZ")
            if i.state == "open":
                i.closed_at = None
            else:
                i.closed_at = datetime.strptime(val["last_change_time"],
                                                "%Y-%m-%dT%H:%M:%SZ")

            issues.append(i.to_dict()) 

        return issues

    def issue(self, iid):
        return self.issues()[iid];

    def commits(self, **args):
        return []

    def commit(self, iid):
        return commits()[iid]

    def users(self, **args):
        return "reguired authentification"

    def user(self, iid):
        return "required authentification"

    def milestones(self, **args):
        r = requests.get("{}bug"
                         .format(self.__bugzila_api_url),
                         params={'product': self.__bugzilla_product_name})

        for val in r.json()["products"]["milestones"]:
            m = Milestone()
            m.title = val["name"]
            m.description = ""
            m.url = ""
            m.state = val["is_active"]
            m.created = None

    def milestone(self, iid):
        return milestones()[iid]

    def code(self, **args):
        pass
