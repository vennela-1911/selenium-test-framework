import os
from datetime import datetime

def take_screenshot(driver, name):

    folder = "reports/screenshots"

    os.makedirs(folder, exist_ok=True)

    file = f"{folder}/{name}_{datetime.now().strftime('%H%M%S')}.png"

    driver.save_screenshot(file)

    return file