import tkinter as tk

class MovingButton(tk.Button):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.start_x = master.winfo_width() // 2
        self.start_y = master.winfo_height() // 2
        self.place(x=self.start_x, y=self.start_y)
        self.bind("<Motion>", self.move_button)
        self.bind("<Button-1>", lambda event: "break")

    def move_button(self, event):
        x, y = event.x, event.y
        x0, y0, x1, y1 = self.master.bbox(self)
        dx, dy = x - x0, y - y0
        if dx < 0:
            dx = max(dx, -x0)
        elif dx > 0:
            dx = min(dx, self.master.winfo_width() - x1)
        if dy < 0:
            dy = max(dy, -y0)
        elif dy > 0:
            dy = min(dy, self.master.winfo_height() - y1)
        dist_x = self.start_x - (x + dx)
        dist_y = self.start_y - (y + dy)
        dist = (dist_x**2 + dist_y**2)**0.5
        if dist > 0:
            speed = 100
            dx *= speed / dist
            dy *= speed / dist
            self.place(x=x+dx, y=y+dy)
        else:
            self.place(x=self.start_x, y=self.start_y)

root = tk.Tk()
root.geometry("800x800")

button = MovingButton(root, text="Click here to keep\nan idiot busy for hours!")
button.place(relx=0.5, rely=0.5, anchor="center")

root.mainloop()
