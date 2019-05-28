from pyo import *
s = Server().boot()
s.amp = 1

sf = SfPlayer("campersongs/primarycolors.wav").out()

sm = SmoothDelay(sf).out()

sm.ctrl()

s.gui(locals())

s.start()
