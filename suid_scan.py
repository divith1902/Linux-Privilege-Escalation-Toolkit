import subprocess

def scan_suid():
    print("\n=== SUID Binary Scan ===")

    result = subprocess.getoutput("find / -perm -4000 -type f 2>/dev/null")
    suid_files = result.split("\n")

    for file in suid_files[:20]:  # limit output
        print(file)

    print(f"\nTotal SUID Binaries Found: {len(suid_files)}")
    