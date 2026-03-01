from system_info import get_system_info
from suid_scan import scan_suid
from permission_scan import scan_world_writable

def main():
    print("Linux Privilege Escalation Automation Toolkit\n")

    get_system_info()
    scan_suid()
    scan_world_writable()

if __name__ == "__main__":
    main()