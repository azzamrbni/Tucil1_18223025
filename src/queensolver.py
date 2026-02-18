import tkinter as tk
from tkinter import filedialog, messagebox
import time
import random
import os
from PIL import Image, ImageDraw, ImageFont

def areachecker(perm, board):
    block= set()
    for r in range(len(perm)):
        area = board[r][perm[r]]
        if area in block:
            return False
        block.add(area)
    
    return True

def diagonalchecker(perm):
    for i in range(len(perm) - 1):
        if abs(perm[i] - perm[i+1]) == 1:
            return False
    
    return True

def nextperm(arr):
    n = len(arr)
    i = n -2
    
    while i >= 0 and arr[i] >= arr[i+1]:
        i-= 1
    
    if i <0:
        return False
    
    j= n - 1
    
    while arr[j] <= arr[i]:
        j -= 1
    arr[i], arr[j] = arr[j], arr[i]
    arr[i+ 1:] = reversed(arr[i+1:])
    
    return True

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Queen Solver")
        self.board = []
        self.n = 0
        self.perm = []
        self.answer = None
        self.count = 0
        self.running = False
        self.starttime = 0
        self.colors = {}
        self.filename = None
        self.update_interval = 2000
        top = tk.Frame(root)
        top.pack(pady=5)

        tk.Button(top, text="Load", command=self.load, width=10).grid(row=0, column=0, padx=5)
        tk.Button(top, text="Solve", command=self.start, width=10).grid(row=0, column=1, padx=5)
        tk.Button(top, text="Save Image", command=self.saveimg, width=12).grid(row=0, column=2, padx=5)
        tk.Button(top, text="Save Text", command=self.savetxt, width=12).grid(row=0, column=3, padx=5)
        self.info_label = tk.Label(root, text="")
        self.info_label.pack()
        self.stats_label = tk.Label(root, text="")
        self.stats_label.pack()
        self.canvas = tk.Canvas(root)
        self.canvas.pack(pady=5)

    def colorgenerator(self):
        differentcolors = set(sum(self.board, []))
        self.colors = {}
        for area in differentcolors:
            r = random.randint(180,255)
            g = random.randint(180, 255)
            b = random.randint(180, 255)
            self.colors[area] = f'#{r:02x}{g:02x}{b:02x}'

    def load(self):
        filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not filepath:
            return

        self.filename =os.path.basename(filepath)
        with open(filepath, 'r') as f:
            self.board = [list(line.strip()) for line in f if line.strip()]

        self.n = len(self.board)

        for row in self.board:
            if len(row) !=self.n:
                messagebox.showerror("Error", "Board harus NxN")
                return

        self.perm = list(range(self.n))
        self.answer = None
        self.colorgenerator()
        size= min(600, 60 * self.n)
        self.canvas.config(width=size, height=size)
        self.draw()
        self.info_label.config(text=f"Board {self.n}x{self.n} loaded")

    def draw(self, perm=None):
        self.canvas.delete("all")
        if self.n == 0:
            return

        canvassize = int(self.canvas["width"])
        cell = canvassize // self.n

        for r in range(self.n):
            for c in range(self.n):
                x1 = c* cell
                y1 = r*cell
                x2 = x1+ cell
                y2 = y1+ cell
                area = self.board[r][c]
                color = self.colors.get(area, "white")
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="black"
                )

                if perm and perm[r] == c:
                    self.canvas.create_text(
                        x1 + cell/2,
                        y1 +cell/2,
                        text="#",
                        font=("Arial", int(cell/2), "bold"),
                        fill="black"
                    )
                else:
                    self.canvas.create_text(
                        x1+cell/2,
                        y1+cell/2,
                        text=area,
                        font=("Arial", int(cell/3))
                    )

    def start(self):
        if not self.board:
            messagebox.showerror("Error", "Load file terlebih dahulu!")
            return

        self.running =True
        self.count = 0
        self.starttime = time.time()
        self.perm = list(range(self.n))
        self.answer = None
        self.solve()

    def solve(self):
        if not self.running:
            return

        for _ in range(self.update_interval):
            self.count += 1

            if areachecker(self.perm, self.board) and diagonalchecker(self.perm):
                self.running = False
                self.answer = self.perm[:]
                end = time.time()
                self.draw(self.answer)
                self.stats_label.config(
                    text=f"Solution ~ {self.count} permutations ~ {(end-self.starttime)*1000:.2f} ms"
                )
                return

            if not nextperm(self.perm):
                self.running = False
                end = time.time()
                self.stats_label.config(
                    text=f"No Solution ~ {self.count} permutations ~ {(end-self.starttime)*1000:.2f} ms"
                )
                return

        self.draw(self.perm)
        self.stats_label.config(text=f"Checked: {self.count}")
        self.root.after(1, self.solve)

    def savetxt(self):
        if self.answer is None:
            messagebox.showerror("Error", "Belum ada solusi!")
            return

        dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        savefolder = os.path.join(dir, "test")
        basename = self.filename.replace(".txt", "")
        savepath = os.path.join(savefolder, f"{basename}_solution.txt")

        with open(savepath, "w") as f:
            for r in range(self.n):
                row = ""
                for c in range(self.n):
                    if self.answer[r] == c:
                        row += "#"
                    else:
                        row += self.board[r][c]
                f.write(row+"\n")

        messagebox.showinfo("Saved", f"Saved to:\n{savepath}")

    def saveimg(self):
        if self.answer is None:
            messagebox.showerror("Error", "Belum ada solusi!")
            return

        dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        savefolder = os.path.join(dir, "test")
        basename = self.filename.replace(".txt", "")
        savepath = os.path.join(savefolder, f"{basename}_solution.png")
        size = 80
        imgsize = self.n*size
        image = Image.new("RGB", (imgsize, imgsize), "white")
        draw = ImageDraw.Draw(image)

        try:
            font = ImageFont.truetype("arial.ttf", int(size/2))
        except:
            font = ImageFont.load_default()

        for r in range(self.n):
            for c in range(self.n):
                x1 = c*size
                y1 = r*size
                x2 = x1+size
                y2 = y1+size

                area = self.board[r][c]
                color = self.colors.get(area, "#ffffff")

                draw.rectangle([x1, y1, x2, y2], fill=color, outline="black")

                if self.answer[r] == c:
                    text = "#"
                else:
                    text = area

                bbox = draw.textbbox((0, 0), text, font=font)
                w= bbox[2]-bbox[0]
                h = bbox[3]-bbox[1]

                draw.text(
                    (x1+(size-w)/2, y1+(size-h)/2),
                    text,
                    fill="black",
                    font=font
                )

        image.save(savepath)
        messagebox.showinfo("Saved", f"Saved to:\n{savepath}")

if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()