from flask import Flask, jsonify, request

app = Flask(__name__)

contacts = [
    {
        "contact": 9987644456,
        "name": "Raju",
        "done": False, 
        "id": 1
    },
    {
        "contact": 9876543222,
        "name": "Rahul", 
        "done": False,
        "id": 2
    }
]

@app.route('/')
def hello():
    return "HELLO!"

@app.route("/get-data")
def get_data():
    return jsonify({ "data": contacts })

@app.route("/add-data", methods=['POST'])
def add_data():
    if not request.json:
        return jsonify({
            "status": "Error",
            "message": "Please provide the data required"
        }, 400)
    contact = {
        "contact": request.json['contact'],
        "name": request.json['name'],
        "done": False,
        "id": contacts[-1]['id']+1
    }
    contacts.append(contact)
    return jsonify({
            "status": "Success",
            "message": "Contact added successfully"
        })

if(__name__ == "__main__"):
    app.run(debug=True)