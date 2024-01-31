from styles import *

import tkinter as tk
from tkinter import scrolledtext, ttk
import datetime
import os


def send_message():
    user_input = user_input_box.get()
    if user_input:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"{YOUR_NAME}: " + user_input + "\n", f"{YOUR_NAME}")

        # Symulowana odpowiedź
        simulated_response = "Otrzymałem: " + user_input  # Tutaj można dodać bardziej zaawansowaną logikę
        chat_history.insert(tk.END, f"{CHAT_NAME}: " + simulated_response + "\n", f"{CHAT_NAME}")

        chat_history.config(state=tk.DISABLED)
        chat_history.see(tk.END)
        user_input_box.delete(0, tk.END)


def reset_chat():
    chat_history.config(state=tk.NORMAL)
    chat_history.delete(1.0, tk.END)
    chat_history.config(state=tk.DISABLED)


app = tk.Tk()
app.title(APP_TITLE)
app.configure(bg=BG_COLOR)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height-80}")

# Główny kontener
main_frame = tk.Frame(app, bg=BG_COLOR)
main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Panel boczny
sidebar = tk.Frame(app, width=200, bg=SIDEBAR_COLOR)
sidebar.pack(side=tk.RIGHT, fill=tk.Y)

# Przyciski na panelu bocznym
first_button = tk.Button(sidebar, text="Model 1", command=reset_chat, bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
first_button.pack(pady=10, padx=10, fill=tk.X)

second_button = tk.Button(sidebar, text="Model 2", command=reset_chat, bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
second_button.pack(pady=10, padx=10, fill=tk.X)

third_button = tk.Button(sidebar, text="Model 3", command=reset_chat, bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
third_button.pack(pady=10, padx=10, fill=tk.X)

# Separator
separator = ttk.Separator(sidebar, orient='horizontal')
separator.pack(pady=5, padx=10, fill=tk.X)

# Generowanie przycisków czatów
# create_chat_buttons()

# Treść czatu
chat_frame = tk.Frame(main_frame, bg=BG_COLOR)
chat_frame.pack(expand=True, fill=tk.BOTH)

chat_history = scrolledtext.ScrolledText(chat_frame, state=tk.DISABLED, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
chat_history.pack(expand=True, fill=tk.BOTH)
chat_history.tag_config(YOUR_NAME, foreground=YOUR_TEXT_COLOR, font=DIALOGUE_FONT)
chat_history.tag_config(CHAT_NAME, foreground=CHAT_TEXT_COLOR, font=DIALOGUE_FONT)

# Pole wprowadzania
input_frame = tk.Frame(main_frame, bg=BG_COLOR)
input_frame.pack(fill=tk.X)

user_input_box = tk.Entry(input_frame, bg=BG_COLOR, fg=TEXT_COLOR, font=USER_INPUT_FONT)
user_input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)
user_input_box.focus_set()

send_button = tk.Button(input_frame, text="Send", command=send_message, bg=BG_COLOR, font=DIALOGUE_FONT, fg=TEXT_COLOR)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

app.mainloop()
