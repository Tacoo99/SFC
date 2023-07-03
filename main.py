import customtkinter
import os
from PIL import Image
from tkinter import filedialog as fd



from ModalWindow import ModalWindow

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.toplevel_window = None

        self.title("SFC")
        self.geometry("400x300")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        # self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "banner-logo.png")), size=(110, 51))
        
        self.file_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "file_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "file_light.png")), size=(20, 20))
        
        self.date_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "date_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "date_light.png")), size=(20, 20))

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=2)

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="SFC - Simple File Creator",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10)
        self.description_text = customtkinter.CTkLabel(self.home_frame, text="Simple tool for bulk creating files with date chooser",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text.grid(row=1, column=0, padx=35, sticky="n")

        #file chooser
        self.filename_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Filename")
        self.filename_entry.grid(row=2, column=0, pady=(15, 15), ipady=5)
        
        self.button_fileChooser = customtkinter.CTkButton(self.home_frame, text="Choose file", command=self.select_file, image=self.file_image, compound="right")
        self.button_fileChooser.grid(row=3, column=0, ipady=5)
        
        
        self.password_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Date")
        self.password_entry.grid(row=4, column=0, padx=30, pady=(15, 15), ipady=5)
        
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Choose date", command=self.open_toplevel, image=self.date_image, compound="right")
        self.home_frame_button_2.grid(row=5, column=0, ipady=5)

        self.home_frame.grid(row=0, column=1, sticky="nsew")
        
        
    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ModalWindow(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it
    
    def select_file(self):
        filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )

        filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)

        self.filename_entry.insert(0, filename)
    


if __name__ == "__main__":
    app = App()
    app.mainloop()
