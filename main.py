import tkinter
import customtkinter
import os
from PIL import Image
from tkinter import filedialog as fd
from pygame import mixer
from datetime import datetime, timedelta
import shutil


from ModalWindow import ModalWindow

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.toplevel_window = None

        self.title("SFC")
        self.geometry("400x690")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
        

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        music_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "music")
        mixer.init()
        mixer.music.load(os.path.join(music_path, "metinek.mp3"))
        mixer.music.play(-1)
        
        self.fullPath = ''
        self.check_var = customtkinter.StringVar(value="file")
        

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
        
        
        self.file_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "file_light.png")), size=(20, 20))
        self.date_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "date_light.png")), size=(20, 20))
        self.folder_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "folder_light.png")), size=(20, 20))
        self.generate_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "generate_light.png")), size=(20, 20))
        self.speaker_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "speaker_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "speaker_light.png")), size=(20, 20))
        self.mute_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "mute_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "mute_light.png")), size=(20, 20))
        

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=2)

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="SFC - Simple File Creator",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10)
        self.description_text = customtkinter.CTkLabel(self.home_frame, text="Simple tool for bulk creating files with date chooser",
                                                  font=customtkinter.CTkFont(size=14))
        self.description_text.grid(row=1, column=0, padx=35, sticky="n")

         #file or directory checkbox
        self.fileOrDir_checkbox = customtkinter.CTkCheckBox(self.home_frame, text=f'Chosen: file', command=self.get_file_or_dir,
                                     variable=self.check_var, onvalue="file", offvalue="directory")
        self.fileOrDir_checkbox.grid(row=4, column=0, padx=35, pady=10, sticky="n")
        
        #file chooser
        self.filename_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Filename")
        self.filename_entry.grid(row=2, column=0, pady=(15, 15), ipady=5)
        
        
         #file or directory chooser button
        self.button_fileChooser = customtkinter.CTkButton(self.home_frame, text="Choose file", command=self.select_file, image=self.file_image, compound="right")
        self.button_fileChooser.grid(row=3, column=0, ipady=5)
        
        
        #directory chooser
        self.directory_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Directory")
        self.directory_entry.grid(row=5, column=0, pady=(15, 15), ipady=5)
        
        self.button_directoryChooser = customtkinter.CTkButton(self.home_frame, text="Choose destination", command=self.select_directory, image=self.folder_image, compound="right")
        self.button_directoryChooser.grid(row=6, column=0, ipady=5)
        
        
         #starting date
        self.startingDate_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Starting date")
        self.startingDate_entry.grid(row=7, column=0, padx=30, pady=(15, 15), ipady=5)
        
        self.startingDate_button = customtkinter.CTkButton(self.home_frame, text="Choose date", command=self.starting_date, image=self.date_image, compound="right")
        self.startingDate_button.grid(row=8, column=0, ipady=5)

         #ending date
        self.endingDate_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Ending date")
        self.endingDate_entry.grid(row=9, column=0, padx=30, pady=(15, 15), ipady=5)
        
        self.endingDate_button= customtkinter.CTkButton(self.home_frame, text="Choose date", command=self.ending_date, image=self.date_image, compound="right")
        self.endingDate_button.grid(row=10, column=0, ipady=5)
        
         #generateFiles button
        self.generateFiles_button= customtkinter.CTkButton(self.home_frame, text="Generate files", command=self.generate_files, image=self.generate_image, compound="right")
        self.generateFiles_button.grid(row=11, column=0, padx=30, pady=(30, 15), ipady=5, sticky='nsew')
        
        self.speaker_button = customtkinter.CTkButton(self.home_frame, text="", width=200, image=self.speaker_image, fg_color='transparent', hover=False, compound="left", command=self.play_music)
        self.speaker_button.grid(row=12, column=0, padx=0, sticky="w")
        
        self.slider_1 = customtkinter.CTkSlider(self.home_frame, from_=0.0, to=1.0, command=self.slider_event)
        self.slider_1.grid(row=13, column=0, sticky="w")
    
        self.home_frame.grid(row=0, column=1)
        
    def set_full_path(self, path):
        self.fullPath = path
    
    def get_full_path(self):
        return self.fullPath
    
    def get_file_or_dir(self):
        fileOrDir = self.check_var.get()
        self.fileOrDir_checkbox.configure(text=f'Chosen: {fileOrDir}')
        
        if fileOrDir == 'directory':
            self.button_fileChooser.configure(image=self.folder_image)
            self.filename_entry.configure(placeholder_text="Directory")
            self.button_fileChooser.configure(text="Choose folder")
        if fileOrDir == 'file':
            self.button_fileChooser.configure(image=self.file_image)
            self.filename_entry.configure(placeholder_text="Filename")
            self.button_fileChooser.configure(text="Choose file")
        
        
    def slider_event(self, value):
        mixer.music.set_volume(value)
        
    def play_music(self):
        if mixer.music.get_volume() == 0.0:
            mixer.music.set_volume(1.0)
            self.speaker_button.configure(image=self.speaker_image)
           
        else:
            mixer.music.set_volume(0.0)
            self.speaker_button.configure(image=self.mute_image)
            
    def duplicate_file_or_directory_with_dates(self,filename, directory, date_from, date_to):
        num_copies = 0
        date_format = "%Y-%m-%d"
        date_start = datetime.strptime(date_from, date_format).date()
        date_end = datetime.strptime(date_to, date_format).date()

        delta = date_end - date_start
        num_days = delta.days

        for i in range(num_days + 1):
            current_date = date_start + timedelta(days=i)
            date_str = current_date.strftime(date_format)
            source_path = filename
            destination_path = os.path.join(directory, f"{date_str}_{os.path.basename(filename)}")

            if os.path.isdir(filename):
                shutil.copytree(source_path, destination_path)
                num_copies += 1
            elif os.path.isfile(filename):
                shutil.copy2(source_path, destination_path)
                num_copies += 1
            else:
                tkinter.messagebox.showerror(title='Error', message='Wrong file or directory, choose another one!')
        tkinter.messagebox.showinfo(title='Success', message=f"Copied {num_copies} of files or directories")
        
    def generate_files(self):
        
        if self.filename_entry.get() != '' and self.directory_entry.get() != '' and self.startingDate_entry.get() != '' and self.endingDate_entry.get() != '':
            self.duplicate_file_or_directory_with_dates(self.get_full_path(), self.directory_entry.get(), self.startingDate_entry.get(), self.endingDate_entry.get())
        else:
            tkinter.messagebox.showerror("Error!", "Please fill in all fields!")
        
    def starting_date(self):
        source = 'start'
        self.open_toplevel(source)
        
    def ending_date(self):
        source = 'end'
        self.open_toplevel(source)
        
        
    def open_toplevel(self, buttonSource):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = ModalWindow(self, callback=self.handleSelectedDate, source = buttonSource  )
        else:
            self.toplevel_window.focus()
    
    def select_directory(self):
        filename = fd.askdirectory(
        title='Select directory',
        )
        
        self.directory_entry.delete(0, 'end')
        self.directory_entry.insert(0, filename)
        
    def select_file(self):
        filetypes = (
        ('Excel files', '*.xlsx'),
        ('All files', '*.*')
    )

        filename = fd.askopenfilename(
        title='Open a file',
        initialdir='/',
        filetypes=filetypes)
        self.set_full_path(filename)
        basename = os.path.basename(filename)
        
        self.filename_entry.delete(0, 'end')
        self.filename_entry.insert(0, basename)
    
    def handleSelectedDate(self, selected_date, source):
        
        if source == 'start':
            self.startingDate_entry.delete(0, 'end')
            self.startingDate_entry.insert(0, selected_date)
            
        elif source == 'end':
            self.endingDate_entry.delete(0, 'end')
            self.endingDate_entry.insert(0, selected_date)
        else:
            tkinter.messagebox.showerror(title='Error', message='You have chosen wrong date!')
        


if __name__ == "__main__":
    app = App()
    app.mainloop()
