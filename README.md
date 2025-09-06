
---

# 🕵️ IP Changer using Tor

This Python script allows you to **automatically change your external IP address at regular intervals using Tor**. It uses the Tor network to route your traffic through different nodes, ensuring anonymity.

---

## ✅ Features

* Automatically installs required packages:

  * **python3-pip**
  * **tor**
  * **requests**
  * **torsocks**
* Starts the Tor service and changes IP at a given time interval.
* Fetches your **current external IP** after each change.
* Works on **Linux systems with apt package manager**.
* **Customizable options**:

  * Interval time between IP changes.
  * Number of times to change IP (or infinite).

---

## 📌 Requirements

* **Python 3**
* **Linux system with `apt` package manager**
* **Root access (sudo privileges)**

---

## 🔍 How It Works

1. Installs all necessary packages if not installed.
2. Starts the **Tor service**.
3. Uses **SOCKS5 proxy (127.0.0.1:9050)** to fetch the external IP.
4. Changes IP by reloading the **Tor service**.
5. Repeats this process based on user input.

---

## ▶️ Usage

### **1. Clone the Repository**

```bash
git clone https://github.com/nerdblud/ip-changer-tor.git
cd ip-changer-tor
```

### **2. Run the Script**

```bash
python3 ip_changer.py
```

### **3. Provide Inputs**

* **Time interval in seconds** (default: 60)
* **Number of times to change IP**

  * Default: 1000
  * Enter `0` for infinite loop.

---

## 🖼️ Example

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

## ⚠️ Disclaimer

This tool is intended for **educational and privacy purposes only**.
Do **NOT** use it for any illegal activities. You are responsible for how you use this script.

---

## 🔐 Important Notes

* You need **Tor installed and running**.
* Script uses **sudo commands**, so you may need to enter your password.
* Changing IP frequently might cause **Tor nodes to block you** temporarily.

---