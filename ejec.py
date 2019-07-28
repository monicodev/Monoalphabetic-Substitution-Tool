import sys
from PyQt5 import QtCore,QtGui
from PyQt5.QtWidgets import *
from ventana import Ui_MainWindow
abecedario = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
abc = [['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'],['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']]

def insertar_letra(posicion,lugar,objeto): 
    letra = objeto.text().upper()
    if (letra==""):
        abc[posicion][lugar]= "*"
    else:
        if (letra in abc[posicion]):
            print("sin clones: " + letra)
            objeto.setText("")
            return 0
        else:
            abc[posicion][lugar]= letra
            print("Agregado: " + abc[posicion][lugar])
    if (ui.btnEncriptar.isChecked()):
        encriptar(1)
    if (ui.btnDesencriptar.isChecked()):
        encriptar(0)

def encriptar(numero):  # 0=Desencriptar   1=Desencriptar
    if (ui.Texto.toPlainText()):
        mensaje = list((ui.Texto.toPlainText().upper()))
        for ind, x in enumerate(mensaje):
            if (x!=" "):
                try:
                    mensaje[ind] = abc[(numero)][abc[(1 ^ numero)].index(x)]
                except ValueError:
                    if x in abecedario:
                        mensaje[ind] = "*"
                    else:
                        mensaje[ind] = ""
                    pass
        mensaje = ("".join(mensaje))
        ui.Texto_2.setPlainText(mensaje)
    
def setOpcion(objeto, numero):
    objeto.Texto.textChanged.connect(lambda: encriptar(numero))
    encriptar(numero)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(main)
    main.show()
    
    ui.plainText1.textChanged.connect(lambda: insertar_letra(0,0,ui.plainText1))
    ui.plainText2.textChanged.connect(lambda: insertar_letra(0,1,ui.plainText2))
    ui.plainText3.textChanged.connect(lambda: insertar_letra(0,2,ui.plainText3))
    ui.plainText4.textChanged.connect(lambda: insertar_letra(0,3,ui.plainText4))
    ui.plainText5.textChanged.connect(lambda: insertar_letra(0,4,ui.plainText5))
    ui.plainText6.textChanged.connect(lambda: insertar_letra(0,5,ui.plainText6))
    ui.plainText7.textChanged.connect(lambda: insertar_letra(0,6,ui.plainText7))
    ui.plainText8.textChanged.connect(lambda: insertar_letra(0,7,ui.plainText8))
    ui.plainText9.textChanged.connect(lambda: insertar_letra(0,8,ui.plainText9))
    ui.plainText10.textChanged.connect(lambda: insertar_letra(0,9,ui.plainText10))
    ui.plainText11.textChanged.connect(lambda: insertar_letra(0,10,ui.plainText11))
    ui.plainText12.textChanged.connect(lambda: insertar_letra(0,11,ui.plainText12))
    ui.plainText13.textChanged.connect(lambda: insertar_letra(0,12,ui.plainText13))
    ui.plainText14.textChanged.connect(lambda: insertar_letra(0,13,ui.plainText14))
    ui.plainText15.textChanged.connect(lambda: insertar_letra(0,14,ui.plainText15))
    ui.plainText16.textChanged.connect(lambda: insertar_letra(0,15,ui.plainText16))
    ui.plainText17.textChanged.connect(lambda: insertar_letra(0,16,ui.plainText17))
    ui.plainText18.textChanged.connect(lambda: insertar_letra(0,17,ui.plainText18))
    ui.plainText19.textChanged.connect(lambda: insertar_letra(0,18,ui.plainText19))
    ui.plainText20.textChanged.connect(lambda: insertar_letra(0,19,ui.plainText20))
    ui.plainText21.textChanged.connect(lambda: insertar_letra(0,20,ui.plainText21))
    ui.plainText22.textChanged.connect(lambda: insertar_letra(0,21,ui.plainText22))
    ui.plainText23.textChanged.connect(lambda: insertar_letra(0,22,ui.plainText23))
    ui.plainText24.textChanged.connect(lambda: insertar_letra(0,23,ui.plainText24))
    ui.plainText25.textChanged.connect(lambda: insertar_letra(0,24,ui.plainText25))
    ui.plainText26.textChanged.connect(lambda: insertar_letra(0,25,ui.plainText26))

    ui.cipherText1.textChanged.connect(lambda: insertar_letra(1,0,ui.cipherText1))
    ui.cipherText2.textChanged.connect(lambda: insertar_letra(1,1,ui.cipherText2))
    ui.cipherText3.textChanged.connect(lambda: insertar_letra(1,2,ui.cipherText3))
    ui.cipherText4.textChanged.connect(lambda: insertar_letra(1,3,ui.cipherText4))
    ui.cipherText5.textChanged.connect(lambda: insertar_letra(1,4,ui.cipherText5))
    ui.cipherText6.textChanged.connect(lambda: insertar_letra(1,5,ui.cipherText6))
    ui.cipherText7.textChanged.connect(lambda: insertar_letra(1,6,ui.cipherText7))
    ui.cipherText8.textChanged.connect(lambda: insertar_letra(1,7,ui.cipherText8))
    ui.cipherText9.textChanged.connect(lambda: insertar_letra(1,8,ui.cipherText9))
    ui.cipherText10.textChanged.connect(lambda: insertar_letra(1,9,ui.cipherText10))
    ui.cipherText11.textChanged.connect(lambda: insertar_letra(1,10,ui.cipherText11))
    ui.cipherText12.textChanged.connect(lambda: insertar_letra(1,11,ui.cipherText12))
    ui.cipherText13.textChanged.connect(lambda: insertar_letra(1,12,ui.cipherText13))
    ui.cipherText14.textChanged.connect(lambda: insertar_letra(1,13,ui.cipherText14))
    ui.cipherText15.textChanged.connect(lambda: insertar_letra(1,14,ui.cipherText15))
    ui.cipherText16.textChanged.connect(lambda: insertar_letra(1,15,ui.cipherText16))
    ui.cipherText17.textChanged.connect(lambda: insertar_letra(1,16,ui.cipherText17))
    ui.cipherText18.textChanged.connect(lambda: insertar_letra(1,17,ui.cipherText18))
    ui.cipherText19.textChanged.connect(lambda: insertar_letra(1,18,ui.cipherText19))
    ui.cipherText20.textChanged.connect(lambda: insertar_letra(1,19,ui.cipherText20))
    ui.cipherText21.textChanged.connect(lambda: insertar_letra(1,20,ui.cipherText21))
    ui.cipherText22.textChanged.connect(lambda: insertar_letra(1,21,ui.cipherText22))
    ui.cipherText23.textChanged.connect(lambda: insertar_letra(1,22,ui.cipherText23))
    ui.cipherText24.textChanged.connect(lambda: insertar_letra(1,23,ui.cipherText24))
    ui.cipherText25.textChanged.connect(lambda: insertar_letra(1,24,ui.cipherText25))
    ui.cipherText26.textChanged.connect(lambda: insertar_letra(1,25,ui.cipherText26))

    regex=QtCore.QRegExp("[a-z-A-Z_]+")
    validator = QtGui.QRegExpValidator(regex)
    ui.plainText1.setValidator(validator)
    ui.plainText2.setValidator(validator)
    ui.plainText3.setValidator(validator)
    ui.plainText4.setValidator(validator)
    ui.plainText5.setValidator(validator)
    ui.plainText6.setValidator(validator)
    ui.plainText7.setValidator(validator)
    ui.plainText8.setValidator(validator)
    ui.plainText9.setValidator(validator)
    ui.plainText10.setValidator(validator)
    ui.plainText11.setValidator(validator)
    ui.plainText12.setValidator(validator)
    ui.plainText13.setValidator(validator)
    ui.plainText14.setValidator(validator)
    ui.plainText15.setValidator(validator)
    ui.plainText16.setValidator(validator)
    ui.plainText17.setValidator(validator)
    ui.plainText18.setValidator(validator)
    ui.plainText19.setValidator(validator)
    ui.plainText20.setValidator(validator)
    ui.plainText21.setValidator(validator)
    ui.plainText22.setValidator(validator)
    ui.plainText23.setValidator(validator)
    ui.plainText24.setValidator(validator)
    ui.plainText25.setValidator(validator)
    ui.plainText26.setValidator(validator)

    ui.cipherText1.setValidator(validator)
    ui.cipherText2.setValidator(validator)
    ui.cipherText3.setValidator(validator)
    ui.cipherText4.setValidator(validator)
    ui.cipherText5.setValidator(validator)
    ui.cipherText6.setValidator(validator)
    ui.cipherText7.setValidator(validator)
    ui.cipherText8.setValidator(validator)
    ui.cipherText9.setValidator(validator)
    ui.cipherText10.setValidator(validator)
    ui.cipherText11.setValidator(validator)
    ui.cipherText12.setValidator(validator)
    ui.cipherText13.setValidator(validator)
    ui.cipherText14.setValidator(validator)
    ui.cipherText15.setValidator(validator)
    ui.cipherText16.setValidator(validator)
    ui.cipherText17.setValidator(validator)
    ui.cipherText18.setValidator(validator)
    ui.cipherText19.setValidator(validator)
    ui.cipherText20.setValidator(validator)
    ui.cipherText21.setValidator(validator)
    ui.cipherText22.setValidator(validator)
    ui.cipherText23.setValidator(validator)
    ui.cipherText24.setValidator(validator)
    ui.cipherText25.setValidator(validator)
    ui.cipherText26.setValidator(validator)

    ui.btnEncriptar.clicked.connect(lambda: setOpcion(ui,1))
    ui.btnDesencriptar.clicked.connect(lambda: setOpcion(ui,0))

    sys.exit(app.exec_())