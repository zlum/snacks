# Usage:
# mc = mousecapture.MouseCapture()

# try:
#     mc.run()
# except mousecapture.ListenInterrupt as e:
#     print(mc.coords.press.x)
#     print(mc.coords.press.y)
#     print(mc.coords.release.x)
#     print(mc.coords.release.y)
#     print(e.args[0])

from pymouse import PyMouseEvent

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

class MouseCoords:
    def __init__(self):
        self.press = Point()
        self.release = Point()

class ListenInterrupt(Exception):
    pass

class MouseCapture(PyMouseEvent):
    def __init__(self):
        PyMouseEvent.__init__(self)
        self.coords = MouseCoords()

    def click(self, x, y, button, press):
        if button == 1: # Left click
            if press:
                self.coords.press.x = x
                self.coords.press.y = y
            else:
                self.coords.release.x = x
                self.coords.release.y = y
                #self.stop()
                raise ListenInterrupt("Grabbed!")
