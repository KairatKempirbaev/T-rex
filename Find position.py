from ctypes import windll, Structure, c_ulong, byref
from ctypes import wintypes
from ctypes import *
import ctypes 

DINO_COLOR = 5460819
ENV_COLOR = 16250871

NEXT_LOOKUP_CACTUS={'x': 785, 'y': 237}
NEXT_LOOKUP_PTERODATCIL={'y': 213, 'x': 729}

user32 = ctypes.WinDLL('user32', use_last_error=True)
h = user32.GetDC(0)
class POINT(Structure):
    _fields_ = [("x", c_ulong), ("y", c_ulong)]

def queryMousePosition():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    return { "x": pt.x, "y": pt.y}

pos = queryMousePosition()
print(pos)



#16777215 #I believe its white color of RGB or BGR value, #FFFFFF (according to msdn it should be RGB)
print(windll.gdi32.GetPixel(h,pos['x'],pos['y']))