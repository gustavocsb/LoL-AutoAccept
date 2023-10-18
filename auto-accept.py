from lcu_driver import Connector # Lib para conectar com a API do League of Legends
# Lib para criar GUI simples em Python
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QCheckBox, QLabel, QWidget, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QPalette, QColor, QFont, QIcon
from PyQt5.QtCore import Qt
import sys
import threading # Executando o GUI e a conexão na API em threads diferentes
import os

# Criando o GUI do app
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Auto Accept")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon("qiydisc_1.ico"))

        # Setando as cores do background e da font
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor(0, 0, 0))
        palette.setColor(QPalette.WindowText, Qt.white)
        self.setPalette(palette)

        # Font instalada no OS
        font = QFont("GodOfWar", 15, QFont.Bold)

        # Alinhando a checkbox e a string de status no centro
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Criando um espaçamentro entre a checkbox/string de status com a borda da janela do app
        spacer_top = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        spacer_bottom = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding) 

        self.status_label = QLabel("Disconnected")
        self.status_label.setFont(font)
        
        self.checkbox = QCheckBox("Auto Accept")
        self.checkbox.setFont(font)

        # Criando a GUI devidamente
        layout.addItem(spacer_top)
        layout.addWidget(self.status_label)
        layout.addWidget(self.checkbox)
        layout.addItem(spacer_bottom)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    # Boolean da checkbox para aceitar ou não o matchmaking
    def update_accepting_queue(self, checked):
        global is_accepting_queue
        is_accepting_queue = checked

    # Fechando os processos do app
    def closeEvent(self, event):
        os._exit(0)

# Instanciando e configurando o conector
connector = Connector()
is_accepting_queue = True

# Manipulando a string para 'Connected' quando inicializar o conector
@connector.ready
async def connect(connection):
    window.status_label.setText('Connected')

# Manipulando a string para 'Disconnected' quando o conector for fechado
@connector.close
async def disconnect(_):
    window.status_label.setText('Disconnected')

# Após um UPDATE no endpoint, é verificado se a checkbox é TRUE e faz uma requisição POST para aceitar o matchmaking
@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types=('UPDATE',))
async def accept_queue(connection, event):
    if is_accepting_queue and event.data['state'] == 'InProgress':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')

def run_gui():
    app = QApplication(sys.argv)
    global window
    window = Window()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec())

def run_connector():
    connector.start()

# Inicializando a GUI e o conector em threads diferentes para execução simultânea
threading.Thread(target=run_gui).start()
threading.Thread(target=run_connector).start()
