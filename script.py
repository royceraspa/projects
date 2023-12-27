import time
import smbus2

# Define the I2C address of the LCD module
LCD_ADDRESS = 0x27

# Define commands for LCD
LCD_CMD = 0x00
LCD_DATA = 0x40

# Define LCD column and row size
LCD_COLUMNS = 16
LCD_ROWS = 2

# Initialize the I2C bus
bus = smbus2.SMBus(1)

def lcd_byte(cmd, mode):
    bus.write_byte_data(LCD_ADDRESS, mode, cmd)
    time.sleep(0.0001)

def lcd_string(message, line):
    # Send the message to LCD
    lcd_byte(0x80 + line*0x40, LCD_CMD)
    for char in message:
        lcd_byte(ord(char), LCD_DATA)

# Initialize LCD
lcd_byte(0x33, LCD_CMD)
lcd_byte(0x32, LCD_CMD)
lcd_byte(0x06, LCD_CMD)
lcd_byte(0x0C, LCD_CMD)
lcd_byte(0x28, LCD_CMD)
lcd_byte(0x01, LCD_CMD)

try:
    # Display "royce" on LCD
    lcd_string("royce", 0)
    time.sleep(2)

except KeyboardInterrupt:
    pass
finally:
    # Cleanup
    lcd_byte(0x01, LCD_CMD)
    bus.close()
