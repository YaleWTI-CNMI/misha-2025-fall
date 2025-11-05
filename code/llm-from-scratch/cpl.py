import signal

SIGTERM = 15

class CPL:

    def __init__(self, sig=SIGTERM):
        self._preempted = False
        self._sig = sig
        signal.signal(self._sig, self._signal_handler)

    def _signal_handler(self, sig, frame):
        self._preempted = True

    def _cpl_handler(self):
        return

    def check(self, handle=_cpl_handler):
        return self._preempted
        

