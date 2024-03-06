from ui import MouseApp
from database import MouseDatabase


if __name__ == "__main__":
    database = MouseDatabase()
    app = MouseApp() 
    app.mainloop()