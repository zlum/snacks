import pyscreenshot as ImageGrab

def grab(x1, y1, x2, y2):
    # Check coords
    if(x1 > x2):
        x1, x2 = x2, x1

    if(y1 > y2):
        y1, y2 = y2, y1

    # Grab part of the screen
    return ImageGrab.grab(bbox = (x1, y1, x2, y2))