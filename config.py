import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


webpage_addresses = [
    "https://t.me/s/filterkoshi",
    "https://t.me/s/MsV2ray",
    "https://t.me/s/Outline_Vpn",
    "https://t.me/s/ARv2ray",
    "https://t.me/s/Eleven_vpn",
    "https://t.me/s/v2rayng_org",
    "https://t.me/s/freeownvpn",
    "https://t.me/s/msv2raynp",
    "https://t.me/s/v2rayngvpn",
    "https://t.me/s/VpnProSec",
    "https://t.me/s/VpnOrgSec",
    "https://t.me/s/v2ray_outlineir",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/v2_vmess",
    "https://t.me/s/V2RAY_VMESS_free",
    "https://t.me/s/ShadowsocksM",
    "https://t.me/s/ShadowSocks_s",
    "https://t.me/s/VmessProtocol",
    "https://t.me/s/FOX_VPN66",
    "https://t.me/s/Network_442",
    "https://t.me/s/Awlix_ir",
    "https://t.me/s/God_CONFIG",
    "https://t.me/s/Configforvpn01",
    "https://t.me/s/vpn_ocean"
]

html_pages = []

for url in webpage_addresses:
    response = requests.get(url)
    html_pages.append(response.text)

codes = []

for page in html_pages:
    soup = BeautifulSoup(page, 'html.parser')
    code_tags = soup.find_all('code')

    for code_tag in code_tags:
        code_content = code_tag.text.strip()
        if "vless://" in code_content or "ss://" in code_content or "vmess://" in code_content or "trojan://" in code_content:
            codes.append(code_content)

codes = list(set(codes))  # Remove duplicates

processed_codes = []

# Get the current date and time
current_date_time = datetime.now()

# Print the current month in letters
current_month = current_date_time.strftime("%b")

# Get the current day as a string
current_day = current_date_time.strftime("%d")

# Increase the current hour by 4 hours
new_date_time = current_date_time + timedelta(hours=4)

# Get the updated hour as a string
updated_hour = new_date_time.strftime("%H")

# Combine the strings to form the final result
final_string = f"{current_month}-{current_day}-{updated_hour}"

i = 1
for code in codes:
    vmess_parts = code.split("vmess://")
    vless_parts = code.split("vless://")

    for part in vmess_parts + vless_parts:
        if "ss://" in part or "vmess://" in part or "vless://" in part or "trojan://" in part:
            service_name = part.split("serviceName=")[-1].split("&")[0]
            processed_part = part.split("#")[0] + "#✅ " + str(final_string) + ":00-" + str(i)
            processed_codes.append(processed_part)
            i += 1

processed_codes = list(set(processed_codes))

print(processed_codes)

with open("config.txt", "w", encoding="utf-8") as file:
    for code in processed_codes:
        print(code)
        file.write(code + "\n")
