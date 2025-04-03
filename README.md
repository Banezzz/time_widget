# Crypto Time Widget

A professional desktop widget for cryptocurrency traders to monitor global market hours across major trading hubs. Built with Python, this tool provides real-time clock display with UTC offsets for all major cryptocurrency trading centers.

## Features

- Real-time clock display for major crypto trading hubs
- Always-on-top window for constant visibility
- Draggable interface for flexible positioning
- Modern dark theme UI optimized for extended trading sessions
- UTC offset display for each time zone
- Comprehensive coverage of global markets:
  - Local Time
  - UTC (Global Reference)
  - Seoul (Korean Market)
  - Tokyo (Asian Market Open)
  - Hong Kong (Asian Trading Hub)
  - Singapore (Asian Crypto Hub)
  - London (European Market Open)
  - Berlin (EU Trading Hub)
  - New York (US Market Open)
  - Chicago (CME Bitcoin Futures)
  - San Francisco (Coinbase HQ)

## Installation

### Binary Installation
1. Download the latest release from [Releases](https://github.com/Banezzz/time_widget/releases)
2. Extract time_widget.zip
3. Run crypto_time_widget.exe

### Source Installation
```bash
git clone https://github.com/Banezzz/time_widget.git
cd time_widget
pip install -r requirements.txt
python main.py
```

## Technical Details

### Requirements
- Python 3.12+
- pytz
- tkinter (included with Python)

### Development Setup
```bash
pip install pyinstaller
pyinstaller --onefile --windowed main.py
```

### Architecture
- Built with Python's tkinter for lightweight GUI
- Uses pytz for accurate timezone handling
- Real-time updates with 1-second precision
- Minimal system resource usage
- No external dependencies beyond Python standard library and pytz

## Usage

The widget displays:
- Time zone name and market significance
- UTC offset for each location
- Current time in HH:MM:SS format
- Current date in YYYY-MM-DD format

The window can be:
- Dragged to any screen position
- Kept on top of other windows
- Closed via the integrated close button

## License
[MIT License](LICENSE)

## Contributing
Contributions are welcome. Please follow these steps:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Contact
- GitHub: [@Banezzz](https://github.com/Banezzz)

---
Developed for cryptocurrency traders who need precise global market time tracking 