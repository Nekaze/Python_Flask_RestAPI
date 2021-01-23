from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from tinydb import TinyDB, Query
from tinydb.operations import delete
from tinydb.queries import where
import datetime;

db = TinyDB('./db.json')
q = Query()

app = Flask(__name__)
api = Api(app)
numeric_id = 0

class Source(Resource):

    def get(self, source_id):                                           # Finds DB entry by source_id
        result = jsonify(db.search(q.source.source_id == source_id))
        return result

    def post(self, source_id):                                                                                    # Adds source_id entry to the DB
        global numeric_id                                                                                         # The entry has a numeric ID, a source_id, a timestamp
        source = {'source_id': source_id, 'timestamp': datetime.datetime.now().timestamp(), 'log': request.json}  # and the value of the JSON body saved as a log
        q = {'id': numeric_id, 'source': source}
        numeric_id += 1
        db.insert(q)
        return {'status': 'success'}

    def delete(self, source_id):                                        # Deletes DB entry by source_id
        db.update(delete('source'), q.source.source_id == source_id)
        return {'status': 'success'}

class Logs(Resource):

    def get(self, log_value):                                           # Gets DB entry by log value
        result = jsonify(db.search(q.source.log.value == log_value))
        return result

    def delete(self, log_value):                                        # Deletes DB by log_value
        db.update(delete("source"), q.source.log.value == log_value)
        return {'status': 'success'}

class ShowAll(Resource):

    def get(self):                                                      # Gets all the current content of the DB
        result = jsonify(db.all())
        return result

api.add_resource(Source, '/source/<source_id>')
api.add_resource(Logs, '/logs/<log_value>')
api.add_resource(ShowAll, '/') 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)