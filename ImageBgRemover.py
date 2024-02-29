import tkinter as tk
from tkinter import filedialog
from rembg import remove
from PIL import Image, ImageTk

class BackgroundRemoverApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Background Remover App")

        # Create labels
        self.label = tk.Label(master, text="Select an image:")
        self.label.pack()

        # Create buttons
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_image)
        self.browse_button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_image)
        self.convert_button.pack()

        self.save_button = tk.Button(master, text="Select Save Folder", command=self.select_save_folder)
        self.save_button.pack()

        # Initialize image paths
        self.input_path = ''
        self.output_path = ''

    def browse_image(self):
        self.input_path = filedialog.askopenfilename(title="Select an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])

        # Display selected image
        if self.input_path:
            image = Image.open(self.input_path)
            image.thumbnail((300, 300))
            imgtk = ImageTk.PhotoImage(image)
            self.label.config(image=imgtk)
            self.label.image = imgtk

    def convert_image(self):
        if self.input_path:
            input_image = Image.open(self.input_path)
            output_image = remove(input_image)

            if self.output_path:
                output_path_with_extension = f"{self.output_path}/output.png"
                output_image.save(output_path_with_extension)
            
            # Display converted image
                converted_image = Image.open(output_path_with_extension)
                converted_image.thumbnail((300, 300))
                imgtk = ImageTk.PhotoImage(converted_image)
                self.label.config(image=imgtk)
                self.label.image = imgtk

                tk.messagebox.showinfo("Success", "Image converted and saved successfully!")
            else:
                tk.messagebox.showwarning("Warning", "Please select a save folder before converting.")
        else:
            tk.messagebox.showwarning("Warning", "Please select an image before converting.")

    def select_save_folder(self):
        self.output_path = filedialog.askdirectory(title="Select a folder to save converted image")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackgroundRemoverApp(root)
    root.mainloop()
