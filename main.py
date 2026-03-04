import qrcode
import tkinter as tk
from tkinter import messagebox
import os

class QRGeneratorApp:
    def __init__(self, window):
        self.window = window
        self.window.title("QuickQR Creator")
        self.window.geometry("350x300")
        self.window.configure(bg="#ffffff")
        self.window.resizable(False, False)
        
        # Title
        tk.Label(self.window, text="QuickQR Creator", font=("Helvetica", 18, "bold"), bg="#ffffff", fg="#000000").pack(pady=20)

        # Data Entry
        tk.Label(self.window, text="URL or Text:", font=("Helvetica", 10), bg="#ffffff", fg="#333333").pack()
        self.entry_data = tk.Entry(self.window, width=35, font=("Helvetica", 10), bd=2, relief="solid")
        self.entry_data.pack(pady=8)

        # Filename Entry
        tk.Label(self.window, text="File Name:", font=("Helvetica", 10), bg="#ffffff", fg="#333333").pack()
        self.entry_filename = tk.Entry(self.window, width=35, font=("Helvetica", 10), bd=2, relief="solid")
        self.entry_filename.pack(pady=8)

        # Generate Button
        self.btn_generate = tk.Button(
            self.window, 
            text="GENERATE QR", 
            command=self.btn_generate_qr, 
            bg="#000000", 
            fg="#ffffff", 
            font=("Helvetica", 10, "bold"),
            width=20,
            height=2,
            cursor="hand2",
            activebackground="#333333",
            activeforeground="#ffffff",
            bd=0
        )
        self.btn_generate.pack(pady=25)

    def btn_generate_qr(self):
        # .strip() prevents issues with accidental spaces
        data = self.entry_data.get().strip()
        filename = self.entry_filename.get().strip()

        if not data or not filename:
            messagebox.showwarning("Warning", "All fields are required!")
            return
        
        try:
            if not os.path.exists("qrcodes"):
                os.makedirs("qrcodes")

            qr = qrcode.make(data)
            save_path = f"qrcodes/{filename}.png"
            qr.save(save_path)
            
            messagebox.showinfo("Success", f"Saved to qrcodes/{filename}.png")

            # Clearing fields for next entry
            self.entry_data.delete(0, tk.END)
            self.entry_filename.delete(0, tk.END)

        except Exception as e:
            messagebox.showerror("Error", f"Failed: {str(e)}")    

if __name__ == "__main__":
    root = tk.Tk()
    app = QRGeneratorApp(root)
    root.mainloop()