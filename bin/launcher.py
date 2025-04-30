import tkinter as tk
import subprocess
import os


def run_script(script_name):
    subprocess.Popen(['python', os.path.join(os.path.abspath(os.path.dirname(__file__)), script_name)], shell=True)


# 创建主窗口
root = tk.Tk()
root.title("启动器")

# 设置窗口大小
root.geometry("300x300")

# 创建抽奖按钮
btn_draw = tk.Button(root, text="抽奖", command=lambda: run_script('prizes.py'))
btn_draw.pack(pady=10)

# 创建抽号按钮
btn_random_number = tk.Button(root, text="抽号", command=lambda: run_script('random_number.py'))
btn_random_number.pack(pady=10)

btn_generated_attendance = tk.Button(root, text='签到', command=lambda: run_script('generated_attendance.py'))
btn_generated_attendance.pack(pady=10)

btn_timer = tk.Button(root, text='计时器', command=lambda: run_script('timer.py'))
btn_timer.pack(pady=10)

btn_whiteboard = tk.Button(root, text='白板', command=lambda: run_script('whiteboard.py'))
btn_whiteboard.pack(pady=10)

root.mainloop()
