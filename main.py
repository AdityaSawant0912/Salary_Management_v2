# Python3
# 14-3-21

# Documentation
# Here it goes:

from tkinter import *
import configparser


class salary:
    def __init__(self, root):
        self.config = configparser.ConfigParser()
        self.config.read('main_config.ini')
        # To show all sections of config file.
        # print(self.config.sections())

        self.root = root
        self.root.title(f"{self.config['DEFAULT']['Title']}")
        self.root.attributes('-fullscreen', self.config['Settings']['Fullscreen'])
        self.root.geometry('1350x700+300+200')


if __name__ == "__main__":
    master = Tk()
    main = salary(master)
    master.mainloop()
