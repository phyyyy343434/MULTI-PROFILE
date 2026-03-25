# ChatGPT Profile Launcher

This is a Python-based automation tool to concurrently launch multiple Chrome profiles, navigate them to ChatGPT, and automatically handle the initial login/signup popup.

## Tech Stack
- **Language**: Python 3.8+
- **Automation**: Playwright
- **OS**: Windows

---

## 1. Step-by-Step Setup Guide

### Step 1: Install Python
Ensure you have Python 3.8 or newer installed. You can download it from [python.org](https://www.python.org/downloads/). Make sure to check the box that says "Add Python to PATH" during installation.

### Step 2: Install Required Libraries
Open a command prompt (cmd) or PowerShell and run the following commands to install Playwright and its dependencies:

```sh
pip install playwright
```

### Step 3: Install Browsers for Playwright
Playwright needs its own browser instances. This command will download a compatible version of Chromium (which we will use to run your Chrome profiles).

```sh
playwright install chromium
```

---

## 2. Configuration

The application is controlled by the `config.json` file.

### Step 1: Find Your Chrome User Data Directory
This is the most important step. This folder contains all your Chrome profiles, cookies, and settings.

1.  Open Chrome.
2.  Navigate to the URL `chrome://version`.
3.  Look for the **"Profile Path"** field.
4.  Copy the entire path, but **remove** the last part (e.g., `\Default` or `\Profile 1`) to get the parent `User Data` directory.

It will typically be: `C:\Users\<YourUsername>\AppData\Local\Google\Chrome\User Data`

### Step 2: Edit `config.json`
Open the `config.json` file and make the following changes:

```json
{
  "chrome_user_data_dir": "C:\\Users\\YourUsername\\AppData\\Local\\Google\\Chrome\\User Data",
  "profiles": [
    "Default",
    "Profile 1",
    "Profile 2"
  ],
  "start_url": "https://chatgpt.com",
  "run_headless": false
}
```

- **`chrome_user_data_dir`**: Paste the `User Data` path you copied. **Important**: Use double backslashes (`\\`) for the path in JSON.
- **`profiles`**: List the folder names of the Chrome profiles you want to launch. These are the folders inside the `User Data` directory (e.g., `Default`, `Profile 1`, `Profile 2`).
- **`start_url`**: The URL to navigate to. Defaults to ChatGPT.
- **`run_headless`**: Set to `true` to run browsers invisibly in the background. Set to `false` to watch them work.

---

## 3. How to Run

Once configured, simply open a command prompt or PowerShell in the project folder and run:

```sh
python main.py
```

The script will then launch and automate a browser for each profile listed in your config.

---

## 4. Explanation of Popup Detection Logic

The previous method relied on screen coordinates or image matching, which is unreliable. This application uses Playwright's modern locator API for precision.

The core logic is in the `automation.py` file:

```python
# This line creates a "locator" for the button.
# It tells Playwright to find an element that is a "button" and has the exact name "Stay logged out".
logout_button = page.get_by_role("button", name="Stay logged out")

# This line waits for up to 5 seconds for the button to appear and then clicks it.
# If it doesn't appear, it will time out and report an error for that profile,
# but it won't crash the whole application.
await logout_button.click(timeout=5000)
```

This approach is superior because:
- **It's not a guess**: It directly asks the browser for the button based on its accessibility properties.
- **It's resilient**: It will work even if the button's color, size, or position on the page changes.
- **It has a built-in wait**: It automatically waits for the element to exist before trying to interact with it, eliminating timing issues.

```
