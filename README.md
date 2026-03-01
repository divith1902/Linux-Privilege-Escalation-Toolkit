# Linux-Privilege-Escalation-Toolkit
A Python-based Linux enumeration toolkit for detecting privilege escalation vulnerabilities.
🐧 Linux Privilege Escalation Automation Toolkit

A Python-based automated Linux enumeration toolkit designed to identify potential privilege escalation misconfigurations in Linux systems.

This tool performs safe security auditing and does not exploit vulnerabilities. It is intended for educational and ethical security testing purposes only.

📌 Project Overview

Privilege escalation is a critical phase in post-exploitation attacks. Misconfigured permissions, insecure SUID binaries, weak sudo policies, and outdated kernels can allow attackers to gain elevated privileges.

This toolkit automates the detection of common Linux privilege escalation vectors.

🚀 Features

System Information Collection

SUID Binary Detection

World-Writable File Identification

Kernel Version Extraction

Privilege Escalation Risk Enumeration

Modular Python-Based Architecture

🧠 Security Checks Implemented
🔹 System Information

Current user

User groups

Kernel version

🔹 SUID Binary Scan

Detects binaries with SUID bit enabled:

find / -perm -4000 -type f

SUID binaries may allow privilege abuse if misconfigured.

🔹 World-Writable File Scan

Identifies files writable by all users:

find / -type f -perm -0002

World-writable files may allow attackers to inject malicious content.

🔹 Kernel Information

Extracts kernel version for vulnerability assessment:

uname -a
🛠 Technologies Used

Python 3

Kali Linux

Linux Command-Line Utilities

VirtualBox (Lab Environment)

📂 Project Structure
PROJECT_6_LINUX_PRIVESC/
│
├── main.py
├── system_info.py
├── suid_scan.py
├── permission_scan.py
└── README.md
▶ How to Run

Clone the repository:

git clone https://github.com/yourusername/Linux-Privilege-Escalation-Toolkit.git

Navigate into the directory:

cd Linux-Privilege-Escalation-Toolkit

Run the toolkit:

python3 main.py
🎯 Learning Outcomes

Understanding Linux privilege escalation vectors

Practical SUID/permission auditing

Linux enumeration techniques

Red-team post-exploitation concepts

Blue-team system auditing practices

⚠ Disclaimer

This project is developed for educational and ethical security research purposes only. Do not use this tool on systems without proper authorization.
