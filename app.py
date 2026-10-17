from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Task 1: Define the Problem - Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # Task 2: Design and Develop the Code
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400
    
    # Task 3: Implement the Loop and Process Each Element (determine next ID)
    new_id = 1
    if events:
        new_id = events[-1].id + 1
        
    new_event = Event(new_id, data["title"])
    
    # Task 4: Return and Handle Results
    events.append(new_event)
    return jsonify(new_event.to_dict()), 201

# Task 1: Define the Problem - Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # Task 2: Design and Develop the Code
    data = request.get_json()
    
    # Task 3: Implement the Loop and Process Each Element
    target_event = None
    for event in events:
        if event.id == event_id:
            target_event = event
            break
            
    if not target_event:
        return jsonify({"error": "Event not found"}), 404
        
    if data and "title" in data:
        target_event.title = data["title"]
        
    # Task 4: Return and Handle Results
    return jsonify(target_event.to_dict()), 200

# Task 1: Define the Problem - Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    global events
    
    # Task 2 & 3: Implement the Loop and Process Each Element to find and remove
    target_event = None
    for event in events:
        if event.id == event_id:
            target_event = event
            break
            
    if not target_event:
        return jsonify({"error": "Event not found"}), 404
        
    events = [e for e in events if e.id != event_id]
    
    # Task 4: Return and Handle Results
    return jsonify({"message": "Event deleted successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)