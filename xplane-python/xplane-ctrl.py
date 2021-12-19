import xpc

# using plugin from:
# https://github.com/nasa/XPlaneConnect

with xpc.XPlaneConnect() as client:
    # Get the current position info for the player aircraft
    posi = client.getPOSI(0)

    while True:
        try:
            # http://www.xsquawkbox.net/xpsdk/docs/DataRefs.html
            drefs = ["sim/flightmodel/position/indicated_airspeed", "sim/flightmodel/position/magnetic_variation"]
            ias,hdr = client.getDREFs(drefs)

            throttle = "sim/flightmodel/engine/ENGN_thro_override"
            if ias[0] < 200:
                val = 1.0
            else:
                val = 0.0
            client.sendDREF(throttle, val)
        
            print(ias, val)
        except:
            pass
