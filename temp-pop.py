# import tkinter as tk
# from tkinter import simpledialog
#
#
# def chat(ta):
#     while True:
#         user_input = simpledialog.askstring("Chat", "Enter your message:")
#         if user_input is None:
#             break
#
#         ans = 'test.main(user_input)'
#         ta.insert(tk.END, f"You: {user_input}\n")
#         ta.insert(tk.END, f"Bot: {ans}\n\n")
#         ta.see(tk.END)  # 滚动到文本末尾
#
#
#
# if __name__ == "__main__":
#     user_input = ''
#     root = tk.Tk()
#     text_area = tk.Text(root)
#     text_area.pack()
#     chat(text_area)
#
#
#
#     root.mainloop()
#
#     root.withdraw()


from tkinter import simpledialog
from tkinter import *
import tkinter as tk
import test

def main():
    root = Tk()
    #root.withdraw()
    chat_box = tk.Text(root)
    chat_box.pack()

    while True:
        user_input = simpledialog.askstring("输入", "请输入您的问题：")
        chat_box.insert(tk.END, 'user:'+user_input+'\n')
        ans = test.main(user_input)
        chat_box.insert(tk.END, 'ans:'+ans+'\n')
        #chat_box.see(tk.END)

    root.mainloop()


if __name__ == "__main__":
    main()
