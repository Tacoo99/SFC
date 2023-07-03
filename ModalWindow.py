import customtkinter
from tkcalendar import Calendar


class ModalWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x360")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=2)
        self.home_frame.grid(row=0, column=1, sticky="nsew")

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="SFC - Simple File Creator",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10)
        
        
        self.cal = Calendar(self.home_frame, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2018, month=2, day=5)
        
        self.cal.grid(row=1, column=0, sticky="nsew")
        
        self.date = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Chosen date")
        self.date.grid(row=2, column=0, pady=(15, 15), ipady=5)
        