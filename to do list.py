import json, os
tf = "tasks.json"
def lt():
    return json.load(open(tf, "r"))if os.path.exists(tf) else []
def st(tasks):
    json.dump(tasks, open(tf, "w"), indent=4)
def at(desc):
    tasks = lt()
    tasks.append({'Id': len(tasks) + 1, 'Description': desc, 'Completed': False})
    st(tasks)
    print(f"Task '{desc}' added!")
def ut(task_id, description=None, completed=None):
    tasks = lt()
    for task in tasks:
        if task['Id'] == task_id:
            task['Description'] = description or task['Description']
            task['Completed'] = completed if completed is not None else task['completed']
            st(tasks)
            print(f"Task {task_id} updated!")
            return
    print(f"Task {task_id} not found.")
def dt(task_id):
    tasks = [task for task in lt() if task['Id'] != task_id]
    st(tasks)
    print(f"Task {task_id} deleted!")
def vt():
    tasks = lt()
    if tasks:
        for task in tasks:
            status = "Done" if task['Completed'] else "Pending"
            print(f"ID: {task['Id']} | Task: {task['Description']} | Status: {status}")
    else:
        print("No tasks found!")
print ("\n*******************\n\n TO-DO-LIST \n\n********************")
def main():
    while True:
        choice = input("\nOptions: \n1. Add Task to list  \n2. Update Task in list  \n3. Delete Task from list  \n4. View Tasks from list \n5. Exit \n\nChoose: ")
        if choice == '1': at(input("Task description: "))
        elif choice == '2': ut(int(input("Task ID: ")), input("New description: "), input("Completed (y/n): ").lower() == 'y')
        elif choice == '3': dt(int(input("Task ID to delete: ")))
        elif choice == '4': vt()
        elif choice == '5': break
if __name__ == "__main__":
    main()
