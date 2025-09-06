import time
import os
import subprocess
import requests
import logging
import json
import threading
import platform
import sys

HEADER = r"""
                    _ _     _           _   
 _ __   ___ _ __ __| | |__ | |_   _  __| |  
| '_ \ / _ \ '__/ _` | '_ \| | | | |/ _` |  
| | | |  __/ | | (_| | |_) | | |_| | (_| |_ 
|_| |_|\___|_|  \__,_|_.__/|_|\__,_|\__,_(_)
- made by a nerd, for nerds.
"""

CONFIG_FILE = "config.json"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------------
# Load or Create Config
# -------------------------
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        default_config = {
            "interval": 60,
            "loops": 1000
        }
        with open(CONFIG_FILE, "w") as f:
            json.dump(default_config, f, indent=4)
        return default_config

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)

# -------------------------
# Cross-platform Commands
# -------------------------
def start_tor_service():
    system = platform.system().lower()
    try:
        if "linux" in system or "darwin" in system:  
            subprocess.run(['sudo', 'service', 'tor', 'start'], check=True)
        elif "windows" in system:
            subprocess.run(['net', 'start', 'tor'], check=True, shell=True)
        else:
            logger.error("Unsupported OS.")
            sys.exit(1)
    except subprocess.CalledProcessError:
        logger.error("Failed to start Tor service.")
        sys.exit(1)

def reload_tor_service():
    system = platform.system().lower()
    try:
        if "linux" in system or "darwin" in system:
            subprocess.run(['sudo', 'service', 'tor', 'reload'], check=True)
        elif "windows" in system:
            subprocess.run(['net', 'stop', 'tor'], check=True, shell=True)
            subprocess.run(['net', 'start', 'tor'], check=True, shell=True)
        else:
            logger.error("Unsupported OS.")
    except subprocess.CalledProcessError as e:
        logger.error(f"Error reloading Tor service: {e}")

def stop_tor_service():
    system = platform.system().lower()
    try:
        if "linux" in system or "darwin" in system:
            subprocess.run(['sudo', 'service', 'tor', 'stop'], check=True)
        elif "windows" in system:
            subprocess.run(['net', 'stop', 'tor'], check=True, shell=True)
        else:
            logger.error("Unsupported OS.")
    except subprocess.CalledProcessError:
        logger.warning("Could not stop Tor service properly.")

# -------------------------
# IP Fetcher
# -------------------------
def get_external_ip():
    url = 'https://www.myexternalip.com/raw'
    try:
        response = requests.get(
            url,
            proxies={'http': 'socks5://127.0.0.1:9050', 'https': 'socks5://127.0.0.1:9050'},
            timeout=10
        )
        response.raise_for_status()
        return response.text.strip()
    except requests.RequestException as e:
        logger.error(f'Failed to get external IP: {e}')
        return None

# -------------------------
# Change IP in a Thread
# -------------------------
def change_ip():
    try:
        reload_tor_service()
        time.sleep(5)
        ip = get_external_ip()
        if ip:
            logger.info(f"Your IP has been changed to: {ip}")
        else:
            logger.warning("Failed to retrieve external IP")
    except Exception as e:
        logger.error(f"Unexpected error while changing IP: {e}")

def threaded_ip_change():
    thread = threading.Thread(target=change_ip)
    thread.start()

# -------------------------
# Main Function
# -------------------------
def main():
    print(HEADER)
    logger.info('Starting IP Changer Script...')

    config = load_config()

    try:
        x = int(input(f"[+] Time to change IP in seconds [default={config['interval']}] >> ") or config['interval'])
        lin = int(input(f"[+] How many times do you want to change your IP [default={config['loops']}], for infinite type [0] >> ") or config['loops'])
        config['interval'] = x
        config['loops'] = lin
        save_config(config)
    except ValueError:
        logger.error("Invalid input. Please enter a number.")
        exit(1)

    logger.info('Starting Tor service...')
    start_tor_service()

    try:
        count = 0
        while True:
            if lin > 0 and count >= lin:
                break
            time.sleep(x)
            threaded_ip_change()  
            count += 1
    except KeyboardInterrupt:
        logger.info('\nScript interrupted by user. Stopping...')
    finally:
        logger.info('Cleaning up...')
        stop_tor_service()

if __name__ == "__main__":
    main()
