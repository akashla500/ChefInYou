from tkinter import Tk
from platform import system


def main():
    # PySyntax box configurations
    chef_in_you_window = Tk()
    chef_in_you_window.title("Chef In You")
    chef_in_you_window.geometry("1200x600+130+100")
    chef_in_you_window.resizable(False, False)

    # ICON not showing good
    # if system() == "Darwin":
    #    logo_image_name = 'images/logo.icns'
    # elif system() == "Windows":
    #    logo_image_name = 'images/logo.ico'
    # else:
    #    logo_image_name = 'images/logo.xbm'

    # chef_in_you_window.iconbitmap(logo_image_name)

    chef_in_you_window.mainloop()


if __name__ == "__main__":
    main()
