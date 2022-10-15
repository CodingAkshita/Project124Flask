from flask import Flask, jsonify, request

#Creating an app using a Flask constructor
app = Flask(__name__)

#Creating a list of contacts
contacts = [
    {
        "Contact" : "9879967842",
        "Name" : "Meena", 
        "done" : False,
        "id" : 1
    },
    {
        "Contact" : "7556479032",
        "Name" : "Clara",
        "done" : False,
        "id" : 2
    }
]

#Creating a route with 'add-data' route with 'POST' method
@app.route("/add-data", methods = ["POST"])
def addTask():
    #displaying an error
    #Here, 400 is the error code
    if not request.json:
        return jsonify({
            "status" : "Error",
            "message" : "Please provide the data"
        }, 400)
        
    contact = {
        'id' : contacts[-1]['id'] + 1,
        'Name' : request.json['Name'],
        'Contact' : request.json.get('Contact', ""),
        'done' : False        
    }
    contacts.append(contact)    
    #When the data is correct and there is no error, we display a success message
    return jsonify({
        "status" : "Success",
        "message" : "Task added successfully"
    })
    
@app.route("/get-data")
def getTask():
    return jsonify({
        "data" : contacts
    })    
    
if (__name__ == "__main__"):
    app.run(debug = True)    