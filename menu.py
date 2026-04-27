# ================= MENU =================
def menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add student")
        print("2. Display students")
        print("3. Search")
        print("4. Sort")
        print("5. Statistics")
        print("6. Save to file")
        print("7. Load from file")
        print("8. Advanced search")
        print("9. Advanced statistics")
        print("10. Save to JSON")
        print("11. Load from JSON")
        print("0. Exit")
        
        choice = input("Choose: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            sort_students()
        elif choice == "5":
            statistics()
        elif choice == "6":
            save_to_file()
        elif choice == "7":
            load_from_file()
        elif choice == "8":
            advanced_search()
        elif choice == "9":
            advanced_statistics()
        elif choice == "10":
            save_json()
        elif choice == "11":
            load_json()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

# ================= RUN =================
menu()