import argparse
import os
import platform
import shutil
import sys
import time
from datetime import datetime

import psutil


def glyphs():
    try:
        "╔═╗║╠╣╚╝█░°".encode(sys.stdout.encoding or "utf-8")
        return "╔", "═", "╗", "║", "╠", "╣", "╚", "╝", "█", "░", "°C"
    except (UnicodeEncodeError, LookupError):
        return "+", "-", "+", "|", "+", "+", "+", "+", "#", ".", "C"


def temperature(unit):
    try:
        for entries in psutil.sensors_temperatures().values():
            for entry in entries:
                if entry.current is not None:
                    return f"{entry.current:.1f}{unit}" if unit == "°C" else f"{entry.current:.1f} C"
    except (AttributeError, OSError):
        pass
    return "N/A"


def draw_dashboard(once=False):
    tl, h, tr, v, ml, mr, bl, br, full, empty, unit = glyphs()
    width = 56

    def border(left, right):
        print(left + h * width + right)

    def row(value):
        print(v + " " + value[: width - 2].ljust(width - 2) + " " + v)

    def bar(label, value):
        value = max(0, min(100, value))
        filled = int(24 * value / 100)
        row(f"{label:<5} {full * filled}{empty * (24 - filled)} {value:5.1f}%")

    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory()
    disk = shutil.disk_usage(os.path.abspath(os.sep))
    net = psutil.net_io_counters()

    if sys.stdout.isatty() and not once:
        os.system("cls" if os.name == "nt" else "clear")
    border(tl, tr)
    row("SERVER MONITOR")
    border(ml, mr)
    row(f"Host: {platform.node()}")
    row(f"OS:   {platform.system()} {platform.release()}")
    row(f"Time: {datetime.now():%Y-%m-%d %H:%M:%S}")
    border(ml, mr)
    bar("CPU", cpu)
    bar("RAM", memory.percent)
    bar("DISK", disk.used / disk.total * 100)
    row(f"TEMP  {temperature(unit)}")
    border(ml, mr)
    row("STORAGE (system drive)")
    row(f"Used:  {disk.used / 1024**3:,.1f} GB")
    row(f"Total: {disk.total / 1024**3:,.1f} GB")
    border(ml, mr)
    row("NETWORK (total since boot)")
    row(f"Received: {net.bytes_recv / 1024**3:,.2f} GB")
    row(f"Sent:     {net.bytes_sent / 1024**3:,.2f} GB")
    border(ml, mr)
    row("Snapshot" if once else "Refresh: 2 seconds  |  Press Ctrl+C to exit")
    border(bl, br)


def main():
    parser = argparse.ArgumentParser(description="Terminal dashboard for server health")
    parser.add_argument("--once", action="store_true", help="print one snapshot and exit")
    args = parser.parse_args()
    try:
        while True:
            draw_dashboard(once=args.once)
            if args.once:
                return
            time.sleep(2)
    except KeyboardInterrupt:
        print("\nServer Monitor stopped.")


if __name__ == "__main__":
    main()
