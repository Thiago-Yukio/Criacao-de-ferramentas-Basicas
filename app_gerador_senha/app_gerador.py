# Bibliotecas
import string
from PySide6.QtGui import QIcon
from random import choices
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication, QMessageBox
import os
import sys

def caminho_recurso(nome):
    if getattr(sys, "frozen", False):
        return os.path.join(sys._MEIPASS, nome)
    return os.path.join(os.path.dirname(__file__), nome)


# Criar todos os caracteres
letras = string.ascii_letters
numeros = string.digits
especiais = string.punctuation
caracteres = letras + numeros + especiais


def gerador_senha(indicador: int) -> str:
    """
    Recebe a quantidade de caracteres e retorna uma senha aleatória.
    """
    senha_aleatorio_lista = choices(caracteres, k=indicador)
    senha_aleatoria = ''.join(senha_aleatorio_lista)
    return senha_aleatoria


class GeradorSenha:
    """Classe que gera senha."""

    def __init__(self):
        """Função responsável por inicializar a classe."""

        # Carregador do arquivo da GUI
        carregador = QUiLoader()

        # Carregar o arquivo da GUI
        self.ui = carregador.load(caminho_recurso("interface_gerador_senha.ui"))

        # Mudar o título e colocar o ícone do app
        self.ui.setWindowTitle('Gerador de senha')
        self.ui.setWindowIcon(QIcon(caminho_recurso("icone.ico")))

        # Botão gerar senha
        self.ui.botao_gerar_senha.clicked.connect(self.gerar_senha)

    def gerar_senha(self):
        """Função responsável por gerar senha aleatória."""

        try:
            # Obter a quantidade de caracteres
            quantidade = int(self.ui.linha_quantidade_caracteres.text())
        except ValueError:
            QMessageBox.warning(self.ui,"Erro","Digite um número válido.")
            return

        # Criar senha
        senha = gerador_senha(quantidade)

        # Colocar senha no campo indicado
        # OBS.: O ideal é usar outro QLineEdit para exibir a senha.
        campo_senha = self.ui.linha_senha_aleatoria
        campo_senha.setText(senha)
        campo_senha.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication()

    interfaces = GeradorSenha()
    interfaces.ui.show()

    app.exec()