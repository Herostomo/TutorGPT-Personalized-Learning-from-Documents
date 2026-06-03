import customtkinter as ctk
from tkinter import filedialog
import shutil
import os
import subprocess
from rag_engine import ask_question

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class TutorGPT(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("TutorGPT")
        self.geometry("900x700")

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="TutorGPT",
            font=("Arial", 28, "bold")
        )
        title.pack(pady=15)

        self.upload_btn = ctk.CTkButton(
            self,
            text="Upload Document",
            command=self.upload_document
        )
        self.upload_btn.pack(pady=10)

        self.chat_box = ctk.CTkTextbox(
            self,
            width=800,
            height=500
        )
        self.chat_box.pack(
            padx=20,
            pady=10
        )

        bottom_frame = ctk.CTkFrame(self)
        bottom_frame.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.question_entry = ctk.CTkEntry(
            bottom_frame,
            placeholder_text="Ask something..."
        )

        self.question_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=5
        )

        send_btn = ctk.CTkButton(
            bottom_frame,
            text="Send",
            command=self.send_question
        )

        send_btn.pack(
            side="right",
            padx=5
        )

    def upload_document(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Documents", "*.pdf *.docx")
            ]
        )

        if not file_path:
            return

        filename = os.path.basename(file_path)

        shutil.copy(
            file_path,
            os.path.join(
                "documents",
                filename
            )
        )

        subprocess.run(
            ["python", "build_index.py"]
        )

        self.chat_box.insert(
            "end",
            f"\n Uploaded: {filename}\n"
        )

    def send_question(self):

        question = self.question_entry.get()

        if not question:
            return

        self.chat_box.insert(
            "end",
            f"\n You: {question}\n"
        )

        self.update()

        answer = ask_question(question)

        self.chat_box.insert(
            "end",
            f"\n TutorGPT: {answer}\n"
        )

        self.question_entry.delete(
            0,
            "end"
        )

if __name__ == "__main__":
    app = TutorGPT()
    app.mainloop()