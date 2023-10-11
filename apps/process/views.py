from config.settings import app
from flask import Blueprint, jsonify, make_response, request
from apps.process.models import Process
from apps.process.schema import ProcessSchema
from apps.process.services import ProcessServices


process_app = Blueprint("process", __name__)

@process_app.route('/process/status/<int:status>/', methods=["GET"])
def showProcess(status: int):
    """ Example for get process by status numbers
    This is using docstrings for specifications.
    ---
    parameters:
      - name: status
        in: path
        type: integer
        required: true
        default: "60"
    definitions:
      Status:
        type: integer
    responses:
      200:
        description: A list by status
        examples:
          status: "60"
    """
    try:
        process = ProcessServices().get_process(status)
        if process:
            process_schema = ProcessSchema()
            process_data = process_schema.dump(process, many=True)
            return make_response(jsonify({'process_status': process_data}), 200)
        else:
            return make_response(jsonify({"message": "Status not exist"}), 200)
    except:
        return make_response(jsonify({"message": "Status not found"}), 500)
    

@process_app.route('/process/add/', methods=["POST"])
def addProcess():
    """ Example for add process
    This is using docstrings for specifications.
    ---
    parameters:
      - name: process
        in: body
        type: object
        required: true
        example:
          idBulk: 1
          retries: 1
          status: 60
          name: 'name'
    definitions:
      Process:
        type: object
        properties:
          id:
            type: integer
          idBulk:
            type: integer
          retries:
            type: integer
          status:
            type: integer
          name:
            type: string
    responses:
      201:
        description: Create a new process
    """
    try:
        process_schema = ProcessSchema()
        process_data = process_schema.load(request.json)
        ProcessServices().add_process(process_data)
        return make_response(jsonify({"result": "success, save new process"}), 200)
    except:
        return make_response(jsonify({"message": "Fail, process not save correct"}), 500)