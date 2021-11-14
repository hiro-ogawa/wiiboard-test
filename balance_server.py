import argparse
from concurrent.futures import ThreadPoolExecutor

from pythonosc import dispatcher
from pythonosc import osc_server
from processing_py import *

app = App(600, 600) # create window: width, height
executor = ThreadPoolExecutor()

px = 300
py = 300
r = 0

def draw_thread():
    while True:
        app.background(0,0,0) # set background:  red, green, blue
        app.fill(255,255,0) # set color for objects: red, green, blue
        app.ellipse(px, py, r, r) # draw a circle: center_x, center_y, size_x, size_y
        app.redraw() # refresh the window

def balance_cb(unused_addr, args, *values):
    # print("value size: ", len(values))
    # for el in values:
    #     print(el)

    global px, py, r
    px = 600 * values[4]
    py = 600 * (1.0 - values[5])
    r = 50 * values[3]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=8001, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = dispatcher.Dispatcher()
    dispatcher.map("/wii/*/balance", balance_cb)

    executor.submit(draw_thread)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()
