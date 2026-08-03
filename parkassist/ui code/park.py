import tkinter as tk
from tkinter import messagebox
import serial
import threading
import datetime
import random
import string

class SmartParkingUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Parking System")
        self.root.geometry("1980x1200")
        self.root.configure(bg="#2c3e50")  # Dark Blue Background

        # Initialize the sensor connection status label before usage
        self.sensor_label = tk.Label(self.root, text="Connecting to Arduino...", font=("Helvetica", 14), fg="yellow", bg="#2c3e50")
        self.sensor_label.pack(pady=20)

        # Initialize Serial Connection
        try:
            self.ser = serial.Serial('COM5', 9600, timeout=1)  # Update COM port if needed
            self.sensor_label.config(text="Connected to Arduino", fg="green")
        except serial.SerialException:
            self.ser = None
            self.sensor_label.config(text="Failed to connect to Arduino", fg="red")

        # Sensor States (5 Parking Spots)
        self.sensor_states = {f"Sensor {i}": False for i in range(1, 6)}  # False indicates spot is available

        # Reserved States
        self.reserved_states = {f"Sensor {i}": False for i in range(1, 6)}  # Track if the spot is reserved

        # Setup UI
        self.setup_ui()
        self.start_serial_thread()

    def setup_ui(self):
        """Create UI Elements"""
        title_label = tk.Label(self.root, text="Smart Parking System",
                               font=("Helvetica", 24, "bold"), fg="#ecf0f1",
                               bg="#2c3e50")
        title_label.pack(pady=10)

        self.spots_frame = tk.Frame(self.root, bg="#2c3e50")
        self.spots_frame.pack(pady=20)

        self.spots = {}
        for i in range(5):
            frame = tk.Frame(self.spots_frame, bg="#34495e", padx=20, pady=20)
            frame.grid(row=0, column=i, padx=10)

            reserve_button = tk.Button(frame, text="Reserve", font=("Helvetica", 12), fg="black", bg="#f39c12",
                                       command=lambda i=i: self.reserve_spot(f"Sensor {i+1}"))
            reserve_button.pack(pady=5)

            self.spots[f"Sensor {i+1}"] = {
                "frame": frame,
                "label": tk.Label(frame, text=f"Spot {i+1}", font=("Helvetica", 14, "bold"), fg="#ecf0f1", bg="#34495e"),
                "status": tk.Label(frame, text="Available", font=("Helvetica", 12), fg="white", bg="#e74c3c", width=15, height=2),
                "reserve_button": reserve_button
            }

            self.spots[f"Sensor {i+1}"]["label"].pack(pady=(0, 5))
            self.spots[f"Sensor {i+1}"]["status"].pack(pady=5)

            self.update_spot_display(f"Sensor {i+1}", False)

        # Add Reserve Any Spot Button
        reserve_any_button = tk.Button(self.root, text="Reserve Any Spot", font=("Helvetica", 16), fg="black", bg="#e67e22", command=self.reserve_any_spot)
        reserve_any_button.pack(pady=20)

    def update_spot_display(self, sensor, is_occupied):
        """Update Parking Spot Display"""
        if sensor in self.spots:
            spot = self.spots[sensor]
            if is_occupied:
                spot["status"].config(text="Occupied", bg="#e74c3c", fg="black")  
            elif self.reserved_states[sensor]:
                spot["status"].config(text="Reserved", bg="#f39c12", fg="black")
            else:
                spot["status"].config(text="Available", bg="#2ecc71", fg="white")

    def generate_token(self, length=8):
        """Generate a unique token for the reservation"""
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def reserve_spot(self, sensor):
        """Reserve a parking spot"""
        if self.reserved_states[sensor]:
            return  # Already reserved

        self.reserved_states[sensor] = True
        self.update_spot_display(sensor, False)
        self.spots[sensor]["reserve_button"].config(state="disabled", text="Reserved")

        token = self.generate_token()
        self.generate_receipt(sensor, token)

        messagebox.showinfo("Reservation Confirmed", f"Spot Reserved: {sensor}\nToken: {token}")

    def reserve_any_spot(self):
        """Automatically reserve the first available spot"""
        for i in range(1, 6):
            sensor = f"Sensor {i}"
            if not self.reserved_states[sensor]:
                self.reserve_spot(sensor)
                break

    def shift_reservation_if_necessary(self):
        """Check if reserved spot is occupied and shift reservation"""
        for sensor in self.reserved_states.keys():
            if self.reserved_states[sensor]:
                if self.sensor_states[sensor]:  # Spot is occupied
                    self.reserved_states[sensor] = False
                    self.update_spot_display(sensor, False)
                    self.spots[sensor]["reserve_button"].config(state="normal", text="Reserve")

                    for i in range(1, 6):
                        next_spot = f"Sensor {i}"
                        if not self.reserved_states[next_spot] and not self.sensor_states[next_spot]:
                            self.reserve_spot(next_spot)
                            break

    def generate_receipt(self, sensor, token):
        """Generate Receipt for Reservation"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        receipt_data = (
            f"Parking Spot Reservation\n"
            f"Spot: {sensor}\n"
            f"Status: Reserved\n"
            f"Time: {timestamp}\n"
            f"Token: {token}"
        )

        file_name = f"{sensor.replace(' ', '_')}_receipt.txt"
        with open(file_name, 'w') as file:
            file.write(receipt_data)

        print(f"Receipt generated: {file_name}")

    def read_serial_data(self):
        """Read Serial Data from Arduino"""
        if self.ser:
            try:
                data = self.ser.readline().decode("utf-8").strip()
                if data:
                    for sensor in self.sensor_states.keys():
                        if sensor in data:
                            is_occupied = "Object Detected" in data
                            self.sensor_states[sensor] = is_occupied
                            self.root.after(1, self.update_spot_display, sensor, is_occupied)
            except Exception:
                pass

            self.shift_reservation_if_necessary()
            self.root.after(1, self.read_serial_data)

    def start_serial_thread(self):
        """Start Background Thread for Serial Reading"""
        thread = threading.Thread(target=self.read_serial_data, daemon=True)
        thread.start()

# Run Application
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartParkingUI(root)
    root.mainloop()