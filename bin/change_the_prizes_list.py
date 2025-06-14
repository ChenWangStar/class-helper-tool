import json
import os
import re
import tkinter as tk
from tkinter import messagebox


# 检测字符串合法性


def change_list_mainloop():
    def contains_single_quote(s):
        return re.search(r"'", s) is not None

    def is_empty(s):
        return not s

    # 添加prizes
    def add_prize():
        prize = prize_entry.get()
        if is_empty(prize):
            messagebox.showerror('Error', '奖品名称不得为空')
        elif contains_single_quote(prize):
            messagebox.showerror('Error', '奖品名不得包含单引号')
        else:
            prizes.append(prize)
            prize_listbox.insert(tk.END, prize)
            prize_entry.delete(0, tk.END)

    # 删除prize
    def delete_prize():
        selected_indices = prize_listbox.curselection()
        for index in selected_indices:
            prize = prize_listbox.get(index)
            prizes.remove(prize)
            prize_listbox.delete(index)

    # 加载prizes列表
    def load_prizes():
        global prizes
        prizes = load_prizes_from_json(os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/prizes.json'))
        prize_listbox.delete(0, tk.END)
        for prize in prizes:
            prize_listbox.insert(tk.END, prize)

    # 保存prizes
    def save_prizes():
        save_prizes_to_json(prizes, os.path.join(os.path.abspath(os.path.dirname(__file__)), '../data/prizes.json'))
        messagebox.showinfo("保存成功", "奖品已成功保存")

    # 读取prizes
    def load_prizes_from_json(file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                prizes = json.load(f)
            return prizes
        else:
            return []

    # 转换为JSON
    def save_prizes_to_json(prizes, file_path):
        with open(file_path, 'w') as f:
            json.dump(prizes, f)

    try:
        root = tk.Tk()
        root.title('Prize Manager')

        # 创建一个列表框来显示prizes
        prize_listbox = tk.Listbox(root, height=6, width=35, border=0)
        prize_listbox.pack(pady=10)

        # 创建一个文本框来输入prize
        prize_entry = tk.Entry(root, width=35)
        prize_entry.pack(pady=10)

        # 创建一个按钮来添加prize
        add_button = tk.Button(root, text='添加', command=add_prize)
        add_button.pack(pady=10)

        # 创建一个按钮来删除prize
        delete_button = tk.Button(root, text='删除', command=delete_prize)
        delete_button.pack(pady=10)

        # 创建一个按钮来加载prizes列表
        load_button = tk.Button(root, text='加载', command=load_prizes)
        load_button.pack(pady=10)

        # 创建一个按钮来保存prizes列表
        save_button = tk.Button(root, text='保存', command=save_prizes)
        save_button.pack(pady=10)

        # prizes列表
        prizes = []

        # 加载prizes列表
        load_prizes()

        root.mainloop()
    except Exception as e:
        messagebox.showerror('Error', str(e))


if __name__ == '__main__':
    change_list_mainloop()
