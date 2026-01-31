import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import tkinter as tk
from tkinter import Scale, HORIZONTAL
from PIL import Image, ImageTk

def preprocess(image_path):
    
    # Step 1: Load image
    image = cv.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found or invalid format")
    
    gray_image= cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray_image=cv.GaussianBlur(gray_image, (9,9), 1.5)

    return image, gray_image

def auto_tune_parameters(gray):
    h,w = gray.shape
    area = h*w
    if(area==0):
        raise ValueError("Area shouldnt be 0")
    
    else:
        edges = cv.Canny(gray, 100, 200)
        edge_density = np.sum(edges > 0)/area

        if (edge_density < 0.02):
            param2 = 40
        elif (edge_density < 0.05):
            param2 = 60
        else:
            param2 = 80

        table = {
            "dp": 1.2,
            "minDist": int(min(h, w)*0.15),
            "param1": 100,
            "param2": param2,
            "minRadius": int(min(h, w)*0.05),
            "maxRadius": int(min(h, w)*0.15)
        }

    return table

def circles(gray_image, table):
    if(gray_image is None):
        return None
    
    crcl=cv.HoughCircles(gray_image,cv.HOUGH_GRADIENT, dp=table["dp"], minDist=table["minDist"], param1=table["param1"], param2=table["param2"], minRadius=table["minRadius"], maxRadius=table["maxRadius"])

    if(crcl is not None):
        crcl = np.uint16(np.around(crcl[0]))

    return crcl

class GUI:
    def __init__(self, root, image, gray, init_params):
        self.root=root
        self.image=image
        self.gray=gray
        self.params=init_params.copy()

        self.panel=tk.Label(root)
        self.panel.pack(side="left", padx=10, pady=10)

        controls=tk.Frame(root)
        controls.pack(side="right", padx=10)

        self.sliders={}
        self.add_slider(controls, "dp",10 ,30, int(self.params["dp"]*10))
        self.add_slider(controls, "minDist", 1, 300, self.params["minDist"])
        self.add_slider(controls, "param1", 1, 300, self.params["param1"])
        self.add_slider(controls, "param2", 1, 200, self.params["param2"])
        self.add_slider(controls, "minRadius", 1, 300, self.params["minRadius"])
        self.add_slider(controls, "maxRadius", 1, 400, self.params["maxRadius"])

        self.update_image()

    def add_slider(self, parent, name, minv, maxv, init):
        tk.Label(parent, text=name).pack()
        slider=Scale(parent, from_=minv, to=maxv, orient=HORIZONTAL, command=self.on_change)
        slider.set(init)
        slider.pack()
        self.sliders[name]=slider

    def on_change(self, _):
        self.update_image()

    def update_image(self):
        self.params["dp"] = self.sliders["dp"].get() / 10
        self.params["minDist"] = self.sliders["minDist"].get()
        self.params["param1"] = self.sliders["param1"].get()
        self.params["param2"] = self.sliders["param2"].get()
        self.params["minRadius"] = self.sliders["minRadius"].get()
        self.params["maxRadius"] = self.sliders["maxRadius"].get()

        if self.params["minRadius"] >= self.params["maxRadius"]:
            self.params["maxRadius"] = self.params["minRadius"] + 1
    
        output=self.image.copy()
        crcl = circles(self.gray, self.params)
        if(crcl is not None):
            for idx,(x, y, r) in enumerate(crcl):
                cv.circle(output,(x,y), r, (0, 255,0), 2)
                cv.circle(output,(x,y), 2, (0,0, 255))
                cv.putText(output, f"ID:{idx} r={r}",(x-40, y-r-10), cv.FONT_HERSHEY_PLAIN, 0.5, (255, 0, 0),1)

        rgb = cv.cvtColor(output, cv.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(Image.fromarray(rgb))
        self.panel.configure(image=img)
        self.panel.image = img

def main():
    image_path = input("Enter image path: ").strip()

    image, gray = preprocess(image_path)
    if image is None:
        return

    auto_params = auto_tune_parameters(gray)
    print("Auto-tuned parameters:", auto_params)

    
    root = tk.Tk()
    GUI(root, image, gray, auto_params)
    root.mainloop()


if __name__ == "__main__":
    main()
            


        


    