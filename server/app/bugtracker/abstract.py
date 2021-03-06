from datetime import datetime
import pickle

class AbstractObject:
    def to_dict(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith("_")}

class Issue(AbstractObject):
    def __init__(self):
        self.title = ""
        self.description = ""
        self.url = ""
        self.author = ""
        self.state = ""
        self.created = ""
        self.closed_at = ""

class Milestone(AbstractObject):
    def __init__(self):
        self.title = ""
        self.description = ""
        self.url = ""
        self.created = ""
        self.closed_at = ""
        self.state = ""
        self.open_issue = ""
        self.close_issue = ""

class Commit(AbstractObject):
    def __init__(self):
        self.message = ""
        self.author = ""
        self.date = ""

class AbstractTrack(AbstractObject):
    def __init__(self, url, provider):
        self.name = "project_name"
        self.provider = provider
        self.url = url
        self.description = ""
        self.date_created = ""

    def issues(self, **args):
        pass

    def issue(self, iid):
        pass

    def commits(self, **args):
        pass

    def commit(self, iid):
        pass

    def users(self, **args):
        pass

    def user(self, iid):
        pass

    def milestones(self, **args):
        pass

    def milestone(self, iid):
        pass

    def code(self, **args):
        pass

    def read(filename):
        with open(filename, "rb") as f:
            return pickle.load(f)

    def write(self):
        with open(self.name+".pickle", "wb") as f:
            pickle.dump(self, f)


