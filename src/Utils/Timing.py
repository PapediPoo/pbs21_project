import time

from numpy import floor

ct = 0

def delta_time():
    global ct
    nt = time.time()
    dt = nt - ct
    ct = nt
    return dt