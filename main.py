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
        
<<<<<<< HEAD
        self.file_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "file_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "file_light.png")), size=(20, 20))
=======
        self.first_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "first_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "first_light.png")), size=(25, 25))
        self.second_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "second_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "second_light.png")), size=(25, 25))
        self.third_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "third_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "third_light.png")), size=(25, 25))

        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew" )
        self.navigation_frame.grid_rowconfigure(3, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="", image=self.logo_image)
        self.navigation_frame_label.grid(row=0, column=0, padx=0, pady=25, sticky="nsew")

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Add account",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   image=self.add_user_image, anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Info/FAQ",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      image=self.info_image, anchor="w", command=self.frame_2_button_event)
        self.frame_2_button.grid(row=2, column=0, sticky="ew")
>>>>>>> 6b207a8d48361ace57a1eaef93cfa13c70686da2
        
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
        
        
<<<<<<< HEAD
        self.password_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Date")
        self.password_entry.grid(row=4, column=0, padx=30, pady=(15, 15), ipady=5)
        
        self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="Choose date", command=self.open_toplevel, image=self.date_image, compound="right")
        self.home_frame_button_2.grid(row=5, column=0, ipady=5)

        self.home_frame.grid(row=0, column=1, sticky="nsew")
        
=======
        self.banner_text2 = customtkinter.CTkLabel(self.help_frame, text="Frequently asked questions",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text2.grid(row=0, column=0, padx=20, pady=0, sticky="nsew", ipady=10)
        self.description_text2 = customtkinter.CTkLabel(self.help_frame, text="Find answers to commonsly asked questions about this program",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text2.grid(row=1, column=0, padx=20, sticky="n")
        
        #first question
        self.first_title = customtkinter.CTkLabel(self.help_frame, text="What is this program for?", image=self.first_image, compound="left")
        self.first_title.grid(row=2, column=0, ipadx=50, pady=25, sticky="wn")
        
        self.first_description = customtkinter.CTkLabel(self.help_frame, text="It allows you to log in to your domain account \nwhen you receive new computer")
        self.first_description.grid(row=3, column=0, sticky="n")
        
        #second question
        self.second_title = customtkinter.CTkLabel(self.help_frame, text="Who to contact in case of problem?", image=self.second_image, compound="left")
        self.second_title.grid(row=4, column=0, ipadx=50, pady=25, sticky="wn")
        
        self.second_description = customtkinter.CTkLabel(self.help_frame, text="E-mail: wojciech.koziol@fujitsu.com\nE-mail: servicedesk@mpl.mee.com\nTelephone: +48 22 104 32 61")
        self.second_description.grid(row=5, column=0, sticky="n")
        
        #third question
        self.third_title = customtkinter.CTkLabel(self.help_frame, text="Who is the author of the program?", image=self.third_image, compound="left")
        self.third_title.grid(row=6, column=0, ipadx=50, pady=25, sticky="wn")
        
        self.third_description = customtkinter.CTkLabel(self.help_frame, text="Wojciech Kozioł, Fujitsu")
        self.third_description.grid(row=7, column=0, sticky="n")
        
        self.third_description = customtkinter.CTkLabel(self.help_frame, text="CUF ©2023 Fujitsu. All Rights Reserved",
                                                        font=customtkinter.CTkFont(size=9))
        self.third_description.grid(row=8, column=0, pady=15,padx=5, sticky="se")
        

        # select default frame
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()
        if name == "frame_2":
            self.help_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.help_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")

    def frame_2_button_event(self):
        self.select_frame_by_name("frame_2")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
>>>>>>> 6b207a8d48361ace57a1eaef93cfa13c70686da2
        
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
