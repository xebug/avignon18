from flask import Flask, request
import uuid

students = dict()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/square/<int:num>')
def square(num):
   return str(num**2)


@app.route('/student/<string:name>', methods=['POST', 'GET'])
def student(name):
    print request
    def getStudent(name):
        return str(students[name])

    def addStudent(name, number):
        students[name] = number
        return getStudent(name)

    if request.method == 'POST':
        if name not in students.keys():
            return addStudent(name, uuid.uuid4())
        return getStudent(name)
    
    if request.method == 'GET':
        return getStudent(name)

if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", debug=True)
