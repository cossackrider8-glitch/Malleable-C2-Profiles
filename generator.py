#!/usr/bin/env python3
# generator.py - KAMUI C2 Profile Generator

import sys
import yaml
import random
import time
from datetime import datetime
from config import DOMAINS, USER_AGENTS, MIMIC_TYPE, OUTPUT_FORMAT
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# --- KAMUI BANNER (Cyber Cyan + Dark Space Purple) ---
def print_banner():
    banner = f"""
{Fore.CYAN}{Style.BRIGHT}
    ██╗  ██╗ █████╗ ███╗   ███╗██╗   ██╗██╗
    ██║ ██╔╝██╔══██╗████╗ ████║██║   ██║██║
    █████╔╝ ███████║██╔████╔██║██║   ██║██║
    ██╔═██╗ ██╔══██║██║╚██╔╝██║██║   ██║██║
    ██║  ██╗██║  ██║██║ ╚═╝ ██║╚██████╔╝██║
    ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝ ╚═════╝ ╚═╝
{Fore.MAGENTA}
        [ C2 PROFILE GENERATOR v1.0 ]
{Fore.CYAN}
        >> Network Evasion & Traffic Mimicry <<
{Fore.MAGENTA}
        Crafted by: Obito Uchiha [ h4ck3r ]  |  KAMUI Protocol
{Fore.RESET}
    """
    print(banner)

# --- MIMICRY ENGINE ---
def get_mimicry_pattern(mimic_type):
    """Returns the exact URI and header patterns based on the mimic type."""
    if mimic_type == "google":
        return {
            "uris": [
                "/search?q=",
                "/_/chrome/newtab?",
                "/complete/search?",
                "/gen_204?"
            ],
            "headers": {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Sec-Fetch-Dest": "document",
                "Sec-Fetch-Mode": "navigate",
                "Sec-Fetch-Site": "none",
                "Connection": "keep-alive",
                "Upgrade-Insecure-Requests": "1"
            },
            "tls": {
                "versions": ["TLSv1.2", "TLSv1.3"],
                "ciphers": [
                    "TLS_AES_128_GCM_SHA256",
                    "TLS_AES_256_GCM_SHA384",
                    "TLS_CHACHA20_POLY1305_SHA256"
                ]
            }
        }
    elif mimic_type == "microsoft":
        return {
            "uris": [
                "/common/oauth2/v2.0/authorize?",
                "/v1.0/me/",
                "/users?",
                "/mailFolders/Inbox/messages?"
            ],
            "headers": {
                "Accept": "application/json, text/plain, */*",
                "Accept-Language": "en-US,en;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "client-request-id": "{{uuid}}",
                "return-client-request-id": "true",
                "Sec-Fetch-Dest": "empty",
                "Sec-Fetch-Mode": "cors",
                "Sec-Fetch-Site": "same-origin"
            },
            "tls": {
                "versions": ["TLSv1.2", "TLSv1.3"],
                "ciphers": [
                    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384",
                    "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256"
                ]
            }
        }
    elif mimic_type == "aws":
        return {
            "uris": [
                "/?Action=ListBuckets&",
                "/?Action=GetObject&",
                "/?Action=PutObject&",
                "/?Action=DeleteObject&"
            ],
            "headers": {
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "X-Amz-Date": "{{timestamp}}",
                "X-Amz-Target": "{{service}}",
                "User-Agent": "aws-sdk-js/2.0.0"
            },
            "tls": {
                "versions": ["TLSv1.2"],
                "ciphers": [
                    "TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256",
                    "TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384"
                ]
            }
        }
    else:
        return None

# --- PROFILE BUILDER ---
def build_profile(domain, user_agent, mimic_type):
    """Builds the full C2 profile YAML dictionary."""
    pattern = get_mimicry_pattern(mimic_type)
    if not pattern:
        print(f"{Fore.RED}[!] Unknown mimic type: {mimic_type}{Fore.RESET}")
        sys.exit(1)

    profile = {
        "name": f"KAMUI_{mimic_type.upper()}_Profile",
        "description": f"Mimics {mimic_type.capitalize()} traffic for C2 evasion",
        "author": "Obito Uchiha",
        "created": datetime.now().isoformat(),
        "http": {
            "domain": domain,
            "uris": pattern["uris"],
            "headers": pattern["headers"],
            "user_agent": user_agent,
            "ssl": pattern["tls"]
        }
    }
    return profile

# --- OUTPUT ---
def output_profile(profile, output_format):
    """Prints or saves the profile."""
    print(f"\n{Fore.GREEN}[+] Generating KAMUI C2 Profile...{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Mimic Type: {MIMIC_TYPE.upper()}{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Domain: {profile['http']['domain']}{Fore.RESET}")
    print(f"{Fore.CYAN}[+] User-Agent: {profile['http']['user_agent'][:60]}...{Fore.RESET}")

    if output_format.lower() == "yaml":
        output = yaml.dump(profile, default_flow_style=False, sort_keys=False)
        filename = f"KAMUI_{MIMIC_TYPE}_{int(time.time())}.yaml"
        
        # Save to file in the profiles/ folder
        with open(f"profiles/{filename}", "w") as f:
            f.write(output)
        print(f"{Fore.GREEN}[+] Profile saved to: profiles/{filename}{Fore.RESET}")
        
        # Also print a preview
        print(f"\n{Fore.MAGENTA}--- PREVIEW ---{Fore.RESET}")
        print(output[:500] + "...\n")
        return output
    else:
        print(f"{Fore.RED}[!] Unsupported output format: {output_format}{Fore.RESET}")
        sys.exit(1)

# --- MAIN EXECUTION ---
def main():
    # Print KAMUI Banner
    print_banner()
    
    print(f"{Fore.CYAN}[+] KAMUI C2 Profile Generator Initialized.{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Mimic Type: {MIMIC_TYPE.upper()}{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Output Format: {OUTPUT_FORMAT.upper()}{Fore.RESET}")
    print(f"{Fore.CYAN}[+] Domains Loaded: {len(DOMAINS)}{Fore.RESET}")
    
    # Pick random domain and user-agent
    domain = random.choice(DOMAINS)
    user_agent = random.choice(USER_AGENTS)
    
    # Build profile
    profile = build_profile(domain, user_agent, MIMIC_TYPE)
    
    # Output profile
    output_profile(profile, OUTPUT_FORMAT)
    
    print(f"\n{Fore.GREEN}[+] KAMUI Engine Finished Successfully.{Fore.RESET}")

if __name__ == "__main__":
    main()
