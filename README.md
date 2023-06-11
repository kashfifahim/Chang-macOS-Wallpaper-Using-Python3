# Dual Monitor Wallpaper Setter
This Python script is designed to change the wallpapers on two separate desktops on macOS. It uses AppleScript executed via Python's `subprocess` module.

## Author
Kashfi Fahim
- Email: kashfi.fahim@gmail.com
- Date: June 11, 2023

## Customizing Wallpapers
To customize the wallpapers for each desktop, you can edit the AppleScript commands in the Python script. Replace the file paths to the images with the paths to your own wallpaper images:
```python
    script1 = """
    tell application "System Events"
        tell desktop 1
            set picture to "/path/to/your/image1.jpg"
        end tell
    end tell
    """

    script2 = """
    tell application "System Events"
        tell desktop 2
            set picture to "/path/to/your/image2.jpg"
        end tell
    end tell
    """
```

## Usage
To run the script, use the following command in Terminal:

```bash
python3 change_wallpaper.py
```

## License 
This script is released under the MIT License.