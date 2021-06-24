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
        """
        slope:
            y = mx + b

            m = tanθ 
              | ∆y/∆x

            b = y - (∆y/∆x)x

        Bresenham's:
            y = mx + C
            y = m(xₖ + 1) + C

            d₁ = y - yₖ = m(xₖ + 1) + C - yₖ

            d₂ = yₖ + 1 - y = yₖ + 1 - m(xₖ + 1) - C

            '''
            yₖ+1 [ ] [ ]
                     /| d₂
                    • •
                   /  | d₁
            yₖ   [×] [ ]
                 xₖ  xₖ+1
            '''

            xₙ = xₖ + 1
            yₙ = (d₁ - d₂) < 0 ? yₖ : yₖ+1

            d₁ - d₂ = [m(xₖ + 1) + C - yₖ] - [yₖ + 1 - m(xₖ + 1) - C]

            d₁ - d₂ = m(xₖ + 1) + C - yₖ - yₖ - 1 + m(xₖ + 1) + C

            d₁ - d₂ = 2m(xₖ + 1) - 2yₖ + 2C - 1

            ∆x(d₁ - d₂) = ∆x[2(∆y/∆x)(xₖ + 1) - 2yₖ + 2C - 1]

            ∆x(d₁ - d₂) = 2∆y(xₖ + 1) - 2∆xyₖ + 2∆xC - ∆x

            pₖ = ∆x(d₁ - d₂) = 2∆yxₖ - 2∆xyₖ + 2∆y + 2∆xC - ∆x

            pₖ = ∆x(d₁ - d₂) = 2∆yxₖ - 2∆xyₖ + (2∆y + 2∆xC - ∆x)/x

            pₖ = ∆x(d₁ - d₂) = 2∆yxₖ - 2∆xyₖ

            pₙ = ∆x(d₁ - d₂) = 2∆yxₙ - 2∆xyₙ

            pₙ - pₖ = [2∆yxₙ - 2∆xyₙ] - [2∆yxₖ - 2∆xyₖ]

            pₙ - pₖ = 2∆yxₙ - 2∆xyₙ - 2∆yxₖ + 2∆xyₖ

            pₙ - pₖ = 2∆y(xₙ - xₖ) - 2∆x(yₙ - yₖ)

            pₙ - pₖ < 0
            → pₙ = pₖ + 2∆y(xₖ + 1 - xₖ) - 2∆x(yₖ - yₖ)
            ⟹ pₙ = pₖ + 2∆y

            pₙ - pₖ ≥ 0
            → pₙ = pₖ + 2∆y(xₖ + 1 - xₖ) - 2∆x(yₖ + 1 - yₖ)
            ⟹ pₙ = pₖ + 2∆y - 2∆x

            P₁ = 2∆yx₁ - 2∆xy₁ + 2∆y + 2∆xC - ∆x

            P₁ = 2∆yx₁ - 2∆xy₁ + 2∆y + 2∆x[y₁ - (∆y/∆x)x₁] - ∆x

            P₁ = 2∆yx₁ - 2∆xy₁ + 2∆y + 2∆xy₁ - 2∆yx₁ - ∆x

            P₁ = 2∆y - ∆x
        """
        
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
