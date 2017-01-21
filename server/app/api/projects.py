from flask import jsonify, request, g, abort, url_for, current_app,send_file
from app.api import api
from app.exceptions import CustomError
from app.utils import toJson
import os
import sys
import uuid
import shutil
import argparse
import tempfile
from io import StringIO,BytesIO

from ..bugtracker.abstract import AbstractTrack
from ..bugtracker.github import Github
from datetime import datetime

#================================================================================
@api.route('/projects/', methods=['GET'])
def get_projects():
    return toJson(_list_project())

#================================================================================
@api.route('/projects/', methods=['POST'])
def create_project():
    post = request.json
    if post["provider"] == "github":
        project = Github(post["track_url"], "github")
        project.url = post["track_url"]
        project.name = post["name"]
        project.description = post["description"]
        project.date_created = datetime.now()
        project.write()
        return toJson(post)
    else:
        raise CustomError("{} provider isn't avaible".format(post["provider"]))

    return True

@api.route('/projects/<int:iid>', methods=['GET'])
def get_project(iid):
    try :
        name = _list_project()[iid - 1]
    except :
        raise CustomError("projects {} didn't exist, sorry".format(iid))
 
    obj = AbstractTrack.read(name)
                          
    if obj.provider == "github":
        return toJson(Github.read(name).to_dict())
    else:
        raise CustomError("{} provider isn't avaible".format(obj.provider))


def _list_project():
    ret_list = list()

    for entry in os.scandir("."):
        if entry.is_file() and entry.name.endswith(".pickle"):
            ret_list.append(entry.name)
 
    return ret_list