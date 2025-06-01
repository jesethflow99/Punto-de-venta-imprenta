import tkinter as tk
from tkinter import messagebox
import socket
import webbrowser
import subprocess
import threading


def get_local_ip():
    # Obtener IP local de la red (no 127.0.0.1)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # conectar a IP externa para obtener la IP local
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Launcher Flask Server")
        self.geometry("400x200")
        
        self.host_all_network = tk.BooleanVar(value=False)
        self.server_process = None
        
        self.init_main_screen()
    
    def init_main_screen(self):
        self.clear_widgets()
        
        label = tk.Label(self, text="Doble clic para iniciar", font=("Arial", 14))
        label.pack(pady=20)
        
        # Simulamos doble clic con un botón normal para demo
        btn = tk.Button(self, text="Doble clic (simulado)", command=self.open_options)
        btn.pack(pady=10)
    
    def open_options(self):
        self.clear_widgets()
        
        tk.Label(self, text="¿Hostear en toda la red?", font=("Arial", 12)).pack(pady=10)
        tk.Checkbutton(self, text="Sí", variable=self.host_all_network).pack()
        
        self.ip_local = get_local_ip()
        self.ip_label = tk.Label(self, text=f"IP Local: {self.ip_local}\nLocalhost: 127.0.0.1")
        self.ip_label.pack(pady=10)
        
        start_btn = tk.Button(self, text="Levantar servidor", command=self.start_server)
        start_btn.pack(pady=5)
        
        go_btn = tk.Button(self, text="Ir a la página", command=self.open_browser, state='disabled')
        go_btn.pack(pady=5)
        self.go_btn = go_btn
    
    def start_server(self):
        # Evitar levantar varias veces
        if self.server_process:
            messagebox.showinfo("Info", "El servidor ya está corriendo.")
            return
        
        host = "0.0.0.0" if self.host_all_network.get() else "127.0.0.1"
        port = 5000
        
        # Lanzar Flask app en un thread para no bloquear GUI
        def run_server():
            # Aquí lanzas tu servidor Flask; ajustar según tu app
            import sys
            python_path = sys.executable  # Esto obtiene el Python del entorno virtual actual
            subprocess.run([python_path, "app.py", "--host", host, "--port", str(port)])

        
        threading.Thread(target=run_server, daemon=True).start()
        
        self.go_btn.config(state='normal')
        messagebox.showinfo("Servidor iniciado", f"Servidor corriendo en http://{host}:{port}")
    
    def open_browser(self):
        host = "0.0.0.0" if self.host_all_network.get() else "127.0.0.1"
        url = f"http://{self.ip_local if host=='0.0.0.0' else '127.0.0.1'}:5000"
        webbrowser.open(url)
    
    def clear_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
