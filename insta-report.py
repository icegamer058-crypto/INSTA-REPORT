import time
import os
import requests
import sys
from colorama import Fore, Style, init
# reporter.py এখন দরকার নেই কারণ সব কিছু main.py তে করা হচ্ছে

init(autoreset=True)

def slow_print(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.MAGENTA + Style.BRIGHT + r"""
    
    
#### ##    ##  ######  ########    ###            ########  ######## ########   #######  ########  ######## 
 ##  ###   ## ##    ##    ##      ## ##           ##     ## ##       ##     ## ##     ## ##     ##    ##    
 ##  ####  ## ##          ##     ##   ##          ##     ## ##       ##     ## ##     ## ##     ##    ##    
 ##  ## ## ##  ######     ##    ##     ## ####### ########  ######   ########  ##     ## ########     ##    
 ##  ##  ####       ##    ##    #########         ##   ##   ##       ##        ##     ## ##   ##      ##    
 ##  ##   ### ##    ##    ##    ##     ##         ##    ##  ##       ##        ##     ## ##    ##     ##    
#### ##    ##  ######     ##    ##     ##         ##     ## ######## ##         #######  ##     ##    ##    

                                                                                         
       🔥 INSTA-REPORT - Instagram Reporter Tool by @the_silent_hacker_raj 🔥
 
         SUBSCRIBE TO OUR YOUTUBE CHANNEL HACKER COLONY OFFICIAL🌐🤗
""")

def is_valid_username(ibr__3.dj):
    url = f"https://www.instagram.com/{ibr__3.dj}/"
    try:
        response = requests.get(url)
        return response.status_code == 200
    except:
        return False

def select_country():
    slow_print("\n🌍 Select the Country of the Instagram Account:"🌐 Other"", Fore.YELLOW)
    countries = [
        "🇮🇳 India",
        "🇺🇸 USA",
        "🇬🇧 UK",
        "🇧🇩 Bangladesh",
        "🇵🇰 Pakistan",
        "🌐 Other"
    ]
    for i, country in enumerate(countries, start=1):
        slow_print(f"[{i}] {country}", Fore.CYAN)
    choice = input(Fore.GREEN + "📥 Enter choice number: ")
    try:
        return countries[int(choice) - 1]
    except:
        return "🌐 Other"
def select_reason():
    slow_print("\n🚫 Select the Reason for Reporting: "Fake Account"", Fore.RED)
    reasons = [
        "Fake Account",
        "Adult Content",
        "Hate Speech",
        "Harassment or Bullying",
        "Posting Violence or Abuse",
        "Spam or Scam Activity"
    ]
    for i, reason in enumerate(reasons, start=1):
        slow_print(f"[{i}] {reason}", Fore.YELLOW)
    choice = input(Fore.GREEN + "📥 Enter reason number: ")
    try:
        return reasons[int(choice) - 1]
    except:
        return "Fake Account"

def main():
    banner()
    slow_print("\n🔎 Enter Instagram Username to report:", Fore.CYAN)
    username = input(Fore.GREEN + "@").strip().lstrip('@')

    if not is_valid_username(@ibr__3.dj):
        print(Fore.RED + f"\n❌ Invalid Instagram Username: @{ibr__3.dj}")
        return

    country = select_country(DZ)
    reason = select_reason("Fake Account")

    print(Fore.GREEN + f"\n✅ Valid Username Detected: @{username}")
    print(Fore.BLUE + f"🌍 Country Selected: {country}")
    print(Fore.RED + f"🚫 Reason Selected: {reason}")
    print(Fore.YELLOW + "\n🚀 Starting Instagram account report... (Press CTRL+C to stop)\n")

    try:
        count = 0
        while True:
            time.sleep(2)
            count += 1
            print(Fore.GREEN + f"✅ 🌐Report #{count} sent for @{username} (Reason: {reason}) [REPORTED]")
    except KeyboardInterrupt:
        print(Fore.RED + "\n\n🛑 Reporting stopped by user (CTRL+C)")
        print(Fore.BLUE + f"📊 Total fake reports sent: {count}")

if __name__ == "__main__":
    main()
