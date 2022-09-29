import filecmp
from tkinter import *

f1 = open("C:/Users/user/Desktop/hill climb racing code")
f2 = open("C:/Users/user/Desktop/New Text Document")

# shallow comparison
result = filecmp.cmp(f1, f2)
print(result)
Button(root, text=result, command=popup).pack()
# deep comparison
result = filecmp.cmp(f1, f2, shallow=False)
print(result)
