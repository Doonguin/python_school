# Import pyautogui
import pyautogui

# Import Pillow
from PIL import Image

# Maakt een screenshot
my_screenshot = pyautogui.screenshot()

# Geeft aan waar de screenshot opgeslagen moet worden 
screenshot_path = r'.\images\screenshot.png'

# Slaat de screenshot op in het opgegeven pad
my_screenshot.save(screenshot_path)

# Opent de screenshot om aanpassingen te maken
image_1 = Image.open(screenshot_path)

# Convert de screenshot naar een rgb kleuren schema
im_1 = image_1.convert('RGB')