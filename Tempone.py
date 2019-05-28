from pyo import *

s = Server().boot()
sf = SfPlayer("mistergood.wav")
#fs = FreqShift(sf).out()
#hr = Harmonizer(sf).out()
ch = Chorus(sf, depth=0, feedback=0).out()
#dly = Delay(sf).out()

ch.ctrl()

s.gui(locals())

s.start()

        #ch_diff = str(mod_temp - 1)
        #ch.depth = mod_temp - int(ch_diff)
        #print(f"set depth to {ch.depth}")

        # Harmonizer
        # hr_diff = POSITIVE -> NEGATIVE?
        # hr.transpo = 
        #print(f"set transpo to {hr.transpo}")
        # default -7

        # Delay
        #dly_diff = str(mod_temp - 0.25)
        #dly.delay = mod_temp - int(dly_diff)
        #print(f"set delay to {dly.delay}")

        # FreqShift
        #mod_temp_sh = mod_temp * 1000
        #sh_diff = str(mod_temp_sh - 100)
        #sh.setShift(mod_temp_sh - int(sh_diff))
        #print(f"set shift to {sh.shift}")

        #speed_diff = str(mod_temp - 1)
        #sf.setSpeed(mod_temp - int(speed_diff))
        #print(f"set speed to {sf.speed}")
        # defaults to 1

