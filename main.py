from styles import *
import tkinter as tk
from tkinter import scrolledtext, ttk

def send_message(event=None):
    user_input = user_input_box.get("1.0", tk.END).strip()
    if user_input:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"{YOUR_NAME}: " + user_input + "\n", f"{YOUR_NAME}")

        # Symulowana odpowiedź
        simulated_response = "Otrzymałem: " + user_input
        chat_history.insert(tk.END, f"{CHAT_NAME}: " + simulated_response + "\n", f"{CHAT_NAME}")

        chat_history.config(state=tk.DISABLED)
        chat_history.see(tk.END)
        user_input_box.delete("1.0", tk.END)

def reset_chat():
    chat_history.config(state=tk.NORMAL)
    chat_history.delete(1.0, tk.END)
    chat_history.config(state=tk.DISABLED)

app = tk.Tk()

icon_path = 'icon/szop2.ico'
app.iconbitmap(default=icon_path)

app.title(APP_TITLE)
app.configure(bg=BG_COLOR)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

app_width = 900
app_height = 800 - 90

x_position = (screen_width - app_width) // 2
y_position = (screen_height - app_height) // 2

app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")

# Panel boczny
sidebar = tk.Frame(app, width=200, bg=SIDEBAR_COLOR)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

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

# Główny kontener
main_frame = tk.Frame(app, bg=BG_COLOR)
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

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

user_input_box = tk.Text(input_frame, height=1.3, width=40, wrap="word", bg=BG_COLOR, fg=TEXT_COLOR, font=USER_INPUT_FONT)
user_input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=10, pady=10)

# Dodanie zdarzenia dla klawisza Enter
user_input_box.bind("<Return>", send_message)

send_button = tk.Button(input_frame, text="Send", command=send_message, bg=BG_COLOR, font=DIALOGUE_FONT, fg=TEXT_COLOR)
send_button.pack(side=tk.RIGHT, padx=10, pady=10)

app.mainloop()
