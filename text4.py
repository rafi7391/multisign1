import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a text editor widget
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)

        # Create a menu bar with a File menu
        menubar = self.menuBar()
        file_menu = menubar.addMenu('File')

        # Add an Open action to the File menu
        open_action = QAction('Open', self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        # Add a Save action to the File menu
        save_action = QAction('Save', self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        # Set the window properties
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Spending Conditions Editor')
        self.show()

    def open_file(self):
        # Open a file dialog to select a file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Spending Condition Files (*.spend)')
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        if file_dialog.exec_() == QFileDialog.Accepted:
            filename = file_dialog.selectedFiles()[0]

            # Load the file contents into the text editor
            with open(filename, 'r') as f:
                self.textEdit.setPlainText(f.read())

    def save_file(self):
        # Open a file dialog to select a file
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter('Spending Condition Files (*.spend)')
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        if file_dialog.exec_() == QFileDialog.Accepted:
            filename = file_dialog.selectedFiles()[0]

            # Save the text editor contents to the file
            with open(filename, 'w') as f:
                f.write(self.textEdit.toPlainText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
