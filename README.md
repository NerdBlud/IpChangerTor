# IP Changer using Tor

This Python script automatically changes your external IP address at regular intervals using the Tor network. It routes traffic through Tor nodes to provide basic IP rotation and network anonymity.

---

## Features

* Automatically installs required packages:

  * python3-pip
  * tor
  * requests
  * torsocks
* Starts the Tor service and changes IP at a specified interval
* Retrieves and displays the current external IP after each change
* Designed for Linux systems using the apt package manager
* Customizable options:

  * Time interval between IP changes
  * Number of IP changes or continuous mode

---

## Requirements

* Python 3
* Linux system with apt package manager
* Root access (sudo privileges)

---

## How It Works

1. Installs required dependencies if they are not already installed
2. Starts the Tor service
3. Uses a SOCKS5 proxy (127.0.0.1:9050) to fetch the external IP
4. Reloads the Tor service to obtain a new exit node and IP address
5. Repeats the process based on user-defined settings

---

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/nerdblud/IpChangerTor.git
cd IpChangerTor
```

### 2. Run the Script

```bash
python3 ip_changer.py
```

### 3. Provide Inputs

* Time interval in seconds (default: 60)
* Number of times to change IP

  * Default: 1000
  * Enter 0 for continuous execution

---

## Example Output

```
                    _ _     _           _   
 _ __   ___ _ __ __| | |__ | |_   _  __| |  
| '_ \ / _ \ '__/ _` | '_ \| | | | |/ _` |  
| | | |  __/ | | (_| | |_) | | |_| | (_| |_ 
|_| |_|\___|_|  \__,_|_.__/|_|\__,_|\__,_(_)
- made by a nerd, for nerds.

[+] Time to change IP in seconds [default=60] >> 60
[+] How many times do you want to change your IP [default=1000], for infinite type [0] >> 10
```

---

## Disclaimer

This tool is intended for educational and privacy-related purposes only.
Do not use this software for illegal activities. You are responsible for complying with all applicable laws and policies.

---

## Important Notes

* Tor must be installed and running on the system
* The script uses sudo commands and may require password entry
* Changing IP addresses frequently may result in temporary restrictions from some Tor exit nodes

---
