from seleniumbase import SB

# GitHub par humein xvfb (virtual display) use karna hai, isliye headless=False rakhein
with SB(uc=True, test=True, headless=False) as sb:
    print("Testing URL par jaa rahe hain...")
    url = "https://crichdsee.st/player.php?id=willowextra"
    
    # Page open karna
    sb.driver.uc_open_with_reconnect(url, reconnect_time=3)
    sb.sleep(5) # Page load hone ka wait
    
    print("Screenshot 1 le rahe hain (Before Click)...")
    sb.save_screenshot("1_before_captcha.png")
    
    print("CAPTCHA dhoondh rahe hain aur click kar rahe hain...")
    try:
        sb.driver.uc_gui_click_captcha()
    except Exception as e:
        print(f"Click karte waqt masla aaya: {e}")
    
    sb.sleep(6) # Click ke baad result ka wait
    
    print("Screenshot 2 le rahe hain (After Click)...")
    sb.save_screenshot("2_after_captcha.png")
    print("Test Complete!")
