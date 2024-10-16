# Class Availability Checker

This Python script checks for seat availability in real time for a specific class section from BRAC university USIS website and sends a notification to running device when seats are available. The script works on both desktop environments (Windows/Linux) and Android devices through the Termux terminal.

## Features
- Fetches real-time class schedule data from a JSON file.
- Checks seat availability for a specific course and section.
- Sends notifications:
  - Desktop notification (Windows/Linux).
  - Termux notification (Android).

## Requirements

### Desktop (Windows/Linux)
- Python 3.x
- Required libraries:
  - `requests`
  - `plyer`
  - `schedule`

### Android (Termux)
- Termux terminal installed.
- Python installed in Termux (`pkg install python`).
- Termux-API APK and Termux Package installed (`pkg install termux-api`).

## Installation and Setup

### 1. Clone the Repository
First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/ahshafin2315/AutoSeatCheckerUsis
cd AutoSeatCheckerUsis
```

### 2. Install dependencies:

```bash
pip install requests schedule plyer
```

For Android (Termux):
Install Python:
```bash
pkg install python
```
Install Termux API:
```bash
pkg install termux-api
```

### 3. Set Up & Run the Script
Run below code inside cloned script directory:

```bash
python script_name.py
```

When a seat becomes available, Desktop or Termux will send you a notification through the system.

## Scheduled Check
The script checks for seat availability every minute. You can modify the frequency in the following line of code:

```python
schedule.every(1).minutes.do(check_class)
```
To adjust, change the number 1 to any number of minutes you prefer.

## Issues and Contributing
Feel free to submit issues or contribute to this project via GitHub. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
