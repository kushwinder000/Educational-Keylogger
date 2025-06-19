# ⌨️ Educational Keylogger (Python)

A Python-based keylogger built **strictly for educational and ethical research purposes**. It captures keystrokes, screenshots, system info, and active application logs, and securely emails the data.

---

## 🚀 Features

- ✅ Captures all keystrokes
- ✅ Tracks active window/application
- ✅ Takes regular screenshots
- ✅ Collects system info (IP address, OS, hostname)
- ✅ Sends all logs to email every 5 seconds (configurable)

---

## ⚙️ Requirements

```bash
pip install -r requirements.txt
```

---

## 🔧 How to Use

### 1. **Set Up Email Credentials (Securely)**

Before running, create environment variables:

#### 🔹 Windows (CMD):
```bash
set SENDER_EMAIL=youremail@gmail.com
set EMAIL_APP_PASSWORD=yourapppassword
```

#### 🔹 Linux/macOS:
```bash
export SENDER_EMAIL=youremail@gmail.com
export EMAIL_APP_PASSWORD=yourapppassword
```

> Optionally, you can use a `.env` file and the `python-dotenv` package to manage credentials.

---

### 2. **Run the Script**
```bash
python keylogger.py
```

The script will:
- Start capturing keystrokes and screenshots
- Store data in local files (`document.txt`, `screenshot.png`, etc.)
- Email logs every 5 seconds

---

## 📂 Output Files

| File               | Purpose                        |
|--------------------|-------------------------------|
| `document.txt`     | All recorded keystrokes        |
| `applicationLog.txt` | Window/app tracking log     |
| `syseminfo.txt`    | System information             |
| `screenshot.png`   | Screenshot of current screen   |

---

## 🔐 Note on Security

Your Gmail must allow **App Passwords**. If using 2FA, create an app-specific password from your Google Account settings.

---

## ⚠️ Disclaimer

> This project is developed **only for educational and ethical testing**. Do not run it on any system you do not own or have explicit permission to monitor. Unauthorized use may violate laws and can result in legal consequences.

---

## 📫 Author

Made with 💻 by [Kushwinder Dadwal](https://www.linkedin.com/in/kushwinder-dadwal-a35465208)
