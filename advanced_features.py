# ================= ADVANCED FEATURES =================
def advanced_search():
    keyword = input("Enter keyword: ").lower()
    results = [s for s in students if keyword in s["name"].lower()]
    
    if results:
        for s in results:
            print(s)
    else:
        print("No match found!")

def advanced_statistics():
    grade_count = {"A":0, "B":0, "C":0, "D":0}
    
    for s in students:
        score = s["score"]
        if score >= 8:
            grade_count["A"] += 1
        elif score >= 6.5:
            grade_count["B"] += 1
        elif score >= 5:
            grade_count["C"] += 1
        else:
            grade_count["D"] += 1
    
    print("Grade statistics:")
    for k, v in grade_count.items():
        print(f"{k}: {v}")
