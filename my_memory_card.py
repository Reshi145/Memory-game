import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton, 
                             QRadioButton, QButtonGroup, QVBoxLayout, QGridLayout)
import random

class MemoryCardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Memory Card Application')
        self.setGeometry(100, 100, 400, 200)

        self.questions = [
            {
                'question': 'What is the capital of France?',
                'options': ['Paris', 'London', 'Berlin', 'Rome'],
                'correct_answer': 'Paris'
            },
            {
                'question': 'What language do they speak in Brazil?',
                'options': ['Portuguese', 'English', 'Spanish', 'French'],
                'correct_answer': 'Portuguese'
            },
            {
                'question': 'What is the world\'s tallest building?',
                'options': ['Eiffel Tower', 'Empire State Building', 'Shanghai Tower', 'Burj Khalifa'],
                'correct_answer': 'Burj Khalifa'
            }
        ]
        self.current_question = 0

        self.question_label = QLabel()
        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignCenter)

        self.radio_group = QButtonGroup()
        self.radio_buttons = [QRadioButton() for _ in range(4)]
        for button in self.radio_buttons:
            self.radio_group.addButton(button)

        self.answer_button = QPushButton('Answer')
        self.answer_button.clicked.connect(self.check_answer)

        self.next_button = QPushButton('Next Question')
        self.next_button.clicked.connect(self.next_question)
        self.next_button.hide()

        layout = QVBoxLayout()
        grid_layout = QGridLayout()

        grid_layout.addWidget(self.question_label, 0, 0, 1, 2)
        for i, button in enumerate(self.radio_buttons):
            grid_layout.addWidget(button, i // 2 + 1, i % 2)

        grid_layout.setHorizontalSpacing(15)
        grid_layout.setVerticalSpacing(8)

        layout.addLayout(grid_layout)
        layout.addStretch(1)
        layout.addWidget(self.answer_button, alignment=Qt.AlignHCenter)
        layout.addWidget(self.result_label)
        layout.addWidget(self.next_button, alignment=Qt.AlignHCenter)

        self.setLayout(layout)
        self.load_question()

    def load_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.setText(question_data['question'])
        options = question_data['options'].copy()
        random.shuffle(options)
        for button, option in zip(self.radio_buttons, options):
            button.setText(option)

    def check_answer(self):
        correct_answer = self.questions[self.current_question]['correct_answer']
        if self.radio_group.checkedButton().text() == correct_answer:
            self.result_label.setText('Correct!')
        else:
            self.result_label.setText(f'Incorrect. The correct answer is {correct_answer}')
        self.answer_button.hide()
        self.next_button.show()

    def next_question(self):
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.load_question()
            self.next_button.hide()
            self.answer_button.show()
            self.result_label.clear()
            for button in self.radio_buttons:
                button.setChecked(False)
        else:
            self.question_label.setText("Quiz completed!")
            for button in self.radio_buttons:
                button.hide()
            self.answer_button.hide()
            self.next_button.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MemoryCardApp()
    ex.show()
    sys.exit(app.exec_())