import time
import os

import requests
import schedule
from plyer import notification
from bs4 import BeautifulSoup

def clear_scrn():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# URLs for seat status
json_url = "https://usis-cdn.eniamza.com/old-usisdump.json"
usis_url = "https://usis.bracu.ac.bd/academia/admissionRequirement/getAvailableSeatStatus"

# Function to check for class availability in the JSON data
def check_class():
    global c_code, sec, url_selected

    try:
        print("Fetching results!!!\n")

        def print_details():
            print(f"Course Code: {course_code}")
            print(f"Program: {program}")
            print(f"Faculty: {faculty}")
            print(f"Section: {section}")
            print(f"Total Seat: {total_seat}")
            print(f"Seat Booked: {seat_booked}")
            print(f"Seat Remaining: {seat_remaining}")
            if seat_remaining > 0:
                print("Seats are available!")
                if os.name == "nt":
                    send_desktop_notification(seat_remaining) # Notify in Windows
                else:
                    send_termux_notification(seat_remaining)  # Notify in Termux
            else:
                print("No seats available at the moment.")
        
        if url_selected == 1:
            response = requests.get(json_url)
            response.raise_for_status()  # Raise an error if the request failed
            data = response.json() # Load JSON data

            # Iterate over the 'data' list in the JSON
            for course in data["data"]:
                course_code = course["courseCode"]
                section = course["courseDetails"].split("-")[1][1:-1]
                program = course["deptName"]
                faculty = course["empShortName"]
                total_seat = course["defaultSeatCapacity"]
                seat_booked = course["totalFillupSeat"]
                seat_remaining = course["availableSeat"]
                if seat_remaining == "":
                    seat_remaining = 0
                else:
                    seat_remaining = int(seat_remaining)
                # Check for the course and section you are interested in
                if course_code == c_code and section == sec:
                    print_details()
                    break  # Stop after finding the desired course
        else:
            # Fetch the page content
            response = requests.get(usis_url)
            response.raise_for_status()  # Check for request success
            # Parse the HTML content
            soup = BeautifulSoup(response.content, "html.parser")
            # Find the table with the course data
            table = soup.find("table", {"id": "customers"})
        
            # Iterate through each row (tr)
            for row in table.find_all("tr")[1:]:  # Skip the header
                cols = row.find_all("td")
                course_code = cols[1].text.strip()
                program = cols[2].text.strip()
                faculty = cols[3].text.strip()
                section = cols[5].text.strip()
                total_seat = int(cols[7].text.strip())
                seat_booked = int(cols[8].text.strip())
                seat_remaining = int(cols[9].text.strip())
                # Check for the course and section you are interested in
                if course_code == c_code and section == sec:
                    print_details()
                    break  # Stop after finding the desired course
    
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

print("\nWhich site would you like to choose to be updated from? :")
print("1. Eniamza's Usis2Global. Or,")
print("2. usis.bracu.ac.bd/academia/")
url_selected = int(input("(Enter 1 or 2): "))
while url_selected not in [1, 2]:
    url_selected = int(input("Please enter a valid option (1 or 2): "))

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