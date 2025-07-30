import tkinter as tk
from tkinter import filedialog, colorchooser, messagebox
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

class TextOverlayApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Overlay Generator (create by xvideos.com)")
        self.root.geometry("850x480")
        self.root.configure(bg="#1e1e1e")

        # Set icon
        try:
            icon = Image.open("icon/icon.png").resize((32, 32))
            icon_tk = ImageTk.PhotoImage(icon)
            self.root.iconphoto(False, icon_tk)
        except Exception as e:
            print("Can't set icon:", e)

        self.image_path = ""
        self.font_path = ""
        self.text_file_path = ""
        self.output_folder = ""
        self.font_color = (255, 255, 255)

        self.build_ui()

    def build_ui(self):
        label_config = {"bg": "#1e1e1e", "fg": "white", "font": ("Arial", 10), "anchor": "w"}
        btn_config = {
            "width": 20, "bg": "#3a3a3a", "fg": "white", "font": ("Arial", 10, "bold"),
            "activebackground": "#555", "relief": "flat", "highlightthickness": 0
        }

        # Dùng grid toàn bộ layout
        for i in range(6):
            tk.Label(self.root, text=f"{i+1}.", **label_config).grid(row=i, column=0, sticky="ne", padx=10, pady=5)

        # 1. Image
        tk.Label(self.root, text="Choose base image:", **label_config).grid(row=0, column=1, sticky="w")
        tk.Button(self.root, text="Choose Image", command=self.choose_image, **btn_config).grid(row=0, column=2, sticky="w")
        self.image_label = tk.Label(self.root, text="", **label_config)
        self.image_label.grid(row=0, column=3, sticky="w", padx=5)

        # 2. Font
        tk.Label(self.root, text="Choose font file (.ttf/.otf):", **label_config).grid(row=1, column=1, sticky="w")
        tk.Button(self.root, text="Choose Font", command=self.choose_font, **btn_config).grid(row=1, column=2, sticky="w")
        self.font_label = tk.Label(self.root, text="", **label_config)
        self.font_label.grid(row=1, column=3, sticky="w", padx=5)

        # 3. Text file
        tk.Label(self.root, text="Choose text file (.txt):", **label_config).grid(row=2, column=1, sticky="w")
        tk.Button(self.root, text="Choose Text File", command=self.choose_text_file, **btn_config).grid(row=2, column=2, sticky="w")
        self.textfile_label = tk.Label(self.root, text="", **label_config)
        self.textfile_label.grid(row=2, column=3, sticky="w", padx=5)

        # 4. Color
        tk.Label(self.root, text="Choose text color:", **label_config).grid(row=3, column=1, sticky="w")
        tk.Button(self.root, text="Choose Color", command=self.choose_color, **btn_config).grid(row=3, column=2, sticky="w")
        self.color_label = tk.Label(self.root, text="Selected Color: (255, 255, 255)", **label_config)
        self.color_label.grid(row=3, column=3, sticky="w", padx=5)

        # 5. Folder
        tk.Label(self.root, text="Choose output folder:", **label_config).grid(row=4, column=1, sticky="w")
        tk.Button(self.root, text="Choose Folder", command=self.choose_folder, **btn_config).grid(row=4, column=2, sticky="w")
        self.folder_label = tk.Label(self.root, text="", **label_config)
        self.folder_label.grid(row=4, column=3, sticky="w", padx=5)

        # 6. Font size + offset
        tk.Label(self.root, text="Font Size:", **label_config).grid(row=5, column=1, sticky="e", pady=(10, 0))
        self.font_size_entry = tk.Entry(self.root, width=8)
        self.font_size_entry.insert(0, "100")
        self.font_size_entry.grid(row=5, column=2, sticky="w", pady=(10, 0))

        tk.Label(self.root, text="Y Offset (px):", **label_config).grid(row=5, column=2, padx=(90, 0), sticky="w", pady=(10, 0))
        self.y_offset_entry = tk.Entry(self.root, width=8)
        self.y_offset_entry.insert(0, "100")
        self.y_offset_entry.grid(row=5, column=2, padx=(200, 0), sticky="w", pady=(10, 0))

        # Status
        self.status_label = tk.Label(self.root, text="", **label_config)
        self.status_label.grid(row=6, column=1, columnspan=3, sticky="w", pady=(10, 0), padx=10)

        # Button Generate
        tk.Button(self.root, text="Generate Images", command=self.generate_images, bg="#4CAF50", fg="white",
                  font=("Arial", 11, "bold"), padx=10, pady=5, relief="flat").grid(row=7, column=2, pady=15, sticky="w")

    def choose_image(self):
        path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg")])
        if path:
            self.image_path = path
            self.image_label.config(text=os.path.basename(path))

    def choose_font(self):
        path = filedialog.askopenfilename(filetypes=[("Font files", "*.ttf *.otf")])
        if path:
            self.font_path = path
            self.font_label.config(text=os.path.basename(path))

    def choose_text_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if path:
            self.text_file_path = path
            self.textfile_label.config(text=os.path.basename(path))

    def choose_color(self):
        color = colorchooser.askcolor(title="Choose text color")
        if color[0]:
            self.font_color = tuple(map(int, color[0]))
            self.color_label.config(text=f"Selected Color: {self.font_color}")

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.output_folder = folder
            self.folder_label.config(text=f"Saving to: {folder}")

    def generate_images(self):
        if not all([self.image_path, self.font_path, self.text_file_path, self.output_folder]):
            messagebox.showerror("Missing info", "Please select all required files and settings.")
            return

        try:
            font_size = int(self.font_size_entry.get())
            y_offset = int(self.y_offset_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Font size and Y offset must be integers.")
            return

        with open(self.text_file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f if line.strip()]

        total = len(lines)
        if total == 0:
            messagebox.showinfo("No text", "Text file is empty.")
            return

        base_img = Image.open(self.image_path).convert("RGBA")
        font = ImageFont.truetype(self.font_path, font_size)

        for i, text in enumerate(lines, start=1):
            img = base_img.copy()
            draw = ImageDraw.Draw(img)
            text_width, text_height = draw.textbbox((0,0), text, font=font)[2:]
            x = (img.width - text_width) // 2
            y = y_offset
            draw.text((x, y), text, font=font, fill=self.font_color)

            out_path = os.path.join(self.output_folder, f"{i:03d}-{text}.png")
            img.save(out_path)
            self.status_label.config(text=f"Processing image {i}/{total}")
            self.root.update_idletasks()

        self.status_label.config(text=f"Done! {total} images saved to {self.output_folder}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TextOverlayApp(root)
    root.mainloop()
