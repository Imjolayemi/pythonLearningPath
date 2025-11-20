"""This project is a simple agricultural bot that simulates one decision cycle of a robot monitoring a greenhouse. The bot checks temperature and humidity levels and decides whether to water the plants or adjust the temperature."""

tomato = {
    "name": "Tomato", # crop name
    "optimal_temp_range": (20, 25),  # in Celsius
    "optimal_humidity_range": (60, 80),  # in percentage
    "water_threshold": 70,  # soil moisture percentage below which watering is needed
    "system_active": True 
}

pepper = {
    "name": "Pepper", # crop name
    "optimal_temp_range": (18, 24),  # in Celsius
    "optimal_humidity_range": (50, 70),  # in percentage
    "water_threshold": 65,  # soil moisture percentage below which watering is needed
    "system_active": True 
}


crop_config = {
    "tomato": tomato,
    "pepper": pepper
}

actionLog = []


# Using triple quotes for a multi-line string
# You can generate these online by searching "Text to ASCII Art generator"
logo = """
    ___    ____  ____  ____         ____  ____  ______
   /   |  / __ \/ __ \/  _/        / __ )/ __ \/_  __/
  / /| | / /_/ / /_/ // / _____   / __  / / / / / /   
 / ___ |/ _, _/ _, _// / _____  /_/ / /_/ / / /    
/_/  |_/_/ |_/_/ |_/___/        /_____/\____/ /_/     
                                                  
      --- SYSTEM V.1.0 INITIALIZING ---
"""
print(logo)

crop_type = input("Enter crop type (tomato/pepper): ").strip().lower() # getting user input for crop type
crop = crop_config.get(crop_type) # fetching crop configuration based on user input

if not crop:
    print("Invalid crop type. Please restart and enter 'tomato' or 'pepper'.")
    exit()
else:
    crop_name = crop['name']
    print(f"Monitoring system for {crop_name} initialized.")

    raw_moisture = input(f"Enter current soil moisture percentage (0-100) for {crop_name}: ") # getting user input for soil moisture
    raw_temperature = input(f"Enter current temperature in Celsius for {crop_name}: ") # getting user input for temperature

    proccessed_moisture = int(raw_moisture) # converting user input for raw moisure to integer
    proccessed_temperature = float(raw_temperature) # converting user input for raw temperature to float

    systemActive = crop['system_active'] # checking if the system is active
    if systemActive:
        print(f"System is active. Monitoring {crop_name} conditions...")
        
        # Check soil moisture
        if proccessed_moisture < crop['water_threshold']:
            actionLog.append(f"Watering {crop_name} plants. Soil moisture at {proccessed_moisture}%.")
            print(f"Action: Watering {crop_name} plants.")
        else:
            actionLog.append(f"Soil moisture adequate at {proccessed_moisture}%. No watering needed.")
            print(f"Action: No watering needed for {crop_name} plants.")

        # Check temperature
        temp_min, temp_max = crop['optimal_temp_range']
        if proccessed_temperature < temp_min:
            actionLog.append(f"Increasing temperature for {crop_name}. Current temperature: {proccessed_temperature}°C.")
            print(f"Action: Increasing temperature for {crop_name}.")
        elif proccessed_temperature > temp_max:
            actionLog.append(f"Decreasing temperature for {crop_name}. Current temperature: {proccessed_temperature}°C.")
            print(f"Action: Decreasing temperature for {crop_name}.")
        else:
            actionLog.append(f"Temperature optimal at {proccessed_temperature}°C. No adjustment needed.")
            print(f"Action: No temperature adjustment needed for {crop_name}.")
        
    else:
        actionLog.append("System inactive. No actions taken.")
        print("System is inactive. No actions taken.")


# Ending Program Message
shutdown_logo = """
    ____  ____  ____   __________  ___    __  ___
   / __ \/ __ \/ __ \ / ____/ __ \/   |  /  |/  /
  / /_/ / /_/ / / / // / __/ /_/ / /| | / /|_/ / 
 / ____/ _, _/ /_/ // /_/ / _, _/ ___ |/ /  / /  
/_/   /_/ |_|\____(_)____/_/ |_/_/  |_/_/  /_/   
                                                 
    _______   ______  __________ 
   / ____/ | / / __ \/ ____/ __ \\
  / __/ /  |/ / / / / __/ / / / /
 / /___/ /|  / /_/ / /___/ /_/ / 
/_____/_/ |_/_____/_____/_____/  
"""

print(shutdown_logo)