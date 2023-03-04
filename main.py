from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

archive = {
    1: {"name": "Birthday", "photos": 73, "videos": 15},
    2: {"name": "New Year", "photos": 81, "videos": 24},
    3: {"name": "Anniversary", "photos": 101, "videos": 30},
    4: {"name": "Holidays", "photos": 432, "videos": 17},
}

parser = reqparse.RequestParser()
parser.add_argument("name", type=str)
parser.add_argument("photos", type=int)
parser.add_argument("videos", type=int)


class Main(Resource):
    def get(self, archive_id):
        if archive_id == 0:
            return archive
        else:
            return archive[archive_id]

    def delete(self, archive_id):
        del archive[archive_id]
        return archive

    def post(self, archive_id):
        archive[archive_id] = parser.parse_args()
        return archive

    def put(self, archive_id):
        archive[archive_id] = parser.parse_args()
        return archive


api.add_resource(Main, "/api/archive/<int:archive_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug=True, port=5000, host="127.0.0.1")
