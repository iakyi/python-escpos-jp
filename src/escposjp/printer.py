from escpos.printer import Network, Usb, Serial, Dummy, File
import inspect
import sys


def JpInit(self):
    self.charcode("CP932")
    self._raw(b'\x1c\x43\x01')


def JpText(self, txt, dw=False, dh=False):
    self._raw(b'\x1c\x26')    # Kanji mode ON
    n = 0x00
    if (dw):
        n += 0x04
    if (dh):
        n += 0x08
    if (n != 0x00):
        # Char size ON
        self._raw(b'\x1c\x21' + n.to_bytes(1, byteorder='big'))
    self._raw(txt.encode('shift-jis', 'ignore'))
    if (n != 0x00):
        self._raw(b'\x1c\x21\x00')  # Char size OFF
    self._raw(b'\x1c\x2e')    # Kanji mode OFF


def addfunc(Klass, func):
    setattr(Klass, func.__name__, func)


for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
    addfunc(obj, JpInit)
    addfunc(obj, JpText)
