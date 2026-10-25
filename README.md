# Server Monitor

A terminal dashboard for CPU, memory, system drive, temperature, network totals, host, and time. It refreshes every 2 seconds.

## Download

Use **Code → Download ZIP** on [GitHub](https://github.com/cc-codex44/server-monitor), then extract it; or clone it:

```bash
git clone https://github.com/cc-codex44/server-monitor.git
cd server-monitor
```

If you downloaded a ZIP, open a terminal in the extracted `server-monitor` folder instead.

## Install and run

Requires Python 3.10 or newer on Windows, Linux, or macOS.

```bash
python -m pip install -r requirements.txt
python server_monitor.py
```

Press `Ctrl+C` to stop. For one snapshot without refreshing, run `python server_monitor.py --once`. On systems where Python is called `python3`, replace `python` with `python3` in these commands.

Temperature shows `N/A` when the OS or hardware does not expose a sensor. Disk usage is for the system drive; network totals are cumulative counters since boot. The display uses ASCII when the terminal cannot print box-drawing characters.
