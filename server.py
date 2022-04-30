##flask参考文档：https://flask.palletsprojects.com/en/2.1.x/quickstart/
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/setAppInfo", methods=['POST','GET'])
def setAppInfo():
    if request.method == 'POST':
        Jury=dict(name='Jury',
                    fans=10000)
        return dict(User=Jury,
                    age=30)
    else:
        print(request.args.get('name', '') )        ##from qury ?name=Jury
        print(request.form['userName'])             ##from body
        print(request.headers['User-Agent'])        ##from header
        return 'setAppInfo get'


if __name__ == "__main__":
    app.run()
