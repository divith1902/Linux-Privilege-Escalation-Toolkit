import subprocess

def scan_world_writable():
    print("\n=== World-Writable File Scan ===")

    result = subprocess.getoutput("find / -type f -perm -0002 2>/dev/null")
    files = result.split("\n")

    for file in files[:20]:  # limit output
        print(file)

    print(f"\nTotal World-Writable Files: {len(files)}")