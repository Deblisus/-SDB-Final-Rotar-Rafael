from ui import UI
from service import Service

if __name__ == '__main__':
    service = Service()
    ui = UI(service)
    ui.run()