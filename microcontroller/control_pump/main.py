from machine import ADC, Pin
from time import sleep

pump_pin = Pin(19, Pin.OUT)     # Set GPIO 19 as output for the pump
adc_pin = Pin(32)               # Set GPIO 32 as ADC pin
adc = ADC(adc_pin, atten=ADC.ATTN_11DB)

# Initialize variables to track moisture levels
val_max = 0
val_min = 9999999
percentage = 0

def check_moisture():
    # Read the value from the ADC 
    val = adc.read_u16()
    # Update max and min values
    global val_max, val_min, percentage
    if val > val_max:
        val_max = val
    if val < val_min:
        val_min = val
    # Calculate the percentage of the current value within the range
    range = val_max - val_min
    print(f'Current range: {range}')
    if range > 0:
        percentage = round((1 - (val - val_min) / range) * 100, 0)
    # Print values and return the percentage
    print(f'min:{val_min} | val:{val} | max:{val_max} | range:{range} | percentage:{percentage}%')
    return percentage

def activate_pump(percentage, threshold=30):
    # Check if the moisture level is below the threshold
    if percentage < threshold:
        print("Moisture level is low, activating pump.")
        return 1
    else:
        print("Moisture level is sufficient, pump remains off.")
        return 0

while True:
    percentage = check_moisture()
    pump_status = activate_pump(percentage)
    pump_pin.value(pump_status)
    for _ in range(6):
        _ = check_moisture()
        sleep(0.5)
