from flask import Flask, request, jsonify

app = Flask(__name__)

# Example projects and their data
projects = {
    "project1": {
        "name": "My First Project",
        "blocks": [
            {"type": "start", "x": 100, "y": 100},
            {"type": "move", "direction": "forward", "distance": 50},
            {"type": "turn", "direction": "right", "angle": 90},
            {"type": "move", "direction": "forward", "distance": 50},
            {"type": "end", "x": 150, "y": 150}
        ]
    },
    "project2": {
        "name": "My Second Project",
        "blocks": [
            {"type": "start", "x": 200, "y": 200},
            {"type": "move", "direction": "forward", "distance": 100},
            {"type": "turn", "direction": "left", "angle": 90},
            {"type": "move", "direction": "forward", "distance": 100},
            {"type": "end", "x": 250, "y": 250}
        ]
    }
}

# Route to get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

# Route to get a specific project by its name
@app.route('/project/<string:name>', methods=['GET'])
def get_project(name):
    if name in projects:
        return jsonify(projects[name])
    else:
        return jsonify({"error": "Project not found"}), 404

# Route to save a project
@app.route('/project', methods=['POST'])
def save_project():
    project_data = request.json
    if 'name' in project_data and 'blocks' in project_data:
        projects[project_data['name']] = project_data
        return jsonify({"message": "Project saved successfully"})
    else:
        return jsonify({"error": "Invalid project data"}), 400

if __name__ == '__main__':
    app.run(debug=True)
