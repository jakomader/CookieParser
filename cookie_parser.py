import requests
import re
import json


def analyze_cookies(url: str) -> None:
    """
    Function analyzes cookies from the given URL and writes the results to cookies.json.

    Args:
        url (str): The URL to analyze cookies from.
    """
    try:
        response = requests.get(url)

        cookies = response.cookies
        set_cookie_headers = response.headers.get('Set-Cookie', '')

        if isinstance(set_cookie_headers, str):
            set_cookie_headers = [set_cookie_headers]
        
        cookie_an = []
        for cookie in cookies:
            analysis = {
                'name': cookie.name,
                'value': cookie.value,
                'secure': cookie.secure,
                'httponly': cookie.has_nonstandard_attr('HttpOnly'),
                'samesite': cookie.has_nonstandard_attr('SameSite'),
                'other_attributes': []
            }

            for header in set_cookie_headers:
                individual_cookies = header.split(', ')
                for individual_cookie in individual_cookies:
                    if individual_cookie.startswith(f"{cookie.name}="):
                        other_attrs = re.findall(r';\s*([^=]+)(?:=(.*?))?(?=;|$)', individual_cookie)
                        for attr, value in other_attrs:
                            if attr not in ['Secure', 'HttpOnly', 'SameSite']:
                                analysis['other_attributes'].append(f"{attr}={value}" if value else attr)

            cookie_an.append(analysis)

        with open('cookies.json', 'w') as json_file:
            json.dump(cookie_an, json_file, indent=4)
    
    except Exception as e:
        print(f"An error occurred: {e}")
