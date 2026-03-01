import random
import time
import csv
import matplotlib.pyplot as plt


# ==========================
# SMART FARM CLASS
# ==========================
class SmartFarm:
    def _init_(self):
        self.soil_moisture = 50
        self.temperature = 25
        self.humidity = 60

        self.irrigation = False
        self.fan = False
        self.heater = False

        self.history = {
            "soil": [],
            "temp": [],
            "humidity": []
        }

    # ==========================
    # SENSOR SIMULATION
    # ==========================
    def read_sensors(self):
        # Natural changes
        self.soil_moisture -= random.uniform(0.5, 1.5)
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-1, 1)

        # Clamp values
        self.soil_moisture = max(0, min(100, self.soil_moisture))
        self.temperature = max(0, min(50, self.temperature))
        self.humidity = max(0, min(100, self.humidity))

    # ==========================
    # AI CONTROL LOGIC
    # ==========================
    def control_system(self):
        # Irrigation logic
        if self.soil_moisture < 35:
            self.irrigation = True
        elif self.soil_moisture > 70:
            self.irrigation = False

        # Temperature control
        if self.temperature > 30:
            self.fan = True
            self.heater = False
        elif self.temperature < 18:
            self.heater = True
            self.fan = False
        else:
            self.fan = False
            self.heater = False

        # Apply irrigation effect
        if self.irrigation:
            self.soil_moisture += 3

        # Apply heater effect
        if self.heater:
            self.temperature += 1

        # Apply fan effect
        if self.fan:
            self.temperature -= 1

    # ==========================
    # SAVE DATA
    # ==========================
    def log_data(self):
        self.history["soil"].append(self.soil_moisture)
        self.history["temp"].append(self.temperature)
        self.history["humidity"].append(self.humidity)

        with open("farm_data.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([
                self.soil_moisture,
                self.temperature,
                self.humidity
            ])

    # ==========================
    # DASHBOARD
    # ==========================
    def show_dashboard(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.history["soil"], label="Soil Moisture")
        plt.plot(self.history["temp"], label="Temperature")
        plt.plot(self.history["humidity"], label="Humidity")
        plt.legend()
        plt.title("Smart Farm Sensor Data")
        plt.xlabel("Time")
        plt.ylabel("Value")
        plt.show()


# ==========================
# MAIN PROGRAM
# ==========================
farm = SmartFarm()

print("🌱 Smart Farm System Running...\n")

# Write CSV header
with open("farm_data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Soil Moisture", "Temperature", "Humidity"])

for minute in range(60):  # simulate 60 cycles
    farm.read_sensors()
    farm.control_system()
    farm.log_data()

    print(f"Minute {minute + 1}")
    print(f"Soil Moisture: {farm.soil_moisture:.1f}%")
    print(f"Temperature: {farm.temperature:.1f}°C")
    print(f"Humidity: {farm.humidity:.1f}%")
    print(f"Irrigation: {'ON' if farm.irrigation else 'OFF'}")
    print(f"Fan: {'ON' if farm.fan else 'OFF'}")
    print(f"Heater: {'ON' if farm.heater else 'OFF'}")
    print("-" * 40)

    time.sleep(0.2)

farm.show_dashboard()
