import tkinter as tk
from tkinter import scrolledtext, messagebox
from antlr4 import *
from CompiledFiles.SampleLexer import SampleLexer
from CompiledFiles.SampleParser import SampleParser
from ASTGeneration import ASTGeneration
from CodeRunner import CodeRunner

class QueryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System Query")

        self.label = tk.Label(root, text="Enter your query:")
        self.label.pack()

        self.query_entry = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10)
        self.query_entry.pack()

        self.run_button = tk.Button(root, text="Run Query", command=self.run_query)
        self.run_button.pack()

        self.result_label = tk.Label(root, text="Result:")
        self.result_label.pack()

        self.result_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=10, state=tk.DISABLED)
        self.result_text.pack()

    def run_query(self):
        query = self.query_entry.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Input Error", "Please enter a query.")
            return

        try:
            input_stream = InputStream(query)
            lexer = SampleLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = SampleParser(stream)
            tree = parser.program()

            ast_generator = ASTGeneration()
            ast_tree = tree.accept(ast_generator)

            code_runner = CodeRunner()
            result = ast_tree.accept(code_runner)

            self.result_text.config(state=tk.NORMAL)
            self.result_text.delete("1.0", tk.END)
            self.result_text.insert(tk.INSERT, str(result))
            self.result_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = QueryApp(root)
    root.mainloop()