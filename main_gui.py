from tkinter import *
from tkinter import filedialog, messagebox

def preprocess_text(text):
    # Placeholder function for preprocessing text
    return text

def generate_summary(text, sentences):
    # Placeholder function for generating summary
    # This is a simple example that returns the first 'sentences' sentences
    sentences_list = text.split('.')
    summary = '.'.join(sentences_list[:sentences])
    return summary

def summarize_text_gui():
    def open_file():
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
            if file_path:
                with open(file_path, 'r', encoding='utf-8') as file:
                    text = file.read()
                    text_box.delete(1.0, END)  # Clear the text box before inserting new text
                    text_box.insert(1.0, text)
            else:
                messagebox.showwarning("File not selected", "No file was selected.")
        except Exception as e:
            messagebox.showerror("Error opening file", f"An error occurred while opening the file: {e}")

    def summarize():
        try:
            text = text_box.get(1.0, END).strip()
            if not text:
                messagebox.showwarning("Empty Text", "Please load a text file or input text to summarize.")
                return
            
            processed_text = preprocess_text(text)
            summary = generate_summary(processed_text, 3)
            
            summary_box.delete(1.0, END)  # Clear the summary box before inserting new summary
            summary_box.insert(1.0, summary)
        except Exception as e:
            messagebox.showerror("Error summarizing text", f"An error occurred during summarization: {e}")

    root = Tk()
    root.title("Text Summarizer")
    root.geometry("600x400")

    Button(root, text="Open File", command=open_file).pack()
    text_box = Text(root, height=10)
    text_box.pack()

    Button(root, text="Summarize", command=summarize).pack()
    summary_box = Text(root, height=10)
    summary_box.pack()

    root.mainloop()

summarize_text_gui()