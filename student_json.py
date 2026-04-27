import json

def save_json(filename="students.json"):
    with open(filename, "w") as f:
        json.dump(students, f, indent=4)
    print("Saved to JSON!")

def load_json(filename="students.json"):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            students.clear()
            students.extend(data)
        print("Loaded from JSON!")
    except:
        print("Error loading file!")
