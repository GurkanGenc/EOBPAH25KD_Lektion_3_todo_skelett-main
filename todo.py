""" Todo-modul

todo -> {"done": bool, "task": str, "priority": int}

priority -> 1..5
"""

todos:list[dict] = []


def create_todo(task:str, priority:int) -> dict:
    # skapar en todo och lägger till i todos
    todo = {"done": False, "task": task, "priority": priority}
    todos.append(todo)
    print(todos)
    return todo

def remove_todo(task:str) -> bool:
    # letar efter en task och tar bort den, gick det bra så returnera vi true, annars false
    for t in todos:
        if t["task"].lower() == task.lower():
            todos.remove(t)
            return True
    return False # if its not found

def serialize_todos(todos:list[dict]) -> str:
    # konstruerar en sträng som representerar en utskrift av en lista med todos
    string_todos = ""
    if not todos:
        return "No todos found. \n"

    string_todos = ""
    for i, t in enumerate(todos, start=1):
        status = "Y" if t["done"] else "N"
        string_todos += f"{i}. [{status}] {t['task']} (Priority: {t['priority']})\n"
    return string_todos

def print_all_todos() -> str:
    return serialize_todos(todos)

def filter_by_done(done:bool) -> str:
    # filtrera alla todos som har korret status
    ...

def filter_by_priority(priority:int, above:bool) -> str:
    # filrerar alla todos som har korrekt priority
    if priority < 1 or priority > 5:
        return "Priority must be between 1 and 5"
    
    if not todos:
        return "No todos found. \n"
    
    filtered = []
    if above:
        for todo in todos:
            if todo["priority"] >= priority:
                filtered.append(todo)
                
    else:
        for todo in todos:
            if todo["priority"] <= priority:
                filtered.append(todo)
    
    return serialize_todos(filtered)

def mark_todo_done(task:str) -> bool:
    if task == todos["todo"]["task"]:
        todos["todo"]["done"] = True
        return True

