# AI BATCH AGENT - COMPLETE SINGLE FILE
# No separate pip installation needed

import sys
import os
import json
import subprocess
import time
import ctypes
from datetime import datetime

# ================================================
# CHECK PYTHON VERSION
# ================================================
def check_python_version():
    """Check if Python is properly installed"""
    try:
        version = sys.version_info
        print(f"Python {version.major}.{version.minor}.{version.micro} detected")
        return True
    except:
        print("Python not detected properly!")
        return False

# ================================================
# PLATFORM DETECTION
# ================================================
IS_WINDOWS = sys.platform == "win32"

if IS_WINDOWS:
    try:
        user32 = ctypes.windll.user32
        WM_CLOSE = 0x0010
    except:
        IS_WINDOWS = False
        user32 = None
        WM_CLOSE = None
else:
    user32 = None
    WM_CLOSE = None

# ================================================
# SIMPLE GUI WITHOUT PYDEPENDENCIES
# ================================================
class SimpleApp:
    def __init__(self):
        self.profiles = {}
        self.browser_path = ""
        self.email = ""
        self.password = ""
        
    def run(self):
        """Simple text-based interface"""
        print("\n" + "="*60)
        print("AI BATCH AGENT - SIMPLE VERSION")
        print("="*60)
        
        self.load_config()
        
        while True:
            print("\n" + "="*60)
            print("MAIN MENU")
            print("="*60)
            print("1. Set Browser Path")
            print("2. Scan Browser Profiles")
            print("3. Set Login Credentials")
            print("4. Launch Profiles")
            print("5. Launch & Auto Login")
            print("6. Arrange Windows")
            print("7. Close All Windows")
            print("8. Exit")
            print("-"*60)
            
            choice = input("Enter choice (1-8): ").strip()
            
            if choice == "1":
                self.set_browser()
            elif choice == "2":
                self.scan_profiles()
            elif choice == "3":
                self.set_credentials()
            elif choice == "4":
                self.launch_profiles()
            elif choice == "5":
                self.launch_and_login()
            elif choice == "6":
                self.arrange_windows()
            elif choice == "7":
                self.close_windows()
            elif choice == "8":
                self.save_config()
                print("Goodbye!")
                break
            else:
                print("Invalid choice!")
    
    def load_config(self):
        """Load configuration"""
        try:
            if os.path.exists("simple_config.json"):
                with open("simple_config.json", "r") as f:
                    config = json.load(f)
                    self.browser_path = config.get("browser_path", "")
                    self.email = config.get("email", "")
                    self.password = config.get("password", "")
                    print("Configuration loaded")
        except:
            pass
    
    def save_config(self):
        """Save configuration"""
        try:
            config = {
                "browser_path": self.browser_path,
                "email": self.email,
                "password": self.password
            }
            with open("simple_config.json", "w") as f:
                json.dump(config, f, indent=2)
            print("Configuration saved")
        except:
            pass
    
    def set_browser(self):
        """Set browser path"""
        print("\nCurrent browser path:", self.browser_path)
        print("\nAuto-detecting browsers...")
        
        # Auto-detect browsers
        if IS_WINDOWS:
            possible = [
                r"C:\Program Files\Google\Chrome\Application\chrome.exe",
                r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
                os.path.expanduser(r"~\AppData\Local\Google\Chrome\Application\chrome.exe"),
                r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            ]
            
            found = []
            for path in possible:
                if os.path.exists(path):
                    found.append(path)
                    print(f"Found: {path}")
            
            if found:
                print("\nSelect a browser:")
                for i, path in enumerate(found, 1):
                    print(f"{i}. {os.path.basename(path)}")
                
                choice = input(f"Enter number (1-{len(found)}): ").strip()
                try:
                    idx = int(choice) - 1
                    if 0 <= idx < len(found):
                        self.browser_path = found[idx]
                        print(f"Browser set to: {self.browser_path}")
                        self.save_config()
                except:
                    print("Invalid choice")
            else:
                print("No browsers found automatically")
                path = input("Enter browser path manually: ").strip()
                if os.path.exists(path):
                    self.browser_path = path
                    self.save_config()
                else:
                    print("File does not exist!")
        else:
            path = input("Enter browser path: ").strip()
            if os.path.exists(path):
                self.browser_path = path
                self.save_config()
            else:
                print("File does not exist!")
    
    def scan_profiles(self):
        """Scan browser profiles"""
        if not self.browser_path:
            print("Please set browser path first!")
            return
        
        self.profiles = {}
        
        try:
            if IS_WINDOWS:
                chrome_path = os.path.join(os.path.expanduser("~"), "AppData", "Local", "Google", "Chrome", "User Data")
                if os.path.exists(chrome_path):
                    self.profiles["Default"] = "Default Profile"
                    
                    for item in os.listdir(chrome_path):
                        item_path = os.path.join(chrome_path, item)
                        if os.path.isdir(item_path) and item.startswith("Profile"):
                            self.profiles[item] = f"Profile {item.replace('Profile ', '')}"
            
            if not self.profiles:
                self.profiles = {
                    "Default": "Default Profile",
                    "Profile1": "Profile 1",
                    "Profile2": "Profile 2",
                }
            
            print(f"\nFound {len(self.profiles)} profiles:")
            for i, (pid, pname) in enumerate(self.profiles.items(), 1):
                print(f"{i}. {pname}")
                
        except Exception as e:
            print(f"Error scanning profiles: {e}")
            self.profiles = {
                "Default": "Default Profile",
                "Profile1": "Profile 1",
                "Profile2": "Profile 2",
            }
    
    def set_credentials(self):
        """Set login credentials"""
        print("\nCurrent credentials:")
        print(f"Email: {self.email}")
        print(f"Password: {'*' * len(self.password) if self.password else 'Not set'}")
        
        email = input("\nEnter email (press Enter to keep current): ").strip()
        if email:
            self.email = email
        
        password = input("Enter password (press Enter to keep current): ").strip()
        if password:
            self.password = password
        
        self.save_config()
        print("Credentials updated!")
    
    def launch_profiles(self):
        """Launch selected profiles"""
        if not self.profiles:
            print("Please scan profiles first!")
            return
        
        if not self.browser_path:
            print("Please set browser path first!")
            return
        
        print("\nSelect profiles to launch:")
        profile_list = list(self.profiles.items())
        for i, (pid, pname) in enumerate(profile_list, 1):
            print(f"{i}. {pname}")
        print("A. All profiles")
        
        choice = input("Enter numbers separated by commas (or 'A' for all): ").strip()
        
        selected = []
        if choice.upper() == "A":
            selected = list(self.profiles.keys())
        else:
            try:
                indices = [int(x.strip()) - 1 for x in choice.split(",") if x.strip().isdigit()]
                for idx in indices:
                    if 0 <= idx < len(profile_list):
                        selected.append(profile_list[idx][0])
            except:
                print("Invalid selection!")
                return
        
        if not selected:
            print("No profiles selected!")
            return
        
        url = input("Enter target URL (default: https://chatgpt.com): ").strip()
        if not url:
            url = "https://chatgpt.com"
        
        print(f"\nLaunching {len(selected)} profiles to {url}...")
        
        for profile in selected:
            self.launch_single_profile(profile, url)
            time.sleep(0.5)
        
        print("Launch complete!")
    
    def launch_single_profile(self, profile, url):
        """Launch a single profile"""
        try:
            if not url.startswith("http"):
                url = "https://" + url
            
            cmd = [self.browser_path, f"--profile-directory={profile}", "--new-window"]
            
            if "chatgpt" in url.lower() or "gemini" in url.lower():
                cmd.append("--app")
            
            cmd.append(url)
            
            startupinfo = None
            if IS_WINDOWS:
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE
            
            subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, startupinfo=startupinfo)
            print(f"  Launched: {self.profiles.get(profile, profile)}")
            return True
            
        except Exception as e:
            print(f"  Failed to launch {profile}: {e}")
            return False
    
    def launch_and_login(self):
        """Launch profiles and auto login"""
        print("\n[INFO] Launch & Auto Login requires pyautogui")
        print("Please install it first: python -m pip install pyautogui")
        print("\nLaunching without auto login...")
        self.launch_profiles()
    
    def arrange_windows(self):
        """Arrange windows"""
        if not IS_WINDOWS:
            print("Window arrangement only available on Windows")
            return
        
        try:
            import ctypes
            
            class RECT(ctypes.Structure):
                _fields_ = [("left", ctypes.c_long), ("top", ctypes.c_long),
                           ("right", ctypes.c_long), ("bottom", ctypes.c_long)]
            
            def get_windows():
                windows = []
                def enum_handler(hwnd, ctx):
                    if ctypes.windll.user32.IsWindowVisible(hwnd):
                        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                        if length > 0:
                            buff = ctypes.create_unicode_buffer(length + 1)
                            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
                            title = buff.value
                            if "ChatGPT" in title or "Gemini" in title:
                                windows.append((hwnd, title))
                    return True
                
                ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
                ctypes.windll.user32.EnumWindows(ENUM_WINDOWS_FUNC(enum_handler), 0)
                return windows
            
            windows = get_windows()
            if not windows:
                print("No ChatGPT/Gemini windows found")
                return
            
            print(f"Found {len(windows)} windows")
            
            # Simple grid arrangement
            for i, (hwnd, title) in enumerate(windows):
                x = (i % 3) * 400
                y = (i // 3) * 850
                ctypes.windll.user32.MoveWindow(hwnd, x, y, 400, 850, True)
                time.sleep(0.05)
            
            print(f"Arranged {len(windows)} windows")
            
        except Exception as e:
            print(f"Error arranging windows: {e}")
    
    def close_windows(self):
        """Close all windows"""
        if not IS_WINDOWS:
            print("Window closing only available on Windows")
            return
        
        try:
            import ctypes
            
            def get_windows():
                windows = []
                def enum_handler(hwnd, ctx):
                    if ctypes.windll.user32.IsWindowVisible(hwnd):
                        length = ctypes.windll.user32.GetWindowTextLengthW(hwnd)
                        if length > 0:
                            buff = ctypes.create_unicode_buffer(length + 1)
                            ctypes.windll.user32.GetWindowTextW(hwnd, buff, length + 1)
                            title = buff.value
                            if "ChatGPT" in title or "Gemini" in title or "AI" in title:
                                windows.append((hwnd, title))
                    return True
                
                ENUM_WINDOWS_FUNC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)
                ctypes.windll.user32.EnumWindows(ENUM_WINDOWS_FUNC(enum_handler), 0)
                return windows
            
            windows = get_windows()
            if not windows:
                print("No AI windows found")
                return
            
            confirm = input(f"Close {len(windows)} windows? (y/n): ").strip().lower()
            if confirm == 'y':
                for hwnd, title in windows:
                    ctypes.windll.user32.PostMessageW(hwnd, 0x0010, 0, 0)
                    time.sleep(0.05)
                print(f"Closed {len(windows)} windows")
            else:
                print("Cancelled")
            
        except Exception as e:
            print(f"Error closing windows: {e}")

# ================================================
# MAIN FUNCTION
# ================================================
def main():
    print("Starting AI Batch Agent...")
    
    if not check_python_version():
        print("\nPython is not properly installed or not in PATH!")
        print("Please install Python from: https://www.python.org/downloads/")
        print("Make sure to check 'Add Python to PATH' during installation.")
        input("\nPress Enter to exit...")
        return
    
    try:
        app = SimpleApp()
        app.run()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")
    except Exception as e:
        print(f"\nError: {e}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()