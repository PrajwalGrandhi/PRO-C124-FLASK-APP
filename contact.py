from flask import Flask,jsonify,request

app=Flask(__name__)

contacts=[
    {
"id":1,
"Name":"Father",
"Contact":123456789,
    },
    {
"id":2,
"Name":"Mother",
"Contact":987654321,
    }
]

@app.route('/contacts')
def getContacts():
    return jsonify({
        "data":contacts
    })

@app.route('/addContacts',methods=['POST'])
def addContacts():
    if not request.json:
        return jsonify({
            "status":"ERROR",
            "message":"Please provide the data"
        },400)
    task={
        "id":contacts[-1]["id"]+1,
        "Name":request.json["Name"],
        "Contact":request.json.get("Contact",""),
    }
    contacts.append(task)
    return jsonify({
        "status":"success",
        "message":"The Task has been has been added succesfully",
        })

if(__name__=="__main__"):
    app.run(debug=True)