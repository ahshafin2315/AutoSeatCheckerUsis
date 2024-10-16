import time
import os

import requests
import schedule
from plyer import notification

def clear_scrn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# URL for the JSON file
json_url = "https://usis-cdn.eniamza.com/old-usisdump.json"

# Function to check for class availability in the JSON data
def check_class():
    global c_code, sec
    try:
        print("Fetching results!!!\n")
        response = requests.get(json_url)
        response.raise_for_status()  # Raise an error if the request failed
        
        data = response.json()  # Load JSON data

        # Iterate over the 'data' list in the JSON
        for course in data["data"]:
            course_code = course["courseCode"]
            section_details = course["courseDetails"]
            seat_cap = course["defaultSeatCapacity"]
            booked = course["totalFillupSeat"]
            available_seat = course["availableSeat"]
            if available_seat == "":
                available_seat = 0
            else:
                available_seat = int(available_seat)

            # Check for specific course and section (CSE321-[03])
            if course_code == c_code and section_details == f"{c_code}-[{sec}]":
                print(f"Course Code: {course_code}")
                print(f"Section: {section_details}")
                print(f"Seat Capacity: {seat_cap}")
                print(f"Booked: {booked}")
                print(f"Available: {available_seat}")

                # If available seats are more than 0, send a notification
                if available_seat > 0:
                    if os.name == "nt":
                        send_desktop_notification(available_seat) # Notify in Windows
                    else:
                        send_termux_notification(available_seat)  # Notify in Termux
                else:
                    print("No seats available at the moment.")
                break  # Break after finding the section you're interested in
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send desktop notification using Plyer
def send_desktop_notification(available_seat):
    notification.notify(
        title=f"{c_code} Section {sec} Slot Available!",
        message=f"A seat is now available for {c_code}, Section {sec}. Available seats: {available_seat}",
        timeout=10  # Notification will last for 10 seconds
    )
    print("Desktop notification sent!")

# Function to send notification via Termux
def send_termux_notification(available_seat):
    os.system(f'termux-notification --title "{c_code} Section {sec} Slot Available!" --content "Available seats: {available_seat}"')
    print("Termux notification sent!")

c_code = input("Enter Course Code: ").upper()
sec = input("Enter Section: ")
if len(sec) == 1:
    sec = '0' + sec

schedule.every(1).minutes.do(check_class)
check_class()

# Keep the script running
while True:
    print("="*40)
    print("Waiting for 1 minute!!")
    print("="*40)
    time.sleep(60)
    clear_scrn()
    schedule.run_pending()