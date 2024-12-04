from machine import Pin, UART
import time
import asyncio
from lib.dfplayer import DFPlayer

# Set up UART communication
uart = UART(2, baudrate=9600, tx=17, rx=16)  # TX=17, RX=16

# Optionally, use the BUSY pin
busy_pin = Pin(15, Pin.IN)  # GPIO 15, change if necessary

# Initialize DFPlayer Mini
df = DFPlayer(2)
df.init(tx=17, rx=16)

async def main():
    print("Bíð eftir að DFPlayer byrji...")
    await df.wait_available()  # Wait until DFPlayer is ready
    print("DFPlayer tilbúinn!")

    await df.volume(15)  # Set volume level
    print("Stillti hljóðstyrk á 15")

    print("Spila skrá 001.mp3 úr möppu 01...")
    await df.play(1, 2)  # Play 001.mp3 from folder 01

    # Monitor the BUSY pin
    while True:
        if busy_pin.value() == 0:  # If BUSY is low, audio is playing
            print("Audio is playing...")
        else:
            print("DFPlayer is idle.")
        await asyncio.sleep(1)

# Run the asyncio main loop
asyncio.run(main())
