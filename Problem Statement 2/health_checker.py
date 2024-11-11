import requests

url = "http://yourapplication.com" 

try:
 
    response = requests.get(url, timeout=5)  
    
    if response.status_code == 200:
        print("Application is up and running!")
    else:
        print(f"Application is down. Status code: {response.status_code}")
except requests.ConnectionError:
    print("Application is down. Failed to connect.")
except requests.Timeout:
    print("Application is down. Request timed out.")
except requests.RequestException as e:
    print(f"Application is down. Error: {e}")
