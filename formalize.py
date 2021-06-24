class Formalize (object):

    @staticmethod
    def gotoxy(x, y):
        print("%c[%d;%df" % (0x1B, y, x), end = "")
    
    @staticmethod
    def putxy(x, y, string):
        Formalize.gotoxy(x, y); print(string)
    
    @staticmethod
    def get(): from msvcrt import getwch as get; return get()

    @staticmethod
    def clr(): from os import system as cmd; cmd("cls")

    @staticmethod
    def line(p, q, char):
        x1, y1 = p
        x2, y2 = q

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            if y2 < y1: y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                Formalize.putxy(x1, y, char)

        else:
            m      = dy / dx
            adjust = 1 if m >= 0 else -1
            offset = 0

            if m <= 1 and m >= -1:
                delta              = abs(dy) * 2
                threshold          = abs(dx)
                thresholdIncrement = abs(dx) * 2

                y = y1
                
                if x2 < x1: x1, x2 = x2, x1 ; y = y2

                for x in range(x1, x2 + 1):
                    Formalize.putxy(x, y, char)

                    offset += delta
                    if offset >= threshold:
                        y         += adjust
                        threshold += thresholdIncrement

            else:
                delta              = abs(dx) * 2
                threshold          = abs(dy)
                thresholdIncrement = abs(dy) * 2

                x = x1

                if y2 < y1: y1, y2 = y2, y1 ; x = x2

                for y in range(y1, y2 + 1):
                    Formalize.putxy(x, y, char)

                    offset += delta
                    if offset >= threshold:
                        x         += adjust
                        threshold += thresholdIncrement
