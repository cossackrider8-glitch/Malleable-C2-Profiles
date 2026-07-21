# config.py - KAMUI C2 Profile Generator Configuration

# ==============================================
# 1. TARGET DOMAINS (Mimic legitimate traffic)
# ==============================================
DOMAINS = [
    "www.google.com",
    "www.microsoft.com",
    "aws.amazon.com",
    "cloudflare.com",
    "www.github.com"
]

# ==============================================
# 2. USER-AGENTS (Pretend to be real browsers)
# ==============================================
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/126.0.0.0"
]

# ==============================================
# 3. MIMICRY TYPE (Choose one)
# ==============================================
# - "google": Mimics Google search traffic
# - "microsoft": Mimics Office 365 traffic
# - "aws": Mimics AWS API calls
MIMIC_TYPE = "google"   # Options: google, microsoft, aws

# ==============================================
# 4. OUTPUT SETTINGS
# ==============================================
OUTPUT_FORMAT = "yaml"   # Standard for Cobalt Strike / Havoc C2
