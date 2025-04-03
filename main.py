import tkinter as tk
from datetime import datetime
import pytz
import time
from tkinter import ttk

class TimeWidget(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Crypto Time Zones")
        self.attributes("-topmost", True)
        self.overrideredirect(True)
        self.geometry("400x500")
        self.configure(bg='#1E1E1E')  # Dark theme background
        
        # Create main frame
        self.main_frame = tk.Frame(self, bg='#1E1E1E')
        self.main_frame.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Title
        title_frame = tk.Frame(self.main_frame, bg='#1E1E1E')
        title_frame.pack(fill='x', pady=(0, 10))
        
        title_label = tk.Label(title_frame, text="🌐 Crypto Trading Times", 
                             font=("Helvetica", 14, "bold"), 
                             bg='#1E1E1E', fg='#00FF00')
        title_label.pack(side='left', pady=5)
        
        # Close button
        self.close_btn = tk.Button(title_frame, text="×", command=self.destroy,
                                 font=("Helvetica", 14), 
                                 bg='#1E1E1E', fg='#FF4444',
                                 bd=0, padx=5,
                                 activebackground='#FF4444',
                                 activeforeground='white')
        self.close_btn.pack(side='right')
        
        # Separator
        ttk.Separator(self.main_frame, orient='horizontal').pack(fill='x', pady=5)
        
        # Create labels for different time zones with their market significance
        self.time_labels = {}
        self.create_time_label("UTC", "🌍 UTC (Global Reference)")
        self.create_time_label("Asia/Tokyo", "🇯🇵 Tokyo (Asian Market Open)")
        self.create_time_label("Asia/Hong_Kong", "🇭🇰 Hong Kong (Asian Trading Hub)")
        self.create_time_label("Asia/Singapore", "🇸🇬 Singapore (Asian Crypto Hub)")
        self.create_time_label("Europe/London", "🇬🇧 London (European Market Open)")
        self.create_time_label("Europe/Berlin", "🇩🇪 Berlin (EU Trading Hub)")
        self.create_time_label("America/New_York", "🇺🇸 New York (US Market Open)")
        self.create_time_label("America/Chicago", "🇺🇸 Chicago (CME Bitcoin Futures)")
        self.create_time_label("America/Los_Angeles", "🇺🇸 San Francisco (Coinbase HQ)")
        self.create_time_label("Asia/Seoul", "🇰🇷 Seoul (Korean Market)")
        
        # Add mouse events for window dragging
        self.bind("<ButtonPress-1>", self.start_move)
        self.bind("<ButtonRelease-1>", self.stop_move)
        self.bind("<B1-Motion>", self.do_move)
        
        self.x = 0
        self.y = 0
        
        # Start updating time
        self.update_time()
    
    def create_time_label(self, timezone, description):
        frame = tk.Frame(self.main_frame, bg='#1E1E1E')
        frame.pack(fill='x', pady=5)
        
        label = tk.Label(frame, text="", font=("Consolas", 11),
                        bg='#1E1E1E', fg='#FFFFFF',
                        anchor='w', justify='left')
        label.pack(fill='x')
        
        self.time_labels[timezone] = {
            'label': label,
            'description': description
        }
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def stop_move(self, event):
        self.x = None
        self.y = None
    
    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")
    
    def update_time(self):
        now_utc = datetime.now(pytz.UTC)
        
        for tz_name, label_info in self.time_labels.items():
            tz = pytz.timezone(tz_name)
            local_time = now_utc.astimezone(tz)
            
            # Format time with custom styling
            time_str = local_time.strftime("%H:%M:%S")
            date_str = local_time.strftime("%Y-%m-%d")
            
            # Update label with description and formatted time
            label_info['label'].config(
                text=f"{label_info['description']}\n"
                     f"  {time_str}  |  {date_str}"
            )
        
        # Schedule next update
        self.after(1000, self.update_time)

if __name__ == "__main__":
    app = TimeWidget()
    app.mainloop()