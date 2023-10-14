from myapp import Flask, AppContext
from globals import g

def main():

    app = Flask()

    ctx = app.app_context()
    ctx.push()
    ctx.y = "b"
    print(g.get().y) # prints b

    # Creates new context and g points to it
    # changes made outside to ctx context dont
    # affect current context
    with app.app_context():
        print(g.get().y) # prints a

    ctx.pop()

if __name__ == "__main__":
    main()
