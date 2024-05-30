import requests
import os
from dotenv import load_dotenv, find_dotenv
import argparse
import sys

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')

if not API_KEY:
    print("Error: API_KEY not found in .env file.")
    sys.exit(1)

BASE_URL = "https://api.hunter.io/v2"

def domain_search(domain):
    url = f"{BASE_URL}/domain-search?domain={domain}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if 'data' not in data:
        print("No data found for the domain.")
        return
    
    emails = data['data'].get('emails', [])
    
    if not emails:
        print(f"No emails found for the domain {domain}.")
        return
    
    print(f"Emails found for domain {domain}:")
    for email_info in emails:
        email = email_info.get('value')
        sources = email_info.get('sources', [])
        print(f"  {email}")
    
def email_verifier(email):
    url = f"{BASE_URL}/email-verifier?email={email}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if 'data' not in data:
        print("No data found for the email.")
        return
    
    status = data['data'].get('status')
    result = data['data'].get('result')
    
    print(f"Email: {email}")
    print(f"  Status: {status}")
    print(f"  Result: {result}")

def main():
    parser = argparse.ArgumentParser(description='Hunter.io CLI tool')
    parser.add_argument('-d', '--domain', help='Domain to search for emails')
    parser.add_argument('-e', '--email', help='Email to verify')
    
    args = parser.parse_args()
    
    if args.domain:
        domain_search(args.domain)
    elif args.email:
        email_verifier(args.email)
    else:
        print("You must provide a domain or an email to verify. Use -h for help.")
        sys.exit(1)

if __name__ == "__main__":
    main()
