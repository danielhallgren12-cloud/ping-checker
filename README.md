# Ping Checker

A simple Python script that pings a list of IP addresses and reports which ones respond.

## Features (v1.0)

- Hardcoded list of IP addresses
- Sends one ping per address using `subprocess.run()`
- Prints response status to the console
- Counts and displays how many hosts responded

## How to Run

1. Make sure you have Python 3 installed.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python ping_checker.py

## Example output

Pinging 192.168.1.1...
192.168.1.1 responded ✅
Pinging 8.8.8.8...
8.8.8.8 responded ✅
Pinging 192.168.1.10...
192.168.1.10 did not respond ❌

2 out of 3 IP addresses responded.

## Planned for v2.0

* Accept IPs via user input
* Add timestamps to each result
* Log results to a file (log.txt)

## Files

* ping_checker.py
* .gitignore

## Author

Created by Daniel Hallgren
danielhallgren12@gmail.com