from collections import defaultdict

log_file = "login_logs.txt"

failed_attempts = defaultdict(int)

with open(log_file, "r") as file:
    for line in file:
        ip, status = line.strip().split()

        if status == "FAILED":
            failed_attempts[ip] += 1

for ip, attempts in failed_attempts.items():
    if attempts >= 3:
        print(f"ALERT: Possible brute force attack from {ip}")
        print(f"Failed login attempts: {attempts}\n")