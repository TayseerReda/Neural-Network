import tkinter as tk
from tkinter import *
from perceptron import precptron_train,testing


# class GUI:
def on_submit():
    feature1 = feature1_var.get()
    feature2 = feature2_var.get()
    class1 = class_var1.get()
    class2 = class_var2.get()
    learning_rate = float(learning_rate_entry.get())
    num_epochs = int(num_epochs_entry.get())
    mse = mse_entry.get()
    bias = var1.get()
    algorithm = var3.get()

    bias_selected = bias == 1
    algorithm_selected = algorithm == 0

    # Call the perceptron_train function with the correct arguments
    
    if bias_selected:
             W,x_test,y_test=precptron_train(feature1, feature2, class1, class2, learning_rate, num_epochs, 1)
    else:
            W,x_test,y_test=precptron_train(feature1, feature2, class1, class2, learning_rate, num_epochs, 0)
    fail,success=testing(W,x_test,y_test)
    accuracy=(success/(fail+success))*100
    print(accuracy)
    
features = [ 
    "Area", 
    "Perimeter", 
    "MajorAxisLength", 
    "MinorAxisLength", 
    "roundnes", 
] 

classes=[
    "BOMBAY",
    "CALI",
    "SIRA"
    ]

window = tk.Tk()
window.title("neural network")
window.geometry("500x500")

feature1_label = tk.Label(window, text="Select Feature 1")
feature1_label.place(x=100,y=20)

feature1_var = tk.StringVar(value=features[0])
feature1_dropdown = tk.OptionMenu(window, feature1_var, *features)
feature1_dropdown.place(x=220,y=15)

# feature1_value_label = tk.Label(window, text="Enter Feature Value 1")
# feature1_value_label.place(x=230,y=15)

# feature1_entry = tk.Entry(window)
# feature1_entry.place(x=350,y=15)

feature2_label = tk.Label(window, text="Select Feature 2")
feature2_label.place(x=100,y=65)

feature2_var = tk.StringVar(value=features[1])
feature2_dropdown = tk.OptionMenu(window, feature2_var, *features)
feature2_dropdown.place(x=220,y=60)

# feature2_value_label = tk.Label(window, text="Enter Feature Value 2")
# feature2_value_label.place(x=230,y=60)

# feature2_entry = tk.Entry(window)
# feature2_entry.place(x=350,y=60)

# Class selection
class1_label = tk.Label(window, text="Class 1:")
class1_label.place(x=140,y=110)



class_var1 = tk.StringVar(value=classes[0])
class_var2 = tk.StringVar(value=classes[1])
class1_dropdown= tk.OptionMenu(window,class_var1 , *classes)
class1_dropdown.place(x=220,y=100)

class2_label = tk.Label(window, text="Class 2")
class2_label.place(x=140,y=150)


class2_dropdown =tk.OptionMenu(window,class_var2 , *classes)
class2_dropdown.place(x=230,y=145)

# Learning Rate
learning_rate_label = tk.Label(window, text="Learning Rate (eta)")
learning_rate_label.place(x=100,y=190)

learning_rate_entry = tk.Entry(window)
learning_rate_entry.place(x=210,y=190)

# Number of Epochs
num_epochs_label = tk.Label(window, text="Number of Epochs (m)")
num_epochs_label.place(x=80,y=235)

num_epochs_entry = tk.Entry(window)
num_epochs_entry.place(x=210,y=235)
        
TLabel=tk.Label(window, text="MSE Threshold")
TLabel.place(x=110, y=280)
mse_entry=tk.Entry(window)
mse_entry.place(x=210,y=280)
mse_entry.focus_set()
        
BLabel=tk.Label(window, text="Bias")
BLabel.place(x=150, y=325)
var1=tk.IntVar()
tk.Checkbutton(window, text="yes", variable=var1).place(x=205, y=325)
# var2=tk.IntVar()
# tk.Checkbutton(window, text="no", variable=var2).place(x=260, y=325)
        
ALabel=tk.Label(window, text="Used Algorithm")
ALabel.place(x=105, y=370)
var3=tk.IntVar()
bt1=tk.Radiobutton(window, text="Perceptron",value=0 , variable=var3).place(x=205, y=370)
var4=tk.IntVar()
bt2=tk.Radiobutton(window, text="Adaline",value=1, variable=var3).place(x=290, y=370)
        
b=tk.Button(window, text="Generate", width=20, command=on_submit)
b.place(x=180, y=420)

# Run the Tkinter event loop
window.mainloop()