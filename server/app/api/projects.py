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
from ..bugtracker.bugzilla import Bugzilla
from datetime import datetime, timedelta

#================================================================================
@api.route('/projects/', methods=['GET'])
def get_projects():
    ret_list = list()
    for i in range(0, len(_list_project())):
        ret_list.append(_get_project(i).to_dict())
    return toJson(ret_list)

#================================================================================
@api.route('/projects/', methods=['POST'])
def create_project():
    post = request.json
    if post["provider"] == "github":
        project = Github(post["track_url"], "github")
    elif post["provider"] == "bugzilla":
        project = Bugzilla(post["track_url"], "bugzilla")
        
    else:
        raise CustomError("{} provider isn't avaible".format(post["provider"]))

    project.name = post["name"]
    project.description = post["description"]
    project.date_created = datetime.now()
    project.write()
    return toJson(post)


@api.route('/projects/<int:iid>', methods=['GET'])
def get_project(iid):
    return(toJson(_get_project(iid).to_dict()))
    
@api.route('/projects/<int:iid>', methods=['DELETE'])
def delete_project(iid):
    try :
        name = _list_project()[iid - 1]
    except :
        raise CustomError("projects {} didn't exist, sorry".format(iid))

    os.remove(name)

    return toJson("iid : {}".format(iid))

@api.route('/projects/<int:iid>/issues', methods=['GET'])
def get_issues(iid):
    project = _get_project(iid)

    date_filter = request.args.get('filter', None)
    param_filter = request.args.get('param', "created")
    print(date_filter, param_filter)
    return toJson(_filter_by_date(project.issues(), param_filter, date_filter))

@api.route('/projects/<int:iid>/issues/<int:issue_id>', methods=['GET'])
def get_issue(iid, issue_id):
    project = _get_project(iid)

    try:
        return toJson(project.issue(issue_id))
    except :
        raise CustomError("issue {} didn't exist in project {}, sorry"
                          .format(issue_id, iid))

@api.route('/projects/<int:iid>/commits', methods=['GET'])
def get_commits(iid):
    project = _get_project(iid)

    date_filter = request.args.get('filter', None)
    param_filter = request.args.get('param', "date")

    return toJson(_filter_by_date(project.commits(), param_filter, date_filter))

@api.route('/projects/<int:iid>/commits/<int:commit_id>', methods=['GET'])
def get_commit(iid, commit_id):
    project = _get_project(iid)

    try:
        return toJson(project.commit(commit_id))
    except :
        raise CustomError("commit {} didn't exist in project {}, sorry"
                          .format(issue_id, iid))

@api.route('/projects/<int:iid>/milestone', methods=['GET'])
def get_milestones(iid):
    project = _get_project(iid)

    date_filter = request.args.get('filter', None)
    param_filter = request.args.get('param', "created")

    return toJson(_filter_by_date(project.milestones(), param_filter, date_filter))

@api.route('/projects/<int:iid>/milestone/<int:mil_id>', methods=['GET'])
def get_milestone(iid, mil_id):
    project = _get_project(iid)
    
    try:
        return toJson(project.milestone(mil_id))
    except:
        raise CustomError("milestone {} didn't exist in project {}, sorry"
                         .format(mil_id, iid))

@api.route('/projects/<int:iid>/code')
def get_code_freq(iid):
    project = _get_project(iid)
    date_filter = request.args.get('filter', None)
    param_filter = request.args.get('param', "date")

    return toJson(_filter_by_date(project.code(), param_filter, date_filter))

def _get_project(iid):
    try :
        name = _list_project()[iid - 1]
    except :
        raise CustomError("projects {} didn't exist, sorry".format(iid))
 
    obj = AbstractTrack.read(name)
 
    if obj.provider == "github":
        return Github.read(name)
    elif obj.provider == "bugzilla":
        return Bugzilla.read(name)
    else:
        raise CustomError("{} provider isn't avaible".format(obj.provider))

def _list_project():
    ret_list = list()

    for entry in os.scandir("."):
        if entry.is_file() and entry.name.endswith(".pickle"):
            ret_list.append(entry.name)
 
    return ret_list

def _filter_by_date(obj_list, parm_name, date_filter):
    ret_list = list()
    if date_filter == "day":
        for obj in obj_list:
            if obj[parm_name] > (datetime.now() - timedelta(1)):
                ret_list.append(obj)
    elif date_filter == "week":
        for obj in obj_list:
            if obj[parm_name] > (datetime.now() - timedelta(7)):
                ret_list.append(obj)
    elif date_filter == "month":
        for obj in obj_list:
            if obj[parm_name] > (datetime.now() - timedelta(30)):
                ret_list.append(obj)
  
    elif date_filter == "year":
         for obj in obj_list:
            if obj[parm_name] > (datetime.now() - timedelta(365)):
                ret_list.append(obj)
    else:
        return obj_list

    return ret_list
