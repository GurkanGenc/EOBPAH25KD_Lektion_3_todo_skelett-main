""" Todo-modul

todo -> {"done": bool, "task": str, "priority": int}

priority -> 1..5
"""

todos:list[dict] = []


def create_todo(task:str, priority:int) -> dict:
    # skapar en todo och lägger till i todos
    ...

def remove_todo(task:str) -> bool:
    # letar efter en task och tar bort den, gick det bra så returnera vi true, annars false
    ...

def serialize_todos(todos:list[dict]) -> str:
    # konstruerar en sträng som representerar en utskrift av en lista med todos
    string_todos = ""
    ...

def print_all_todos() -> str:
    serialize_todos(todos)

def filter_by_done(done:bool) -> str:
    # filtrera alla todos som har korret status
    ...

def filter_by_priority(priority:int, above:bool) -> str:
    # filrerar alla todos som har korrekt priority
    ...

def mark_todo_done(task:str) -> bool:
    ...

