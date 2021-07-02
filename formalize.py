class Formalize (object):

    @staticmethod
    def gotoxy(x, y): print("%c[%d;%df" % (0x1B, y, x), end = "")
    
    @staticmethod
    def putxy(at, string): Formalize.gotoxy(at[0], at[1]); print(string)
    
    @staticmethod
    def get(): from msvcrt import getwch as get; return get()

    @staticmethod
    def clrscr(): from os import system as cmd; cmd("cls")

    @staticmethod
    def line(p, q, char):
        x1, y1 = p
        x2, y2 = q

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0:
            if y2 < y1: y1, y2 = y2, y1

            for y in range(y1, y2 + 1):
                Formalize.putxy((x1, y), char)

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
                    Formalize.putxy((x, y), char)

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
                    Formalize.putxy((x, y), char)

                    offset += delta
                    if offset >= threshold:
                        x         += adjust
                        threshold += thresholdIncrement

    @staticmethod
    def rectangle(at, width, height, leftWall = "#", upWall = "#", downWall = "#", rightWall = "#"):
        XOffset, YOffset = at
        
        Formalize.line(
            (XOffset, YOffset),
            (XOffset + width, YOffset),
            upWall
        )

        Formalize.line(
            (XOffset, YOffset),
            (XOffset, YOffset + height),
            leftWall
        )

        Formalize.line(
            (XOffset, YOffset + height),
            (XOffset + width, YOffset + height),
            downWall
        )

        Formalize.line(
            (XOffset + width, YOffset),
            (XOffset + width, YOffset + height),
            rightWall
        )

    @staticmethod
    def renderBar(at, maxValue, currentValue, length, leftWall = "[", rightWall = "]", fill = "@", dead = " "):
        point       = maxValue // length
        points      = currentValue // point
        deltaPoints = length - currentValue // point

        Formalize.putxy(at, f'{leftWall}{fill * points}{dead * deltaPoints}{rightWall}')

    @staticmethod
    def changeState(key, state, options):
        TLength = len(options) - 1

        return (state - 1) * (state > 0       and key == "w") + \
               (state + 1) * (state < TLength and key == "s") + \
               (TLength)   * (state == 0      and key == "w")
