import os
import platform

def shutdown():
    os_type = platform.system()

    if os_type == "Windows":
        os.system("shutdown /s /t 0")
    elif os_type == "Linux" or os_type == "Darwin":  # Darwin is macOS
        os.system("sudo shutdown -h now")
    else:
        print("Unsupported OS")

shutdown()
