import os
import subprocess

def get_system_info():
    print("\n=== System Information ===")

    user = os.getenv("USER")
    print(f"Current User: {user}")

    groups = subprocess.getoutput("groups")
    print(f"Groups: {groups}")

    kernel = subprocess.getoutput("uname -a")
    print(f"Kernel Version: {kernel}")