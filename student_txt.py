import os

def save_to_file(filename="students.txt"):
    with open(filename, "w") as f:
        for s in students:
            f.write(f"{s['id']},{s['name']},{s['score']}\n")
    print("Data saved successfully!")

def load_from_file(filename="students.txt"):
    if not os.path.exists(filename):
        print("File not found!")
        return
    with open(filename, "r") as f:
        students.clear()
        for line in f:
            id, name, score = line.strip().split(",")
            students.append({
                "id": id,
                "name": name,
                "score": float(score)
            })
    print("Data loaded successfully!")
