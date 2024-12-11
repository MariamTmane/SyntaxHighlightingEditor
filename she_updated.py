from tkinter import *
import re

# Creating tkinter window/GUI
she = Tk()

# GUI Default appearance
BG_COLOR = "#610773"
TEXT_COLOR = "#ebeaea"

# Window Configuration
she.geometry("800x500")
she.title("Syntax Highlighting Editor")

# Labels
label = Label(she, text="Start typing your Python code below!!", bg="lightblue", fg="black", font=("Arial", 16))
label.pack()

# Textbox initialization
textBox = Text(she, bg=BG_COLOR, fg=TEXT_COLOR, height=15, width=80, font=("Arial", 18))
textBox.pack()


patterns = {
    "comment": r"#.*",
    "keyword": r"\b(if|else|while|return|elif|in|def|import|from|for)\b",
    "string": r"\".*?\"|'.*?'",  
    "parens": r"[\(\[\{\)\]\}]",
    "nums": r"\b\d+\b",
    "operators": r"\+|\+=|==|//|/|-|-=|=|>=|<=|\*|%", 
    "boolean": r"\b(True|False)\b",
    "builtin": r"\b(len|range|append|max|min|print)\b",
}


colors = {
    "comment": "#00FF00",
    "keyword": "#de2bbd",
    "string": "#478a3b",
    "parens": "#a7a5a7",
    "nums": "#d6a247",
    "operators": "#FF5733",  
    "boolean": "#FF5733",
    "builtin": "#5885f5",

}


# Function to apply syntax highlighting to the entire content
def apply_syntax_highlighting(event=None):
    # Remove all the existing tags
    for tag in colors.keys():
        textBox.tag_remove(tag, "1.0", "end")

    # Get the entire content of the text box / user input
    content = textBox.get("1.0", "end-1c")

    # Apply highlighting for each pattern accordingly
    for tag, pattern in patterns.items():
        for match in re.finditer(pattern, content):
            start_index = f"1.0+{match.start()}c"
            end_index = f"1.0+{match.end()}c"
            textBox.tag_add(tag, start_index, end_index)
            textBox.tag_configure(tag, foreground=colors[tag])


# Bind text changes to the syntax highlighting function after each character typed
textBox.bind("<KeyRelease>", apply_syntax_highlighting)

she.mainloop()
