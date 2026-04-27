students = []

# ================= BASIC FEATURES =================
def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter name: ")

    try:
        score = float(input("Enter score (0-10): "))
        if score < 0 or score > 10:
            print("Score must be between 0 and 10!")
            return
    except:
        print("Invalid score!")
        return

    student = {
        "id": student_id,
        "name": name,
        "score": score
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No student found.")
        return
    
    print(f"{'ID':<10}{'Name':<20}{'Score':<10}")
    print("-"*40)
    
    for s in students:
        print(f"{s['id']:<10}{s['name']:<20}{s['score']:<10}")

def search_student():
    keyword = input("Enter ID or Name to search: ").lower()

    found = False
    for s in students:
        if keyword in s["id"].lower() or keyword in s["name"].lower():
            print(s)
            found = True

    if not found:
        print("No student found.")

def sort_students():
    students.sort(key=lambda x: x["score"], reverse=True)
    print("Students sorted by score (descending).")

def statistics():
    if not students:
        print("No student found.")
        return
    
    scores = [s["score"] for s in students]
    avg = sum(scores) / len(scores)
    
    print("Average score:", round(avg, 2))
    print("Max score:", max(scores))
    print("Min score:", min(scores))