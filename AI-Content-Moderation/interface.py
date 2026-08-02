import customtkinter as ctk
from detector import detect
from translations import TEXTS


class Interface :

    def __init__(self):

        self.window = ctk.CTk()

        self.window.title("AI Content Moderation")

        self.window.geometry("1200x750")

        self.window.grid_rowconfigure(0, weight=1)
        
        self.window.grid_columnconfigure(0, weight=1)
        
        self.main_frame = ctk.CTkScrollableFrame(self.window, fg_color="transparent")
        
        self.main_frame.grid(row=0, column=0, sticky="nsew")
        
        self.main_frame.grid_columnconfigure((0, 1), weight=0)

        self.language = "EN"

        self.placeholder = True

        self.has_output = False

        self.title = ctk.CTkLabel(

            self.main_frame,

            text=TEXTS[self.language]["title"],

            font=("Arial", 28, "bold")

        )

        self.subtitle = ctk.CTkLabel(

            self.main_frame,

            text=TEXTS[self.language]["sub"],

            font=("Arial", 20)

        )

        self.textbox = ctk.CTkTextbox(

            self.main_frame,

            width=500,

            height=300,

            wrap="word"

        )

        self.textbox.tag_config(

            "placeholder",

            justify="center"

        )

        self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")

        self.textbox.bind("<FocusIn>", self.remove_placeholder)

        self.textbox.bind("<FocusOut>", self.restore_placeholder)

        self.analyze_button = ctk.CTkButton(

            self.main_frame,

            command=self.analyze,

            text=TEXTS[self.language]["analyze"]

        )

        self.result_label = ctk.CTkLabel(

            self.main_frame,

            text=TEXTS[self.language]["results"],

            font=("Consolas", 12),

            justify="left",

            anchor="w"

        )

        self.reset_button = ctk.CTkButton(

            self.main_frame,

            command=self.reset,

            text=TEXTS[self.language]["reset"]

        )

        self.language_button = ctk.CTkButton(

            self.main_frame,

            command=self.change_language,

            text=TEXTS[self.language]["lang"]

        )

        self.title.grid(row=0, column=0, columnspan=2, padx=20, pady=(20,5))

        self.subtitle.grid(row=1, column=0, columnspan=2, padx=20, pady=(0,20))

        self.textbox.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        self.analyze_button.grid(row=3, column=0, columnspan=2, padx=20, pady=20)

        self.result_label.grid(row=4, column=0, columnspan=2, padx=20, pady=20)

        self.reset_button.grid(row=5, column=0, padx=20, pady=20)

        self.language_button.grid(row=5, column=1, padx=20, pady=20)

    def run(self):

        self.window.mainloop()

    def analyze(self):

        text = self.textbox.get("1.0", "end").strip()

        if not text :

            return self.result_label.configure(

                text=TEXTS[self.language]["no_text"]

            )

        else:

            self.analyze_button.configure(

                text=TEXTS[self.language]["analyzing"]

            )

            try:

                results = detect(text)

            except Exception as error:
                
                self.result_label.configure(
                            
                    text=f'{TEXTS[self.language]["error"]} : {error}'
                            
                )

                self.has_output = True

                self.analyze_button.configure(
                
                    text=TEXTS[self.language]["analyze"]
                
                )
                
                return

            self.has_output = True

            self.result_label.configure(

                text=results

            )

            self.analyze_button.configure(

                command=self.analyze,
                
                text=TEXTS[self.language]["analyze"]
            
            )

    def remove_placeholder(self, event):

        if self.placeholder:

            self.textbox.delete("1.0", "end")

            self.placeholder = False

    def restore_placeholder(self, event):

        text = self.textbox.get("1.0", "end").strip()

        if not text:

            self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")

            self.placeholder = True

    def reset(self):
    
        self.textbox.delete("1.0", "end")

        self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")
        
        self.placeholder = True
            
        self.analyze_button.configure(
            
            command=self.analyze,
            
            text=TEXTS[self.language]["analyze"]
            
        )

        self.has_output = False
            
        self.result_label.configure(
            
            text=TEXTS[self.language]["results"],
            
        )

    def change_language(self):

        if self.language == "EN":

            self.language = "FR"

        else:

            self.language = "EN"

        self.title.configure(
        
            text=TEXTS[self.language]["title"],

            font=("Arial", 28, "bold")
        
        )
        
        self.subtitle.configure(
        
            text=TEXTS[self.language]["sub"],

            font=("Arial", 20)
        
        )

        if self.placeholder:

            self.textbox.delete("1.0", "end")

            self.textbox.insert("1.0", TEXTS[self.language]["box"], "placeholder")
        
        self.textbox.configure(
        
            width=500,
        
            height=300,

            wrap="word"
        
        )
        
        self.analyze_button.configure(
        
            command=self.analyze,
        
            text=TEXTS[self.language]["analyze"]
        
        )
        
        if not self.has_output :

            self.result_label.configure(
            
                text=TEXTS[self.language]["results"],

                font=("Consolas", 12),

                justify="left",

                anchor="w"

            )
        
        self.reset_button.configure(
        
            command=self.reset,
        
            text=TEXTS[self.language]["reset"]
        
        )
        
        self.language_button.configure(
        
            command=self.change_language,
        
            text=TEXTS[self.language]["lang"]
        
        )