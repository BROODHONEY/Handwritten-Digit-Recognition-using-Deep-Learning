from keras.models import load_model
from tkinter import *
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np
import matplotlib.pyplot as plt

model = load_model('digit_recognizer_model.h5')

def predict_digit(img):
    # Resize, convert to grayscale, and invert colors
    img = img.resize((28, 28)).convert('L')  # Convert to grayscale
    img = np.array(img)
    img = 255 - img  # Invert colors (white digit on black background)


    plt.figure(figsize=(2, 2))
    plt.imshow(img, cmap='gray')
    plt.show()

    img = img / 255.0  # Normalize pixel values (0-1)
    img = img.reshape(1, 28, 28, 1)  # Reshape to match input shape

    # Predict using the model
    prediction = model.predict(img)

    # Extract predicted digit and confidence
    digit = np.argmax(prediction)  # Predicted digit
    acc = np.max(prediction) * 100  # Confidence percentage

    # Return both digit and accuracy
    return digit, acc

class GUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0

        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg = "white", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text = "Recognise", command = self.classify_handwriting)
        self.button_clear = tk.Button(self, text = "Clear", command = self.clear_all)

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1,pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)

        #self.canvas.bind("<Motion>", self.start_pos)
        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")
        self.label.configure(text='Thinking..')

    def classify_handwriting(self):
        HWND = self.canvas.winfo_id()  # Get handle of the canvas
        x = self.canvas.winfo_rootx()
        y = self.canvas.winfo_rooty()
        w = x + self.canvas.winfo_width()
        h = y + self.canvas.winfo_height()

        # Grab the canvas area
        img = ImageGrab.grab(bbox=(x, y, w+x, h+y))

        digit, acc = predict_digit(img)
        self.label.configure(text=str(digit) + ', ' + str(int(acc * 100)) + '%')

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 10  # Thicker lines
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')

app = GUI()
mainloop()