#!/usr/bin/python3

import mousecapture as Capture
import pyperclip as Clip
import screengrabber as Grabber
import textrecognizer as Reco

if __name__ == "__main__":
    mc = Capture.MouseCapture()

    try:
        mc.run()
    except Capture.ListenInterrupt as e:
        print("Processing...", end = " ", flush = True)
    
    # Grab part of the screen
    img = Grabber.grab(mc.coords.press.x,
                       mc.coords.press.y, 
                       mc.coords.release.x, 
                       mc.coords.release.y)

	# Recognize text in img
    text = Reco.recognize(img)

    # Copy text to clipboard
    Clip.copy(text)

    print("Done!")
    print(text)
