from flask import jsonify, request, g, abort, url_for, current_app,send_file
from app.api import api
from app.exceptions import CustomError
from app.utils import toJson
import sys
import uuid
import shutil
import argparse
import tempfile
from io import StringIO,BytesIO


#================================================================================
@api.route('/projects/')
def get_projects():
    return toJson("Sacha est un con")

#================================================================================
@api.route('/projects/', methods=['POST'])
def create_project():
	return toJson({"id": FOLDER, "name": name})

