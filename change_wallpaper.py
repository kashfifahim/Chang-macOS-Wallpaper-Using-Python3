#!/usr/bin/env python3
# The above line is a "shebang" that sets the interpreter for this script to Python 3.
"""
Author: Kashfi Fahim
Date: June 11, 2023
Email: kashfi.fahim@gmail.com
"""

import subprocess
# We import the subprocess module, which allows us to spawn new processes,
# connect to their input/output/error pipes, and obtain their return codes.

def main(name):
    # This is a function that prints a greeting. It isn't called in this script.
    print(f"Hello, {name}!")

def change_wallpaper():
    # This function changes the desktop wallpapers.
    
    # This is an AppleScript that sets the wallpaper for desktop 1.
    # Replace the path here with the path to your desired image for desktop 1.
    script1 = """
    tell application "System Events"
        tell desktop 1
            set picture to "/path/to/your/image1.jpg"
        end tell
    end tell
    """

    # This is an AppleScript that sets the wallpaper for desktop 2.
    # Replace the path here with the path to your desired image for desktop 2.
    script2 = """
    tell application "System Events"
        tell desktop 2
            set picture to "/path/to/your/image2.jpg"
        end tell
    end tell
    """
    
    # These lines execute the AppleScripts using the osascript command-line tool.
    # The "-e" flag is used to specify the script as a command-line argument.
    subprocess.call(["osascript", "-e", script1])
    subprocess.call(["osascript", "-e", script2])

if __name__ == "__main__":
    # This line checks if the script is being run directly (not being imported).
    # If it is, it calls the change_wallpaper function.
    change_wallpaper()