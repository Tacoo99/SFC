import tkinter
import customtkinter
from tkcalendar import Calendar


class ModalWindow(customtkinter.CTkToplevel):
    def __init__(self, *args, callback=None, source =None, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.callback = callback 
        self.calendarSource = source
        
        self.title("Date chooser")
        self.geometry("310x400")
        self.resizable(False, False)
        self.iconbitmap("images/icon/icon.ico")
        
        self.transient(self.master)
        self.update_idletasks()
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_width()) // 2
        y = (screen_height - self.winfo_height()) // 2
        self.geometry(f"+{x}+{y}")
        self.lift()
        self.focus_force()
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        self.home_frame.grid(row=0, column=1, sticky="nsew")

        self.banner_text = customtkinter.CTkLabel(self.home_frame, text="Choose date",
                                                  font=customtkinter.CTkFont(size=18, weight="bold"))
        self.banner_text.grid(row=0, column=0, sticky="nsew", ipady=10)
        
        
        self.cal = Calendar(self.home_frame, font="Arial 12", selectmode='day', locale='en_US',
                   cursor="hand2", year=2023, month=7, day=3)
        
        self.cal.bind("<<CalendarSelected>>", lambda event: self.getSelection(event, source="calendar"))
        
        self.cal.grid(row=1, column=0)
        
        self.date_entry = customtkinter.CTkEntry(self.home_frame, width=200, placeholder_text="Chosen date")
        self.date_entry.grid(row=2, column=0, pady=(15, 15), ipady=5)
        
        self.confirm_button= customtkinter.CTkButton(self.home_frame, text="Confirm", command=lambda: self.getSelection(None, source="button"))
        self.confirm_button.grid(row=3, column=0, pady=(15, 15), ipady=5)
        
    def getSelection(self, event, source):
        selected_date = self.cal.selection_get()
        if source == "calendar":
            self.date_entry.delete(0, 'end')
            self.date_entry.insert(0, selected_date)
        elif source == "button":
            if self.date_entry.get() == '':
                tkinter.messagebox.showerror(title='Error', message='Please choose a date!')
            else:
                if self.callback:
                    self.callback(selected_date, self.calendarSource)
                self.destroy()
        
        