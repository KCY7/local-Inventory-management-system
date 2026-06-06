import os
import sys
import threading
import time
import subprocess
import webview
from django.core.management import execute_from_command_line

def trigger_background_backup():
    """Runs the PowerShell backup script quietly in the background."""
    try:
        # Looks for the script right next to your .exe
        script_path = os.path.join(os.getcwd(), "auto_backup.ps1")
        if os.path.exists(script_path):
            subprocess.Popen([
                "powershell.exe", 
                "-ExecutionPolicy", "Bypass", 
                "-WindowStyle", "Hidden", 
                "-File", script_path
            ])
            print(">>> Backup triggered.")
    except Exception as e:
        print(f"Backup failed: {e}")

def start_django():
    """Starts the Django development server."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    # --noreload is critical for PyInstaller
    execute_from_command_line(['manage.py', 'runserver', '127.0.0.1:8000', '--noreload'])

if __name__ == '__main__':
    # Initial Backup on Start
    trigger_background_backup()

    # Start Django in a background thread
    t = threading.Thread(target=start_django, daemon=True)
    t.start()

    # Wait for server to initialize
    time.sleep(2)

    # Create the Standalone App Window
    webview.create_window(
        'Holy Child College Inventory', 
        'http://127.0.0.1:8000/login/', 
        width=1280, 
        height=800,
        min_size=(1024, 600)
    )
    
    # Start the engine (gui='qt' uses PySide6 if installed)
    webview.start()

    # Final Backup on Close
    trigger_background_backup()