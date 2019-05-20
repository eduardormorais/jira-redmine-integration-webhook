from flask import Flask, request
from flask_restful import Resource, Api
from manipule_jira import cerate_dic_fields, create_new_issue


app = Flask(__name__)
api = Api(app)

class RedMineWebHook(Resource):
    def post(self):
        webhook = request.get_json()
        print(webhook)
        dic_fields = cerate_dic_fields(webhook)
        result = create_new_issue(dic_fields)
        print(result)


api.add_resource(RedMineWebHook, "/api/v1/webhook")
if __name__ == "__main__":
    app.run(host= "0.0.0.0")



