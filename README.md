# Honeypy: Modular SSH & HTTP Honeypot System

## 🛡️ Project Overview
Honeypy is a high-fidelity, low-interaction honeypot designed to emulate vulnerable services (SSH and HTTP) to capture and analyze unauthorized access attempts. This project serves as a proactive defense mechanism, providing real-time threat intelligence and mapping attacker behavior to the **MITRE ATT&CK Framework**.

## 📊 Key Features
* **SSH Deception:** A Paramiko-based SSH server that handles cryptographic handshakes and logs brute-force credential attempts.
* **Web Decoy:** A Flask-driven HTTP server presenting a fake WordPress administrative login to attract web-based automated scanners.
* **Interactive Dashboard:** A Plotly-Dash visualization suite that transforms raw `audits.log` data into actionable insights (IP distribution, login frequency, and success/fail ratios).
* **Persistent Identity:** Utilizes RSA server keys to maintain a consistent identity, preventing fingerprinting by sophisticated attackers.

## 🚀 Installation & Setup

### 1. Clone the Repository
###```bash
git clone https://github.com/sc23ade/honeypie.git
cd honeypie

Ensure you have python 3.x installed
pip install -r requirements.txt

To start Honeypot service:
py honeypy.py

To launch dashboard:
py dashboard.py
view the live status at http://127.0.0.1:8050

📁 Repository Structure
• honeypy.py - Main service orchestrator and entry point.
• ssh_honeypot.py - Logic for the SSH deception layer.
• web_honeypot.py - Logic for the Flask/WordPress decoy.
• dashboard.py - Data visualization and analytics engine.
• templates/ - Contains wp-admin.html for the web decoy.
• audits.log - Centralized forensic log file for all captured events.
• requirements.txt - Comprehensive list of necessary Python libraries.
⚖️ Ethical Disclaimer
This tool is for educational and authorized security research purposes only. Ensure compliance with local laws and organizational policies before deployment.
