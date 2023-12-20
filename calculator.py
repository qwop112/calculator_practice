import sys
import numpy
from PyQt5.QtWidgets import *

class Main(QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    
    def init_ui(self):
        main_layout = QVBoxLayout()

        

        ### 레이아웃 생성
        layout_buttons = QGridLayout()
        layout_equation_solution = QFormLayout()

        ### 수식 입력과 답 출력을 동시에 하는 LineEdit
        self.resultLine = QLineEdit("")

        ### layout_equation_solution 레이아웃에 수식 입력과 답 출력을 동시에 하는 위젯 추가
        layout_equation_solution.addRow(self.resultLine)
        
        #추가 버튼들
        button_CE = QPushButton("CE")
        button_C = QPushButton("C")
        button_percent = QPushButton("%")
        button_inverse = QPushButton("1/x")
        button_square = QPushButton("x²")
        button_root = QPushButton("²√x")
        button_pm = QPushButton("+/-")

        layout_buttons.addWidget(button_CE)
        layout_buttons.addWidget(button_C)
        layout_buttons.addWidget(button_percent)
        layout_buttons.addWidget(button_inverse)
        layout_buttons.addWidget(button_square)
        layout_buttons.addWidget(button_root)
        layout_buttons.addWidget(button_pm)

   
        ### 사칙연산 버튼 생성
        button_plus = QPushButton("+")
        button_minus = QPushButton("-")
        button_product = QPushButton("x")
        button_division = QPushButton("/")

        ### 사칙연산 버튼을 클릭했을 때, 각 사칙연산 부호가 수식창에 추가될 수 있도록 시그널 설정
        button_plus.clicked.connect(lambda state, operation = "+": self.button_operation_clicked(operation))
        button_minus.clicked.connect(lambda state, operation = "-": self.button_operation_clicked(operation))
        button_product.clicked.connect(lambda state, operation = "*": self.button_operation_clicked(operation))
        button_division.clicked.connect(lambda state, operation = "/": self.button_operation_clicked(operation))

        ### 사칙연산 버튼을 layout_operation 레이아웃에 추가
        layout_buttons.addWidget(button_plus)
        layout_buttons.addWidget(button_minus)
        layout_buttons.addWidget(button_product)
        layout_buttons.addWidget(button_division)

        ### =, backspace 버튼 생성
        button_equal = QPushButton("=")
        button_backspace = QPushButton("Backspace")

        ### =, backspace 버튼 클릭 시 시그널 설정
        button_equal.clicked.connect(self.button_equal_clicked)
        button_backspace.clicked.connect(self.button_backspace_clicked)

        ### =, backspace 버튼을 layout_clear_equal 레이아웃에 추가
        layout_buttons.addWidget(button_backspace)
        layout_buttons.addWidget(button_equal)

        ### 숫자 버튼 생성하고, layout_number 레이아웃에 추가
        ### 각 숫자 버튼을 클릭했을 때, 숫자가 수식창에 입력 될 수 있도록 시그널 설정
        number_button_dict = {}
        for number in range(0, 10):
            number_button_dict[number] = QPushButton(str(number))
            number_button_dict[number].clicked.connect(lambda state, num = number:
                                                       self.number_button_clicked(num))
            if number >0:
                x,y = divmod(number-1, 3)
                layout_buttons.addWidget(number_button_dict[number], x, y)
            elif number==0:
                layout_buttons.addWidget(number_button_dict[number], 3, 1)

        ### 소숫점 버튼을 입력하고 시그널 설정
        button_dot = QPushButton(".")
        button_dot.clicked.connect(lambda state, num = ".": self.number_button_clicked(num))
        layout_buttons.addWidget(button_dot, 3, 2)

        ### 각 레이아웃을 main_layout 레이아웃에 추가
        main_layout.addLayout(layout_equation_solution)
        main_layout.addLayout(layout_buttons)

        self.setLayout(main_layout)
        self.show()

    #################
    ### functions ###
    #################


    def number_button_clicked(self, num):
        equation = self.equation.text()
        equation += str(num)
        self.equation.setText(equation)

    
    def button_operation_clicked(self, operation):
        equation = self.equation.text()
        equation += operation
        self.equation.setText(equation)

    def button_equal_clicked(self):
        equation = self.equation.text()
        solution = eval(equation)
        self.solution.setText(str(solution))

    def button_clear_clicked(self):
        self.equation.setText("")
        self.solution.setText("")

    def button_backspace_clicked(self):
        equation = self.equation.text()
        equation = equation[:-1]
        self.equation.setText(equation)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())