class Game(object):
    from formalize import Formalize
    from style     import Styles

class WF(object):
    def __init__(self): self.run()
    def run     (self):
        while True:
            option = self.menu()
            
            if option == 0:
                self.game()
            elif option == 1:
                pass
            elif option == 2:
                break

    def game(self):
        buttons = [
            "Fight",
            "Workshop",
            "Back",
        ]; state = 0

        while True:
            Game.Formalize.clrscr()

            Game.Formalize.rectangle((0, 0), 31, 7)

            Game.Formalize.putxy((13, 2), "WF")

            for i in range(len(buttons)):
                Game.Formalize.putxy((3, 3 + i), f"{f'> {Game.Styles.Colors.GruvBox.FGRed}' if state == i else ''}{buttons[i]}{Game.Styles.Style.Reset}")

            key = Game.Formalize.get()

            if key == "e": return state

            state = Game.Formalize.changeState(key, state, buttons)

    def menu(self):
        buttons = [
            "Play",
            "Settings",
            "Exit",
        ]; state = 0

        while True:
            Game.Formalize.clrscr()

            Game.Formalize.rectangle((0, 0), 31, 7)

            Game.Formalize.putxy((11, 2), "Main Menu")

            for i in range(len(buttons)):
                Game.Formalize.putxy((3, 3 + i), f"{f'> {Game.Styles.Colors.GruvBox.FGRed}' if state == i else ''}{buttons[i]}{Game.Styles.Style.Reset}")

            key = Game.Formalize.get()

            if key == "e": return state

            state = Game.Formalize.changeState(key, state, buttons)
        
if __name__ == '__main__' : WF() ; exit(0)
