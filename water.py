import tkinter as tk
from gpiozero import DigitalInputDevice

# GPIO pin where the signal pin of the water sensor is connected
SENSOR_PIN = 17

class WaterSensorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Water Sensor GUI")
        self.root.geometry("300x100")

        self.label = tk.Label(root, text="Water Sensor Status: ")
        self.label.pack(pady=20)

        # Create a digital input device for the water sensor
        self.water_sensor = DigitalInputDevice(SENSOR_PIN)
        # Set up a callback function to update the GUI when water is detected
        self.water_sensor.when_activated = self.water_detected
        self.water_sensor.when_deactivated = self.water_not_detected

    def water_detected(self):
        self.label.config(text="Water Detected!", fg="red")

    def water_not_detected(self):
        self.label.config(text="No Water Detected", fg="green")

if __name__ == "__main__":
    root = tk.Tk()
    app = WaterSensorApp(root)
    root.mainloop()
