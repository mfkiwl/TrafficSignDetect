import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox, QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtGui import *
from traffic import Ui_MainWindow
from new_use import SignDetect


class DetailUI(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(DetailUI, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('交通标志识别')

    def openImage(self):
        try:
            sd = SignDetect()
            path, _ = QFileDialog.getOpenFileName(self, '选择图片', 'C:\\', 'Image files (*.jpg)')
            result = sd.do_detect(path)
            self.image.setPixmap(QPixmap(path))
            self.label.setText('检测结果：' + result)
        except:
            QMessageBox.critical(self, '错误', '打开文件失败，可能是文件类型错误', QMessageBox.Ok)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = DetailUI()
    ex.show()
    sys.exit(app.exec_())
