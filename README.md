# Class Availability Checker

This Python script checks for seat availability in a specific class section from a university schedule website and sends a notification when seats are available. The script works on both desktop environments (Windows/Linux) and Android devices through the Termux terminal.

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
  - `termux-api` (for Android)

### Android (Termux)
- Termux terminal installed.
- Python installed in Termux (`pkg install python`).
- Termux API installed (`pkg install termux-api`).

## Installation and Setup

### 1. Clone the Repository
First, clone the repository from GitHub to your local machine:

```bash
git clone https://github.com/your-username/class-availability-checker.git
cd class-availability-checker
```

2. Install Dependencies
Install the necessary Python packages listed in requirements.txt:

For Desktop (Windows/Linux):
Create a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Linux
.\venv\Scripts\activate   # On Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
For Android (Termux):
Install Python:

bash
Copy code
pkg install python
Install Termux API:

bash
Copy code
pkg install termux-api
Install dependencies:

bash
Copy code
pip install requests schedule plyer
3. Set Up the Script
Edit the script to enter your course details. When prompted, enter the course code and section (e.g., CSE321, 03).

bash
Copy code
python script_name.py
4. Run the Script
For Desktop:
Run the script, and it will notify you through the system tray when a seat becomes available:

bash
Copy code
python script_name.py
For Android (Termux):
In Termux, simply run:

bash
Copy code
python script_name.py
When a seat becomes available, Termux will send you a notification through the Android system.

5. Customize Notifications
Desktop Notifications: You can customize the desktop notification by editing the send_desktop_notification function.
Android Notifications: Modify the send_termux_notification function to change the notification message or title.
Scheduled Check
The script checks for seat availability every minute. You can modify the frequency in the following line of code:

python
Copy code
schedule.every(1).minutes.do(check_class)
To adjust, change the number 1 to any number of minutes you prefer.

Issues and Contributing
Feel free to submit issues or contribute to this project via GitHub. All contributions are welcome!

License
This project is licensed under the MIT License - see the LICENSE file for details.
