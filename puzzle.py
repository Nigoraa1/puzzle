from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton
)

from random import shuffle


class Button(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(100,100)
        self.setStyleSheet('''
            font-weight: bold;
            font-size: 60px; 
            border: 3px solid black;
            border-radius: 20%; 
            background: #008DDA;
        ''')

class ButtonRed(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedSize(100,100)
        self.setStyleSheet('''
            font-weight: bold;
            font-size: 60px; 
            border: 3px solid black;
            border-radius: 20%; 
            background: red;
        ''')


class Puzzle(QWidget):
    def __init__(self, size) -> None:
        super().__init__()
        self.size = size
        self.matrix = []
        self.grid = QGridLayout()

        self.setWindowTitle("Puzzle 15")
        self.setFixedSize(500,500)
        self.setStyleSheet("""
            background: #41C9E2;
        """)
        self.show()
        self.initUI()


    def initUI(self):
        self.create_buttons()
        self.connection_change_btns()
        if self.check_winner():
            print("win")
            return


    def create_buttons(self):
        numbers = self.create_numbers()
        index = 0
        
        for x in range(self.size):
            row = []
            for y in range(self.size):
                button = Button(f'{numbers[index]}')
                self.grid.addWidget(button, x,y)
                row.append(button)
                index += 1
            self.matrix.append(row)
        self.setLayout(self.grid)


    def create_numbers(self):
        numbers = [str(i) for i in range(1, self.size*self.size)] + [" "]
        shuffle(numbers)
        return numbers 
    

    def connection_change_btns(self):
        for x in range(self.size):
            for y in range(self.size):
                self.matrix[x][y].clicked.connect(self.change_postion)
                if self.matrix[x][y].text() == " ":
                    self.matrix[x][y].hide() 
    

    def change_postion(self):
        if self.check_winner():
            print("win")
            return
        
        btn = self.sender()
        for x in range(self.size):
            for y in range(self.size):
                if btn == self.matrix[x][y]:
                    if x-1 >= 0 and self.matrix[x-1][y].text() == ' ':
                        self.matrix[x-1][y].setText(self.matrix[x][y].text())
                        self.matrix[x-1][y].show()
                        self.matrix[x][y].setText(" ")
                        self.matrix[x][y].hide()
                    elif x+1 < self.size and self.matrix[x+1][y].text() == ' ':
                        self.matrix[x+1][y].setText(self.matrix[x][y].text())
                        self.matrix[x+1][y].show()
                        self.matrix[x][y].setText(" ")
                        self.matrix[x][y].hide()
                    elif y-1 >= 0 and self.matrix[x][y-1].text() == ' ':
                        self.matrix[x][y-1].setText(self.matrix[x][y].text())
                        self.matrix[x][y-1].show()
                        self.matrix[x][y].setText(" ")
                        self.matrix[x][y].hide()
                    elif y+1 < self.size and self.matrix[x][y+1].text() == ' ':
                        self.matrix[x][y+1].setText(self.matrix[x][y].text())
                        self.matrix[x][y+1].show()
                        self.matrix[x][y].setText(" ")
                        self.matrix[x][y].hide()
                    

    def check_winner(self):
        n = 1
        for x in range(self.size):
            for y in range(self.size):
                if self.matrix[x][y].text() != str(n):
                    return False
                n += 1
                if self.size * self.size == n:
                    return True
                    


app = QApplication([])
game = Puzzle(4)
app.exec_()