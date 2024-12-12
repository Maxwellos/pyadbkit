import asyncio
from pyadbkit import Client

async def main():
    client = Client()

    # List connected devices
    devices = await client.devices()
    print("Connected devices:")
    for device in devices:
        print(f"  {device['serial']} - {device.get('product', 'Unknown')}")

    if devices:
        # Use the first device for demonstration
        serial = devices[0]['serial']

        # Get device info
        info = await client.get_device_info(serial)
        print(f"\nDevice info for {serial}:")
        for key, value in info.items():
            print(f"  {key}: {value}")

        # Run a shell command
        print("\nRunning 'ls /sdcard' command:")
        result = await client.shell(serial, 'ls /sdcard')
        print(result)

        # Get battery level
        battery = await client.get_battery_level(serial)
        print(f"\nBattery level: {battery}%")

    else:
        print("No devices connected.")

if __name__ == "__main__":
    asyncio.run(main())