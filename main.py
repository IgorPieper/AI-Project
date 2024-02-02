from styles import *

import tkinter as tk
from tkinter import scrolledtext, ttk
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
from transformers import pipeline
from gtts import gTTS
import os

# Konfiguracja Translatora
model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

tokenizer.src_lang = "pl_PL"

# Konfiguracja Emocji
classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)


selected_model = 0
icon_path = "icon/szop.ico"


def send_message():
    user_input = user_input_box.get()
    if user_input:
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"{YOUR_NAME}: " + user_input + "\n", YOUR_NAME)
        chat_history.config(state=tk.DISABLED)

        encoded_pl = tokenizer(user_input, return_tensors="pt")
        generated_tokens = model.generate(
            **encoded_pl,
            forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
        )
        simulated_response1 = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

        response_str = ' '.join(simulated_response1)  # Join list elements into a single string
        chat_history.config(state=tk.NORMAL)
        chat_history.insert(tk.END, f"{CHAT_NAME}: " + response_str + "\n", CHAT_NAME)

        if selected_model == 1:
            output = gTTS(text=response_str, lang="en", slow=False)
            output.save("output.mp3")

        if selected_model == 2:
            sentences = [response_str]
            simulated_response = classifier(sentences)
            chat_history.insert(tk.END, f"Emotions: ", CHAT_NAME)

            for emotion in (simulated_response[0]):
                if emotion['score'] > 0.1:
                    chat_history.insert(tk.END, f"{emotion['label']}, ", CHAT_NAME)

            chat_history.insert(tk.END, "\n\n", CHAT_NAME)

        chat_history.config(state=tk.DISABLED)

        # Clear the input box and set focus
        user_input_box.delete(0, tk.END)
        user_input_box.focus_set()


def reset_chat():
    chat_history.config(state=tk.NORMAL)
    chat_history.delete(1.0, tk.END)
    chat_history.config(state=tk.DISABLED)


def select_model(model_number):
    global selected_model
    selected_model = model_number

    # Resetowanie kolorów wszystkich przycisków
    first_button.config(bg=SIDEBAR_BUTTON_COLOR)
    second_button.config(bg=SIDEBAR_BUTTON_COLOR)
    third_button.config(bg=SIDEBAR_BUTTON_COLOR)

    # Zmiana koloru aktywnego przycisku
    if model_number == 1:
        first_button.config(bg=CHOOSEN_BUTTON_COLOR)
    elif model_number == 2:
        second_button.config(bg=CHOOSEN_BUTTON_COLOR)
    elif model_number == 3:
        third_button.config(bg=CHOOSEN_BUTTON_COLOR)


app = tk.Tk()
app.title(APP_TITLE)
app.configure(bg=BG_COLOR)
app.iconbitmap(default=icon_path)

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

# Główny kontener
app_width = 900
app_height = 800 - 90

x_position = (screen_width - app_width) // 2
y_position = (screen_height - app_height) // 2

app.geometry(f"{app_width}x{app_height}+{x_position}+{y_position}")

main_frame = tk.Frame(app, bg=BG_COLOR)
main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Panel boczny
sidebar = tk.Frame(app, width=200, bg=SIDEBAR_COLOR)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Przyciski na panelu bocznym
first_button = tk.Button(sidebar, text="text to speech", command=lambda: select_model(1), bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
first_button.pack(pady=10, padx=10, fill=tk.X)

second_button = tk.Button(sidebar, text="Emotions", command=lambda: select_model(2), bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
second_button.pack(pady=10, padx=10, fill=tk.X)

third_button = tk.Button(sidebar, text="Stats", command=lambda: select_model(3), bg=SIDEBAR_BUTTON_COLOR, font=FONT, fg=TEXT_COLOR)
third_button.pack(pady=10, padx=10, fill=tk.X)

# Separator
separator = ttk.Separator(sidebar, orient='horizontal')
separator.pack(pady=5, padx=10, fill=tk.X)

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
app.bind('<Return>', lambda event=None: send_button.invoke())

app.mainloop()
