import tkinter as tk
from tkinter import ttk


class WhiteboardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("白板")

        # 初始化变量
        self.current_color = "black"
        self.pen_size = 5
        self.x = None
        self.y = None

        # 创建界面组件
        self.create_widgets()

        # 绑定事件
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_position)

    def create_widgets(self):
        # 工具栏
        toolbar = ttk.Frame(self.root, padding=5)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        # 颜色按钮
        colors = [("黑", "black"), ("红", "red"), ("黄", "yellow"),
                  ("绿", "green"), ("粉", "pink")]
        for text, color in colors:
            btn = tk.Button(toolbar, text=text, bg=color, width=4,
                            command=lambda c=color: self.set_color(c))
            btn.pack(side=tk.LEFT, padx=2, pady=2)

        # 擦除
        eraser_btn = tk.Button(toolbar, text="擦除", command=self.use_eraser)
        eraser_btn.pack(side=tk.LEFT, padx=2, pady=2)

        # 笔触大小调节
        self.size_slider = tk.Scale(toolbar, from_=1, to=20, orient=tk.HORIZONTAL,
                                    label="笔触大小", command=self.set_pen_size)
        self.size_slider.set(self.pen_size)
        self.size_slider.pack(side=tk.LEFT, padx=10)

        # 清空按钮
        clear_btn = tk.Button(toolbar, text="清空", command=self.clear_canvas)
        clear_btn.pack(side=tk.RIGHT, padx=2, pady=2)

        # 创建画布
        self.canvas = tk.Canvas(self.root, width=800, height=600, bg="white")
        self.canvas.pack(expand=True, fill=tk.BOTH)

    def set_color(self, color):
        self.current_color = color

    def set_pen_size(self, size):
        self.pen_size = int(size)

    def use_eraser(self):
        self.current_color = "white"

    def clear_canvas(self):
        self.canvas.delete("all")

    def paint(self, event):
        if self.x is not None and self.y is not None:
            # 绘制线条
            self.canvas.create_line(
                self.x, self.y, event.x, event.y,
                width=self.pen_size,
                fill=self.current_color,
                capstyle=tk.ROUND,
                smooth=True
            )
        # 更新坐标
        self.x = event.x
        self.y = event.y

    def reset_position(self, event):
        self.x = None
        self.y = None


if __name__ == "__main__":
    root = tk.Tk()
    app = WhiteboardApp(root)
    root.mainloop()
