# Python3
# 15-3-21

# Documentation
# Here it goes:

from tkinter import *
import configparser


class menu:
    def __init__(self, root):
        self.config = configparser.ConfigParser()
        self.config.read('menu_config.ini')
        # To show all sections of config file.
        # print(self.config.sections())

        self.root = root
        self.root.title(f"{self.config['DEFAULT']['Title']}")
        self.root.attributes('-fullscreen', self.config['Settings']['Fullscreen'])
        self.root.geometry('800x700+550+170')
        self.root.configure(bg=f"#{self.config['DEFAULT']['Bg Color']}")


if __name__ == '__main__':
    master = Tk()
    start = menu(master)
    master.mainloop()
