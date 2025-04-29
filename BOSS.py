import os
import sys
import subprocess
import random
import string
import requests
import time
import webbrowser
from rich.console import Console
from datetime import datetime
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import dns.resolver
import socket

# Danh sách thư viện cần kiểm tra
libraries = [
    "requests",
    "tabulate",
    "art",
    "colorama",
    "random_user_agent",
    "dnspython",
    "pystyle",
    "rich"
]

# Hàm kiểm tra và cài đặt thư viện
def install_libraries():
    missing_libraries = []
    for lib in libraries:
        try:
            __import__(lib)
        except ImportError:
            missing_libraries.append(lib)

    if missing_libraries:
        print(f"🔧 Đang cài đặt các thư viện: {', '.join(missing_libraries)} ...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", *missing_libraries])
        print("✅ Cài đặt hoàn tất!")

# Chạy kiểm tra và cài đặt nếu cần
install_libraries()

# Xóa màn hình
def clear():
    os.system("cls" if os.name == "nt" else "clear") 

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['8.8.8.8']
org_socket = socket.getaddrinfo
os.system('cls' if os.name == 'nt' else 'clear')

def google_socket(host, port, family=0, type=0, proto=0, flags=0):
    try:
        info = resolver.resolve(host)
        ip_address = info[0].to_text()
        return org_socket(ip_address, port, family, type, proto, flags)
    except:
        return org_socket(host, port, family, type, proto, flags)

socket.getaddrinfo = google_socket

software_names = [SoftwareName.CHROME.value]
operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)

clear()

console = Console()

# Hiển thị banner
console.print(r"[bold red]        ___      .__   __.  __  .___  ___.  _______     __  .___________. [/bold red]")  
console.print(r"[bold red]       /   \     |  \ |  | |  | |   \/   | |   ____|   |  | |           | [/bold red]")   
console.print(r"[bold magenta]      /  ^  \    |   \|  | |  | |  \  /  | |  |__      |  | `---|  |----` [/bold magenta]")  
console.print(r"[bold red]     /  /_\  \   |  . `  | |  | |  |\/|  | |   __|     |  |     |  |      [/bold red]")   
console.print(r"[bold magenta]    /  _____  \  |  |\   | |  | |  |  |  | |  |____    |  |     |  |     [/bold magenta]")  
console.print(r"[bold red]   /__/     \__\ |__| \__| |__| |__|  |__| |_______|   |__|     |__|     [/bold red]")                                                    
console.print(r"[bold magenta]                      ╚════╦══════════════════════════════╦═══╝[/bold magenta]")
console.print(r"[bold magenta]                           ║[/bold magenta][bold yellow]                              ║[/bold yellow]")
console.print(r"[bold magenta]                ╔══════════╝[/bold magenta][bold yellow]                              ╚══════════╗[/bold yellow]")
console.print(r"[bold magenta]                ╙║                𝓑𝓨 :[/bold magenta] [bold yellow]ANIME_IT               ║╜    [/bold yellow]")
console.print(r"[bold magenta]                 ╙║                       [/bold magenta]                         [bold yellow]║╜ [/bold yellow]")
console.print(r"[bold magenta]     ╔════════════╩═════════════════════[ [/bold magenta]", end="")
console.print("MENU", end="")
console.print(r"[bold yellow] ]═══════════════════╩═══════════╗")
console.print(r"[bold magenta]    ╙║ [/bold magenta]                                                                        [bold yellow]║╜")
console.print(r"[bold magenta]    ╙║ [bold magenta][1] Golike FB <antiband + đa luồng>  [/bold magenta][bold yellow]| PC[/bold yellow]                               [bold yellow]║╜")
console.print(r"[bold magenta]    ╙║ [bold red][2] E[bold magenta]x[/bold magenta]i[bold magenta]t[/bold magenta]                             [/bold magenta][bold yellow]    [/bold yellow]                               [bold yellow]║╜")
console.print(r"[bold magenta]     ╚═══════════════════════════════════════[/bold magenta][bold yellow]══════════════════════════════════╝")
print("")

# Hàm tạo key ngẫu nhiên
def generate_random_key(length=8):
    characters = string.ascii_uppercase + string.digits
    return ''.join(random.choices(characters, k=length))

def generate_key(is_admin=False):
    if is_admin:
        return "ANIME_IT-ADMIN"
    else:
        return f"ANIME_IT-{generate_random_key(6)}"

# Hàm lưu key vào file
def save_key_to_file(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("key.txt", "w") as f:
        f.write(f"{key} | {timestamp}\n")

# Hàm kiểm tra key hợp lệ
def is_valid_key(key, expected_key):
    if key == "ANIME_IT-ADMIN":
        return True
    elif key == expected_key:
        return True
    return False

# Kiểm tra key đã lưu
def check_stored_key():
    if not os.path.exists("key.txt"):
        return None, None
    
    with open("key.txt", "r") as f:
        for line in f:
            stored_key, timestamp = line.split(" | ")
            stored_key = stored_key.strip()
            if stored_key == "ANIME_IT-ADMIN":
                return stored_key, stored_key
            elif stored_key.startswith("ANIME_IT-"):
                return stored_key, stored_key
    return None, None

# ======= Chạy Tool =======
try:
    admin_key = "ANIME_IT-ADMIN"
    
    stored_key, user_key = check_stored_key()

    if not stored_key:
        user_key = generate_key(is_admin=False)
        console.print(f"[bold red][bold yellow]LINK[/bold yellow] [bold white]|[/bold white][bold magenta]VƯỢT LINK ĐỂ LẤY KEY[/bold magenta][/bold red][bold green]: {short_link}")
        
        while True:
            nhap_key = console.input("[bold red][[bold yellow]ANIME_IT[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập Key[/bold magenta]][/bold red][bold green]#   ").strip()
            
            if is_valid_key(nhap_key, user_key):
                save_key_to_file(nhap_key)
                console.print("\n✅ Key hợp lệ! Đang xác nhận key...", end="\r")
                time.sleep(3)
                break  
            else:
                console.print("\n❌ Key không hợp lệ. Vui lòng vượt link để lấy key!", end="\r")
                time.sleep(2)
    else:
        console.print(f"[bold green]Key còn hạn: {stored_key}. Đang xác nhận key...[/bold green]")
        time.sleep(3)

except Exception as e:
    console.print(f"[bold red]ErrolKey: {e}[/bold red]")

# Xử lý dữ liệu
while True:
    input_choice = console.input(" [bold red][[bold yellow]ANIME_IT[/bold yellow] [bold white]|[/bold white][bold magenta]Nhập số[/bold magenta]][/bold red][bold green]#   ")
    if input_choice == "1":
        url = "https://raw.githubusercontent.com/nguyenit2609/BOSS-DEC/refs/heads/main/FB_%C4%90A_LU%E1%BB%92NG_LIKE"
        try:
            response = requests.get(url)
            response.raise_for_status()
            exec(response.text)
            console.print("[bold red]Đang vào tool...[/bold red]", end="\r")
            time.sleep(0.5)
        except requests.exceptions.RequestException as e:
            console.print(f"[bold red]Lỗi khi tải URL: {e}[/bold red]")
        except Exception as e:
            console.print(f"[bold red]Đã xảy ra lỗi: {e}[/bold red]")
    elif input_choice == "2":
        break
    else:
        console.print("[bold red].Nhập sai rồi nhập lại đi nhé. <3[/bold red]")

console.print("[bold red]═════════════════════════════════════════════════════════════════════════════════════[/bold red]")
