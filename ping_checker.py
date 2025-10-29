# Multiple ip ping checker.
import subprocess

ip_list = ["45.33.32.156", "8.8.8.8", "8.8.4.4"] #Scanme, Google.

success_count = 0

for ip in ip_list:
    print(f"Pinging {ip}...")
    result = subprocess.run(["ping", "-n", "1", ip], capture_output=True, text=True)
    if result.returncode == 0:
        print(f"{ip} answered")
        success_count += 1
    else:
        print(f"{ip} didnt answer")

print(f"\nTotal succeded answers {success_count} of {len(ip_list)} IP-addresses.")