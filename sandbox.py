import tkinter as tk
from tkinter import ttk


def popup_message(title_text, message_text, confirmation_button_text):
    normal_font = ('Helvetica', 16)
    popup = tk.Tk()
    popup.attributes("-topmost", True)
    popup.wm_title(title_text)
    label = ttk.Label(popup, text=message_text, font=normal_font)
    label.pack(side="top", fill="both", padx=60, pady=60)
    B1 = ttk.Button(popup, text=confirmation_button_text, command=popup.destroy, padding=10)
    B1.pack(side="bottom", pady=20)
    popup.mainloop()


popup_message('Manual step',
              'Connect BNC adapter cable to Triton head',
              'Cable connected')
