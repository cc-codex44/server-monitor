import os
import platform
import shutil
import time
from datetime import datetime

import psutil


def progress_bar(value, width=24):
    value = max(0, min(100, value))
    filled = int(width * value / 100)
    return "█" * filled + "░" * (width - filled)


def get_temperature():
    try:
        temperatures = psutil.sensors_temperatures()
        for sensors in temperatures.values():
            for sensor in sensors:
                if sensor.current is not None:
                    return f"{sensor.current:.1f}°C"
    except (AttributeError, OSError):
        pass
    return "N/A"


def get_disk_info():
    disk = shutil.disk_usage(os.path.abspath(os.sep))
    return disk.used / disk.total * 100, disk.used / 1024**3, disk.total / 1024**3


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def draw_dashboard():
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk_percent, disk_used, disk_total = get_disk_info()
    temperature = get_temperature()
    net = psutil.net_io_counters()

    clear_screen()
    print("╔" + "═" * 56 + "╗")
    print("║" + " " * 18 + "SERVER MONITOR" + " " * 24 + "║")
    print("╠" + "═" * 56 + "╣")
    print(f"║ Host: {platform.node():<48} ║")
    print(f"║ OS:   {platform.system()} {platform.release():<44} ║")
    print(f"║ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S'):<48} ║")
    print("╠" + "═" * 56 + "╣")
    print(f"║ CPU      {progress_bar(cpu)}  {cpu:5.1f}%{' ' * 12}║")
    print(f"║ RAM      {progress_bar(memory.percent)}  {memory.percent:5.1f}%{' ' * 12}║")
    print(f"║ DISK     {progress_bar(disk_percent)}  {disk_percent:5.1f}%{' ' * 12}║")
    print(f"║ TEMP     {temperature:<47}║")
    print("╠" + "═" * 56 + "╣")
    print("║ STORAGE")
    print(f"║ Used:    {disk_used:,.1f} GB")
    print(f"║ Total:   {disk_total:,.1f} GB")
    print("╠" + "═" * 56 + "╣")
    print("║ NETWORK")
    print(f"║ Received: {net.bytes_recv / 1024**3:,.2f} GB")
    print(f"║ Sent:     {net.bytes_sent / 1024**3:,.2f} GB")
    print("╠" + "═" * 56 + "╣")
    print("║ Refreshing every 2 seconds...  Press Ctrl+C to exit.")
    print("╚" + "═" * 56 + "╝")


try:
    while True:
        draw_dashboard()
        time.sleep(2)
except KeyboardInterrupt:
    clear_screen()
    print("Server Monitor stopped.")
