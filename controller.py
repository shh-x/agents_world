"""
Among Us AI Agent - Controller Module
Handles all keyboard and mouse inputs using pydirectinput
and screenshot capture using PIL/Pillow
"""

import pydirectinput
import time
from PIL import ImageGrab
import os


def move(direction: str, duration: float) -> None:
    """
    Move the character in the specified direction using WASD keys
    
    Args:
        direction (str): Direction to move ('up', 'down', 'left', 'right')
        duration (float): Duration in seconds to hold the key
    """
    try:
        direction = direction.lower()
        key_map = {
            'up': 'w',
            'down': 's', 
            'left': 'a',
            'right': 'd'
        }
        
        if direction not in key_map:
            print(f"[ERROR] Invalid direction: {direction}. Use up/down/left/right")
            return
            
        key = key_map[direction]
        print(f"[ACTION] Moving {direction.upper()} for {duration} seconds")
        
        pydirectinput.keyDown(key)
        time.sleep(duration)
        pydirectinput.keyUp(key)
        
    except Exception as e:
        print(f"[ERROR] Failed to move {direction}: {e}")


def interact() -> None:
    """
    Press the interact key (F) to interact with objects in game
    """
    try:
        print("[ACTION] Pressing INTERACT key (F)")
        pydirectinput.press('f')
        time.sleep(0.1)  # Small delay to prevent input flooding
        
    except Exception as e:
        print(f"[ERROR] Failed to interact: {e}")


def open_chat() -> None:
    """
    Open the in-game chat by pressing the chat key (E or Enter)
    """
    try:
        print("[ACTION] Opening CHAT")
        pydirectinput.press('enter')
        time.sleep(0.2)  # Allow time for chat to open
        
    except Exception as e:
        print(f"[ERROR] Failed to open chat: {e}")


def send_chat(message: str) -> None:
    """
    Type and send a chat message in the game
    
    Args:
        message (str): Message to send in chat
    """
    try:
        print(f"[ACTION] Sending chat message: '{message}'")
        
        # Type the message
        pydirectinput.write(message)
        time.sleep(0.1)
        
        # Send the message
        pydirectinput.press('enter')
        time.sleep(0.1)
        
    except Exception as e:
        print(f"[ERROR] Failed to send chat message: {e}")


def take_screenshot(save_path: str) -> None:
    """
    Capture and save the current screen as a screenshot
    
    Args:
        save_path (str): File path where screenshot will be saved
    """
    try:
        print(f"[ACTION] Taking screenshot and saving to: {save_path}")
        
        # Capture the screen
        screenshot = ImageGrab.grab()
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Save the screenshot
        screenshot.save(save_path)
        print(f"[SUCCESS] Screenshot saved successfully")
        
    except Exception as e:
        print(f"[ERROR] Failed to take screenshot: {e}")


def click(x: int, y: int) -> None:
    """
    Click at specific screen coordinates
    
    Args:
        x (int): X coordinate on screen
        y (int): Y coordinate on screen
    """
    try:
        print(f"[ACTION] Clicking at coordinates ({x}, {y})")
        pydirectinput.click(x, y)
        time.sleep(0.1)  # Small delay to prevent input flooding
        
    except Exception as e:
        print(f"[ERROR] Failed to click at ({x}, {y}): {e}")
