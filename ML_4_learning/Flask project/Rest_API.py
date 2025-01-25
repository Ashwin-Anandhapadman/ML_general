#Put and delete HTTP verbs
# working with APIs --json

from flask import Flask, jsonify, request
app =Flask(__name__) #intializing the flask

#Intial data in to-do list
#the below data can come from any databased like SQL or MongoDB

items= [
    {id:1, 'name':'item1', "description":"This is item 1"},
    {id:2, 'name':'item2', "description":"This is item 2"}
]

@app.route('/')
def home():
    return 'Welcome to the sample to-do list applicaiton!'

# GET: get all the items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items) #returning the items in json format

#GET: get based on speicific item by ID
@app.route('/items/<int:id>', methods=['GET'])
def get_item(id):
    item= next((item for item in itmes if item['id']==id), None) #None becuz if the item is not found then it should return None
    if item is None:
        return jsonify("error": "Item not found")
    return jsonify(item)

#next(): The next() function retrieves the next item from an iterator (in this case, a generator expression)

#POST: creating a new item
@app.route('/items', methods=['POST'])
def create_item():
   if not request.json or not 'name' in request.json:
       return jsonify({"error": "item not found"})
   new_item={
         'id': items[-1]['id']+1 if items else 1, #if the item is present do this else keep as 1
         'name': request.json['name'],
         'description': request.json.get('description')
   }
   items.append(new_item)
   return jsonify(new_item)


#PUT: update the exisitng item
@app.route('/items/<int:id>', methods=['PUT'])
def update_item(id):
    item= next((item for item in items if item['id']==id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name']= request.json.get('name', item['name'])
    item['description']= request.json.get('description', item['description'])
    return jsonify(item)

#DELETE: delete the item
@app.route('/items/<int:id>', methods=['DELETE'])
def delete_item(id):
    global items
    items= [item for item in items if item['id']!=id]
    return jsonify({"result": True})





if __name__ == '__main__':
    app.run(debug=True)