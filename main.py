"""
Among Us AI Agent - Main Test Module
Runs the test loop for Phase 1: Basic game control automation
"""

import time
import os
from datetime import datetime
from controller import (
    move, interact, open_chat, send_chat, 
    take_screenshot, click
)


def generate_screenshot_path() -> str:
    """
    Generate a unique screenshot path with timestamp
    
    Returns:
        str: Full path for the screenshot file
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return os.path.join("screenshots", f"test_{timestamp}.png")


def run_test_loop():
    """
    Main test loop that demonstrates all controller functions
    """
    print("=" * 50)
    print("AMONG US AI AGENT - PHASE 1 TEST")
    print("=" * 50)
    
    # 3-second startup delay so user can alt-tab into game
    print("\n[STARTUP] Starting in 3 seconds - switch to Among Us game now!")
    print("[STARTUP] 3...")
    time.sleep(1)
    print("[STARTUP] 2...")
    time.sleep(1)
    print("[STARTUP] 1...")
    time.sleep(1)
    print("[STARTUP] GO! Starting test sequence...\n")
    
    try:
        # Take initial screenshot
        print("\n--- INITIAL SCREENSHOT ---")
        screenshot_path1 = generate_screenshot_path()
        take_screenshot(screenshot_path1)
        time.sleep(1)
        
        # Test movement in all 4 directions
        print("\n--- MOVEMENT TESTS ---")
        directions = [
            ('up', 1.0),
            ('right', 1.0), 
            ('down', 1.0),
            ('left', 1.0)
        ]
        
        for direction, duration in directions:
            move(direction, duration)
            time.sleep(0.5)  # Small delay between movements
        
        # Test interact function
        print("\n--- INTERACT TEST ---")
        interact()
        time.sleep(1)
        
        # Test chat functions
        print("\n--- CHAT TESTS ---")
        open_chat()
        time.sleep(0.5)
        send_chat("Hello from AI Agent!")
        time.sleep(1)
        
        # Test click function (center of screen)
        print("\n--- CLICK TEST ---")
        # Get screen dimensions for center click
        import pyautogui  # Only for getting screen size, not for input
        screen_width, screen_height = pyautogui.size()
        center_x, center_y = screen_width // 2, screen_height // 2
        click(center_x, center_y)
        time.sleep(1)
        
        # Take final screenshot
        print("\n--- FINAL SCREENSHOT ---")
        screenshot_path2 = generate_screenshot_path()
        take_screenshot(screenshot_path2)
        
        print("\n" + "=" * 50)
        print("TEST SEQUENCE COMPLETED!")
        print(f"Initial screenshot: {screenshot_path1}")
        print(f"Final screenshot: {screenshot_path2}")
        print("=" * 50)
        
    except KeyboardInterrupt:
        print("\n[STOPPED] Test interrupted by user")
    except Exception as e:
        print(f"\n[ERROR] Test failed: {e}")


if __name__ == "__main__":
    run_test_loop()
