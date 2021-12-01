from tkinter import *


class NewsFeed:
    def __init__(self, root): 
        self.root = root 
        self.root.geometry('1152x864') 
        self.root.title("News Feed") 

        self.newsButton = [] 
        self.newsType = ["home", "coronavirus", "climate", "technology", "business"] 
        bg_color = "#000000"
        text_area_bg = "#ffffff"
        title = Label(self.root, text="NewsPaper Software", font=("times new roman", 30, "bold"), pady=2, bd=12, relief=RAISED, bg=bg_color, fg=text_area_bg).pack(fill=X) 

        F1 = LabelFrame(self.root, font=("times new roman", 20, "bold"), bg=bg_color, fg=text_area_bg, bd=10, relief=RAISED) 
        F1.place(x=0, y=80, width=300, relheight=0.88) 

        for i in range(len(self.newsType)): 
            b = Button(F1, text=self.newsType[i].upper(), width=20, bd=7, font=("times new roman", 15, "bold")) 
            b.grid(row=i, column=0, padx=10, pady=5) 
            self.newsButton.append(b) 

        F2 = Frame(self.root, bd=7, relief=RAISED) 
        F2.place(x=320, y=80, relwidth=0.7, relheight=0.8) 
        news_title = Label(F2, text="News Area", font=("times new roman", 20, "bold"), bd=7, relief=RAISED).pack(fill=X) 
        self.txtarea = Text(F2, font=("times new roman", 15, "bold"), bg=text_area_bg, fg=bg_color) 
        self.txtarea.insert(END, "This is where the news will show up!") 
        self.txtarea.pack(fill=BOTH, expand=1) 


root = Tk() 
obj = NewsFeed(root) 
root.mainloop()