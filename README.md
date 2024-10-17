# Class Availability Checker

This Python script checks for seat availability in real time for a specific course section from either the [BRAC University USIS](https://usis.bracu.ac.bd/academia/admissionRequirement/getAvailableSeatStatus) website or [Eniamza's Usis2Global](https://github.com/Eniamza/usis2global) and sends a notification to running device when seats are available. The script works on both desktop environments (Windows/Linux) and Android devices through the Termux terminal.

## Features
- Fetches real-time class schedule data from a JSON file.
- Checks seat availability for a specific course and section.
- Option to choose seat update from which site preferred.
- Sends notifications:
  - Desktop notification (Windows/Linux).
  - Termux notification (Android).

## Requirements

### Desktop (Windows/Linux)
  - [Python](https://www.python.org/downloads/) 3.x

### Android (Termux)
  - [Termux](https://github.com/termux/termux-app) terminal installed.
  - Python installed in Termux (`pkg install python`).
  - [Termux-API](https://github.com/termux/termux-api) APK and Termux Package installed (`pkg install termux-api`).

### Required Python libraries:
  - `requests`
  - `plyer`
  - `schedule`
  - `bs4`

## Installation and Setup

### 1. Clone the Repository
First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/ahshafin2315/AutoSeatCheckerUsis
cd AutoSeatCheckerUsis
```
or, just download the `usis_seatCheck.py` script and store in desired location

### 2. Install dependencies:

For Android (Termux):
Install Python:
```bash
pkg install python
```
Install Termux API:
```bash
pkg install termux-api
```
For all platforms (must):
```bash
pip install requests schedule plyer bs4
```

### 3. Set Up & Run the Script
Run below code inside cloned script directory:

```bash
python usis_seatCheck.py
```
Set your desired inputs in the prompts and choose the site you wish to get updated from.
When a seat becomes available, Desktop or Termux will send you a notification through the system.

## Scheduled Check
The script checks for seat availability every minute. You can modify the frequency in the following line of code:

```python
schedule.every(1).minutes.do(check_class)
```
To adjust, change the number 1 to any number of minutes you prefer.

## Issues and Contributing
Feel free to submit issues or contribute to this project via GitHub. All contributions are welcome!

## Disclaimer 
Unfortunately, the usisdump of Eniamza has stopped updating due to data freeze in main USIS database or something (I donno :3). For now, the main USIS site seems to be most updated. So, sorry for the inconvenience if the script data won't update as expected 🥲.

## Credit
Huge Thanks to [Eniamza](https://github.com/Eniamza/) and his [USIS-CDN](https://usis-cdn.eniamza.com/old-usisdump.json) dump file for my data pulling.

## License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.
