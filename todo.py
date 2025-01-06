import argparse
import os
import json

# -a or --add for adding a task
# -l or --list for listing all tasks
# -d or --delete for deleting a task
# -u or --update for updating a task

def create_parser():
    parser = argparse.ArgumentParser(description='Task Tracker')
    parser.add_argument('-a', "--add", metavar="", help="Add a task")
    parser.add_argument('-l', "--list", action="store_true", help="List all tasks")
    parser.add_argument('-d', "--delete",metavar="", help="Delete a task")
    parser.add_argument('-u', "--update",metavar="", help="Update a task")
    return parser

def add_task(task):
    tasks = []
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    tasks.append({'task': task, 'done': False})
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)
    print('Task added successfully')

def list_tasks():
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            for index, task in enumerate(tasks):
                print(f'{index + 1}. {task["task"]} - {"Done" if task["done"] else "Not Done"}')
    else:
        print('No tasks found')

def delete_task(index):
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            if 0 < index <=len(tasks):
                print(f'Deleted task: {tasks[index-1]["task"]}')
                del tasks[index-1]
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file)
                print("Task deleted successfully")
    else:
        print("No task found to delete")

def update_task(index):
    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
            if 0 < index <= len(tasks):
                tasks[index-1]['done'] = not tasks[index-1]['done']
                with open('tasks.json', 'w') as file:
                    json.dump(tasks, file)
                print("Task successfully updated")
    else:
        print("No task found to update")



def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.delete:
        delete_task(int(args.delete))
    elif args.update:
        update_task(int(args.update))
    else:
        parser.print.help()

if __name__ == '__main__':
    main()
        