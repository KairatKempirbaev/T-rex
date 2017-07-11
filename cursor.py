from ctypes import windll, Structure, c_ulong, byref
from ctypes import wintypes
from ctypes import *
import ctypes 
import random                                                                            


DINO_COLOR = 5460819
ENV_COLOR = 16250871
NEXT_LOOKUP_CAC={'x': 795, 'y': 247}
NEXT_LOOKUP_PTER={'y': 212, 'x': 740}
DINO_POSITION={'y': 231, 'x': 726}
class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}  

#pos = queryMousePosition()
#print(pos)
#user= windll.LoadLibrary(" c:\\winnt\\system32\\user32.dll") 
user32 = ctypes.WinDLL('user32', use_last_error=True)
h = user32.GetDC(0)

#16777215 #I believe its white color of RGB or BGR value, #FFFFFF (according to msdn it should be RGB)
def create_new_range():
	three_pairs=[]
	for _ in range(3):
		three_pairs.append(random.randrange(DINO_POSITION["x"],NEXT_LOOKUP_CAC["x"]))
	return three_pairs
def jump_baby(three_elements):
	for i in three_elements:
		if windll.gdi32.GetPixel(h,i,NEXT_LOOKUP_CAC["y"]+random.randrange(-2,2))!= ENV_COLOR:
			return True      
	return False
def look_position():
	while True:
		if windll.gdi32.GetPixel(h,NEXT_LOOKUP_CAC["x"],NEXT_LOOKUP_CAC["y"]) != ENV_COLOR :
			return True

		
