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
    def DDAline(p, q, char):
        '''@deprecated'''
        x1, y1 = p
        x2, y2 = q
        
        dx = x2 - x1
        dy = y2 - y1
        
        s = max(abs(dx), abs(dy))

        xi = dx / s
        yi = dy / s

        for _ in range(s):
            Formalize.putxy(round(x1), round(y1), char)
            x1 += xi
            y1 += yi

    def line(p, q, char):
        x1, y1 = p
        x2, y2 = q

        x = x1
        y = y1

        dx = x2 - x1
        dy = y2 - y1

        p = 2 * dy - dx

        pl = 2 * dy
        pg = 2 * dy - 2 * dx

        for x in range(x, x2 + 1):
            Formalize.putxy(x, y, char)

            if p < 0: p += pl
            else    : p += pg ; y += 1
