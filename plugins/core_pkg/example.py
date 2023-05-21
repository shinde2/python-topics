import sys
from app.application import Operation
from importlib.metadata import entry_points


def get_runner(op):
    if op == "add":
        return Operation
    for eps in entry_points()["app_plugins"]:
        if eps.name == op:
            return eps.load()
    raise "Invalid app"

def run_app():
    runner = get_runner(sys.argv[1])
    run = runner(int(sys.argv[2]), int(sys.argv[3]))
    result = run.get()
    print(result)
    