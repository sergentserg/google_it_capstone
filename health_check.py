import socket
import shutil
import psutil

import emails


DISK_MIN = 20
CPU_MAX = 80
# 500 MB.
MEMORY_MIN = 500 * 1024 * 1024


def check_disk_usage():
    du = shutil.disk_usage("/")
    free = (du.free / du.total) * 100
    return free > DISK_MIN


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < CPU_MAX


def check_available_memory():
    memory = psutil.virtual_memory()
    return memory.available > MEMORY_MIN


def check_localhost():
    localhost = socket.gethostbyname("localhost")
    return localhost == "127.0.0.1"


if __name__ == '__main__':
    checks = [
        (check_disk_usage, "Error - CPU usage is over 80%"),
        (check_cpu_usage, "Error - Available disk space is less than 20%"),
        (check_available_memory, "Error - Available memory is less than 500MB"),
        (check_localhost, "Error - localhost cannot be resolved to 127.0.0.1")
    ]

    error_messages = []
    for check, message in checks:
        if not check():
            error_messages.append(message)

    for message in error_messages:
        error_email = emails.generate_email(
            sender="automation@example.com",
            recipient="username@example.com",
            subject=message,
            body="Please check your system and resolve the issue as soon as possible!")

        emails.send_email(error_email)
