#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8).

This script handles urllib.error.HTTPError exceptions and prints:
Error code: followed by the HTTP status code.

Usage: ./3-error_code.py <URL>
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
