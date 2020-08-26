from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer, QTime
from PyQt5.QtGui import QColor, QIcon
import sys

class Clock(QLCDNumber):
    def __init__(self):
        super().__init__()

        baslik = "Benim saatim"
        ust = 350
        sol = 350
        genislik = 400
        yukseklik = 400 

        renkler = self.palette()
        renkler.setColor(renkler.WindowText, QColor("white"))
        renkler.setColor(renkler.Window,QColor("black"))
        self.setPalette(renkler)

        self.setWindowTitle(baslik)
        self.setGeometry(ust,sol,genislik,yukseklik)

        self.setSegmentStyle(QLCDNumber.Filled)
        zamanlayıcı = QTimer(self)
        zamanlayıcı.timeout.connect(self.zamani_goster)
        zamanlayıcı.start(1000)

    def zamani_goster(self):
        zaman = QTime.currentTime()
        metin = zaman.toString("hh:mm")
        print(metin)

        self.display(metin)

uygulama = QApplication(sys.argv)
saat = Clock()
saat.show()
sys.exit(uygulama.exec_())







