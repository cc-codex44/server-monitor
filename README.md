# 🖥️ Server Monitor

A lightweight Python terminal dashboard for monitoring a home server.

## 📊 What it shows

- CPU usage
- RAM usage
- Disk usage and free space
- Temperature when supported
- Network traffic
- Operating system and hostname
- Current time
- Automatic refresh every 2 seconds

## 🛠️ Requirements

- Python 3.10+
- `psutil`
- Windows, Linux or macOS

## 🚀 Installation

```bash
git clone https://github.com/YOUR_USERNAME/server-monitor.git
cd server-monitor
pip install -r requirements.txt
python server_monitor.py
```

On Linux you may need:

```bash
python3 server_monitor.py
```

## 📁 Project structure

```text
server-monitor/
├── server_monitor.py
├── requirements.txt
└── README.md
```

## 🔮 Roadmap

- [x] CPU monitoring
- [x] RAM monitoring
- [x] Disk monitoring
- [x] Network statistics
- [x] Automatic refresh
- [ ] Individual disk monitoring
- [ ] Docker container monitoring
- [ ] Web interface
- [ ] Historical graphs
- [ ] Alerts
