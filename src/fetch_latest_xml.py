import os
import re
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

def get_latest_file(files):
    latest_file = None
    max_volume_number = -1
    
    for file_path in files:
        # Extract the volume number using regex
        match = re.search(r'vol(\d+)', file_path)
        if match:
            volume_number = int(match.group(1))
            # Update latest_file if a higher volume number is found
            if volume_number > max_volume_number:
                max_volume_number = volume_number
                latest_file = file_path
    return latest_file

def fetch_latest_xml(base_url: str,base_dir: str, title: str, year: str = '2024'):
    url = f"{base_url}{base_dir}/{year}/{title}/"
    chrome_options = Options()  
    # Opens the browser in background
    chrome_options.add_argument("--headless")

    #Open the link in browser
    with Chrome(options=chrome_options) as browser:
        browser.get(url)
        response = browser.page_source
    
    soup = BeautifulSoup(response, 'html.parser')

    # Find XML file by extracting all the links
    files = []
    for a in soup.find_all('a', href=True):
        if a['href'].endswith('.xml'):
            files.append(a['href'])
    if not files:
        raise FileNotFoundError("No XML files found at the specified URL.")
    
    # Find the file with the highest volume number
    latest_file  = get_latest_file(files)

    # Fetch the content of the latest XML file
    xml_url = f"{base_url}{latest_file}"
    xml_response = requests.get(xml_url)
    if xml_response.status_code != 200:
        raise FileNotFoundError(f"Failed to fetch the XML file from {xml_url}. Status code: {xml_response.status_code}")
    
    return xml_response.content, os.path.basename(xml_url)

