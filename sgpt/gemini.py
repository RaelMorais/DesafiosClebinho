import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai
import textwrap
import api_user_key_class as api
class gemini_app:
    def __init__(self):
        self.a = ""
    def gemini_app_api(self):
        def to_markdown(text):
            text = text.replace("•", "  *")
            return textwrap.indent(text, "> ", predicate=lambda _: True)

        GOOGLE_API_KEY = api.api_key_user().api_user() 
        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel('gemini-1.5-flash')

        def generate_content():
            user_prompt = entry.get()
            if user_prompt.strip().lower() == 'exit':
                root.quit()
            else:
                try:
                    response = model.generate_content(user_prompt)
                    output_text = response.text if hasattr(response, 'text') else "Erro"
                except Exception as e:
                    output_text = f"Erro: {str(e)}"
                
                output_area.config(state=tk.NORMAL)
                output_area.delete(1.0, tk.END) 
                output_area.insert(tk.END, to_markdown(output_text))
                output_area.config(state=tk.DISABLED)

        root = tk.Tk()
        root.configure(bg='lightblue')

        root.title("Questões")

        label = tk.Label(root, text="Qual sua questão?")
        label.pack(pady=5)

        entry = tk.Entry(root, width=50)
        entry.pack(pady=5)

        generate_button = tk.Button(root, text="Gerar", command=generate_content, bg='red', fg='white', font=('Arial', 12, 'bold'))
        generate_button.pack(pady=5)

        output_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
        output_area.pack(pady=5)
        output_area.config(state=tk.DISABLED) 

        root.mainloop()
