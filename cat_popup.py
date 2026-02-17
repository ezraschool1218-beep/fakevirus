import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import sys
import os

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return os.path.join(os.path.abspath("."), filename)

def open_more(parent):
    more_window = tk.Toplevel(parent)
    more_window.title("System Alert")
    more_window.geometry("400x300")
    more_window.resizable(False, False)
    more_window.configure(bg="#1e1e1e")

    # Set custom icon
    icon_img = ImageTk.PhotoImage(Image.open(resource_path("alert.png")))
    more_window.iconphoto(False, icon_img)
    more_window.icon_img = icon_img  # prevent garbage collection

    tk.Label(
        more_window,
        text="CRITICAL THREAT DETECTED\n\nJust kidding 😸",
        bg="#1e1e1e",
        fg="white",
        font=("Segoe UI", 11, "bold"),
        justify="center"
    ).pack(pady=10)

    img = Image.open(resource_path("cat.gif"))
    frames = [ImageTk.PhotoImage(frame.copy()) for frame in ImageSequence.Iterator(img)]

    gif_label = tk.Label(more_window, bg="#1e1e1e")
    gif_label.pack()

    def animate(index=0):
        gif_label.config(image=frames[index])
        more_window.after(100, animate, (index + 1) % len(frames))

    animate()

    tk.Button(
        more_window,
        text="Close",
        width=12,
        command=more_window.destroy,
        bg="#d13438",
        fg="white"
    ).pack(pady=15)

def close_app(parent):
    parent.destroy()

# MAIN WINDOW
root = tk.Tk()
root.title("Windows Security Alert!")
root.geometry("420x220")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# Set custom icon (removes feather)
icon_img = ImageTk.PhotoImage(Image.open(resource_path("alert.png")))
root.iconphoto(False, icon_img)
root.icon_img = icon_img  # prevent garbage collection

top_frame = tk.Frame(root, bg="#1e1e1e")
top_frame.pack(pady=25, padx=15, fill="x")

icon_label = tk.Label(
    top_frame,
    text="⚠",
    bg="#1e1e1e",
    fg="#ffcc00",
    font=("Segoe UI", 36, "bold")
)
icon_label.pack(side="left", padx=15)

message = tk.Label(
    top_frame,
    text="SYSTEM BREACH DETECTED!\nUnauthorized access attempt blocked.",
    bg="#1e1e1e",
    fg="white",
    font=("Segoe UI", 12, "bold"),
    justify="left"
)
message.pack(side="left")

button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(pady=20)

tk.Button(
    button_frame,
    text="Reboot",
    width=14,
    command=lambda: close_app(root),
    bg="#d13438",
    fg="white"
).pack(side="left", padx=20)

tk.Button(
    button_frame,
    text="More...",
    width=14,
    command=lambda: open_more(root),
    bg="#3a3a3a",
    fg="white"
).pack(side="right", padx=20)

root.mainloop()
