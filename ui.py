THEME_COLOR = "#375362"
T = True
F = False
from tkinter import *
from quiz_brain import QuizBrain
from tkinter import messagebox
class Interface:

    def __init__(self,quizz_brain : QuizBrain):
        self.window = Tk()
        self.window.title("Quizz Game")
        self.window.config(pady=20,padx=20,bg=THEME_COLOR)
        self.quizz = quizz_brain

        # here is our score code
        self.score = Label(text=f"Score :0",font=('Calibari',25,'bold'))
        self.score.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score.grid(row=0,column=1,columnspan=2)
        #here our canvas code
        self.canvas = Canvas()
        que = self.quizz.next_question()
        self.canvas.config(height=350,width=350)
        self.question = self.canvas.create_text(175,175,width=280,text=que,font=("Arial",20,"italic"))
        self.canvas.grid(row=1, column=0, padx=20, pady=20, columnspan=2)

        #here is our right button code
        rig_image = PhotoImage(file="Images/true.png")
        self.right_button = Button(image=rig_image,bg=THEME_COLOR,highlightthickness=0,command=self.right_pressed)
        self.right_button.grid(row=2,column=0,padx=20,pady=20)

        # here is our left button code
        left_image = PhotoImage(file="Images/false.png")
        self.left_button = Button(image=left_image,bg=THEME_COLOR,highlightthickness=0,command=self.wrong_pressed)
        self.left_button.grid(row=2, column=1, padx=20, pady=20)

        self.window.mainloop(0)

    def new_que(self):
        if self.quizz.still_has_questions():
            quest = self.quizz.next_question()
            self.canvas.itemconfig(self.question,text = quest)
        else:
            messagebox.showinfo(title="You have Complited the game.", message=f"your Score is {self.quizz.score}.")
            self.window.destroy()
    def right_pressed(self):
        self.quizz.check_answer(user_answer="True")
        self.new_que()
        self.score.config(text=f"Score :{self.quizz.score} ")
    def wrong_pressed(self):
        self.quizz.check_answer(user_answer="False")
        self.new_que()
