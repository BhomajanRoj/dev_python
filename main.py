import tkinter

def clickBtn():
    text = entry.get()
    button["text"] = text 

root = tkinter.Tk()
root.title("テキスト入力")
root.geometry("400x200")

entry = tkinter.Entry(width=20)
entry.place(x=30, y=100)
#width = 20は半角文字20文字の意味
# entry = tkinter.Entry(width=20)
# entry.place(x=10, y=10)
button = tkinter.Button(text="スタート",command=clickBtn)
button.place(x=20, y=100)

questionsDict = {
  "apple" :"りんご",
  "banana": "バナナ",
  "peach":"もも",
  "orange": "オレンジ"
}
# Add labels, buttons and frame

tkinter.Label(root, text="My Dictionary", font=(
    "Poppins, 20 bold"), fg="Orange").pack(pady=20)
print(questionsDict.keys())


label = tkinter.Label(root,text=questionsDict["apple"],font =("system",30))
label.place(x=200, y=200)

root.mainloop()