from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
QUESTION_FONT = ("Ariel", 20, "italic")
SCORE_FONT = ("Ariel", 20, "italic")


class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label_score = Label(text="Score: 0", font=SCORE_FONT, bg=THEME_COLOR, fg="white", anchor="center")
        self.label_score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="Question",
                                                     font=QUESTION_FONT,
                                                     fill=THEME_COLOR,
                                                     width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.wrong_button_img = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_button_img, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.select_false)
        self.wrong_button.grid(row=2, column=1)

        self.right_button_img = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_button_img, highlightthickness=0, highlightbackground=THEME_COLOR,command=self.select_true)
        self.right_button.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def select_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def select_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)

