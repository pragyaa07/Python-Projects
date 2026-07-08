import os
myfile = "tasks.txt"

def load_tasks():
    tasks={}
    if os.path.exists(myfile):
        with open(myfile, "r") as file:
            for line in file:
                id, title, status = line.split(" | ")
                #mylist = line.split("|")
                #tasks[int(mylist[0])]={"title": mylist[1], "status": mylist[2]}
                tasks[int(id)] = {"title": title, "status": status}
    return tasks

def save_tasks(tasks):
    with open(myfile, "w") as file:
        for id, task in tasks.items():
            file.write(f"{id} | {task['title']} | {task['status']}\n")
    print("Tasks saved in file")

def add_task(tasks):
    title = input("Enter task title: ")
    id = max(tasks.keys(), default=0) +1 
    tasks[id] = {"title": title, "status": "incomplete"}
    print(f"Task: {title} added")

def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
    else:
        for id, task in tasks.items():
            print(f"[{id}] {task['title']} : {task['status']}")

def complete_task(tasks):
    id = int(input("Enter task id: "))
    if id in tasks:
        tasks[id]["status"] = "complete"
        print(f"Task: {tasks[id]['title']} completed")
    else:
        print("Id not found")

def delete_tasks(tasks):
    id = int(input("Enter task id: "))
    if id in tasks:
        deleted = tasks.pop(id)
        print(f"Task: {deleted['title']} deleted")
    else:
        print("Id not found")

def main():
    tasks = load_tasks()
    while True:
        print("\n**TASK MANAGER**")
        print("1. View Tasks")
        print("2. Add Tasks")
        print("3. Complete Tasks")
        print("4. Delete Tasks")
        print("5. Save Tasks")
        print("6. Exit")

        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            view_tasks(tasks)

        elif choice == "2":
            add_task(tasks)
        
        elif choice == "3":
            complete_task(tasks)
        
        elif choice == "4":
            delete_tasks(tasks)

        elif choice == "5":
            save_tasks(tasks)

        elif choice == "6":
            save_tasks(tasks)
            print("Exiting")
            break
        
        else:
            print("invalid choice. Try again")
    
if __name__ == "__main__":
    main()



