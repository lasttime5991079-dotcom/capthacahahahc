from seleniumbase import SB
import random

# Proxy use karne ke liye, niche wale section ko uncomment karein
# Aur apne proxy details enter karein. Ek residential proxy sab se behtareen hai.
# PROXY_STRING = "http://username:password@proxy_host:proxy_port" 

# GitHub par humein headless=False hi use karna hai xfvb ke saath.
# settings.DEFAULT_SB_SETUP allows more context-specific setup control
with SB(uc=True, test=True, headless=False, proxy=None) as sb: 
    print("Testing URL par jaa rahe hain...")
    url = "https://crichdsee.st/player.php?id=willowextra"
    
    # 1. Open and Wait
    # Page open karein, aur lambay reconnect time ke saath check karein
    try:
        sb.driver.uc_open_with_reconnect(url, reconnect_time=10) # Lambay reconnect time
    except Exception as e:
        print(f"Error opening page: {e}")
        sb.save_screenshot("error_opening.png")
        raise # Exit if page won't load
    
    # Mazeed random delay page settle hone ke liye
    initial_delay = random.uniform(5, 8) 
    print(f"Page settle hone ka {initial_delay:.1f} seconds wait karein ge...")
    sb.sleep(initial_delay) 
    
    print("Screenshot 1 le rahe hain (Before Click Attempt)...")
    sb.save_screenshot("1_before_click.png")
    
    # 2. Robust Clicking with Retries
    for attempt in range(1, 3): # 2 attempts karein ge
        print(f"Attempt {attempt}: CAPTCHA checkbox ko dhoondh rahe hain...")
        
        # Check karein agar checkbox still visible hai
        if sb.is_element_visible("iframe"): 
            try:
                # Human behavior simulate karne ke liye short delay before click
                pre_click_delay = random.uniform(1.5, 3)
                print(f"Humanlike delay {pre_click_delay:.1f} seconds click se pehle...")
                sb.sleep(pre_click_delay)

                # Execute critical click function
                sb.driver.uc_gui_click_captcha()
                print(f"Attempt {attempt}: Click executed. Wait kar rahe hain result ke liye...")
                
                # Click ke baad post-click delay, random
                post_click_delay = random.uniform(8, 12)
                print(f"Result observe karne ke liye {post_click_delay:.1f} seconds wait...")
                sb.sleep(post_click_delay)

            except Exception as e:
                print(f"Attempt {attempt}: Click fail hua: {e}")
            
            # Click ke baad check karein if checkbox updated (successfully passed or still present)
            if not sb.is_element_visible("iframe") or attempt == 2: # Pass or no more tries
                break
            else:
                print("Attempt fail lag rahi hai. Reload kar ke retry karein ge.")
                sb.refresh() # Page reload karein next attempt ke liye
                sb.sleep(10) # Reload ke baad settle delay
        else:
            print("CAPTCHA iframe not visible. Shayed automatically pass ho gaya ya challenge change ho gaya.")
            break # No iframe, no click needed
    
    print("Final Screenshot (After Click Attempt)...")
    sb.save_screenshot("2_final_after_click.png")
    print("Test Complete!")
