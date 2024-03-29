from memo_card_layout import (
    app, layout_card,
    lb_Question, lb_Correct, lb_Resalt,
    rbtn_1, rbtn_2, rbtn_3, rbtn_4,
    btn_OK, show_question, show_result
)


from PyQt5.QtWidgets import QWidget, QApplication
from random import shuffle #перемішувати відповіді

card_width, card_height = 600, 500

text_wrong = 'Неправильно'
text_correct = 'Правильно'

frm_question = 'яблуко'
frm_right = 'apple'
frm_wrong1 = 'application'
frm_wrong2 = 'building'
frm_wrong3 = 'caterpillar'

radio_list = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(radio_list)

answer = radio_list[0]
wrong_answer1, wrong_answer2, wrong_answer3 = radio_list[1], radio_list[2], radio_list[3]

def show_data():
    lb_Question.setText(frm_question)
    lb_Correct.setText(frm_right)
    answer.setText(frm_right)
    wrong_answer1.setText(frm_wrong1)
    wrong_answer2.setText(frm_wrong2)
    wrong_answer3.setText(frm_wrong3)


def check_result():
    correct = answer.isChecked()
    if correct:
        lb_Resalt.setText(text_correct)
        show_result()
    else:
        incorrect = wrong_answer1.isChecked() or wrong_answer2.isChecked() or wrong_answer3.isChecked()
        if incorrect:
            lb_Resalt.setText(text_wrong)
            show_result()

def click_OK(self):
    if btn_OK.text() !='Наступне питання':
        check_result()

win_card = QWidget()
win_card.resize(card_width, card_height)
win_card.move(300,300)
win_card.setWindowTitle('Memory Card')


show_data()
show_question()
btn_OK.clicked.connect(click_OK)

win_card.show()
app.exec_()