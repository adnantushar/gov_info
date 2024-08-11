# XML to PDF Converter

## Project Overview

This Python project is designed to automatically fetch the latest XML file from a specified directory on the [govinfo.gov](https://www.govinfo.gov/) website and convert its content into a PDF file. The script is dynamic, meaning it can adapt to changes in the directory structure, such as changes in the directory, year or title.

### Project Structure

```plaintext
gov_info/
│
├── data/
│   ├── 2024                  # Store genarated XML file and pdf file
├── src/
│   ├── fetch_latest_xml.py   # Script to fetch the latest XML file
│   ├── xml_to_pdf.py         # Script to convert XML content to PDF
│   └── main.py               # Main script to coordinate fetching and conversion
│
├── README.md                 # Project documentation
├── requirements.txt          # List of dependencies
└── .gitignore                # Files and directories to be ignored by Git
 ```
## Code Tools Explanation

This script uses several Python libraries and tools to fetch the latest XML file from a specified URL and return its content. Below is a description of each tool used in the script:

- os:
  - The os module is used for interacting with the operating system. In this script, it is used to extract the file name from a URL (os.path.basename) and Join Path     (os.path.join).
  
- re:
    - The re module provides support for regular expressions in Python. Here, it's used to extract volume numbers from file paths to identify the latest file.
      
- requests:
    - The requests module allows sending HTTP requests in Python. It is used to fetch the content of the latest XML file after identifying it.

- BeautifulSoup (from bs4):
    - BeautifulSoup is used for parsing HTML and XML documents. In this script, it is used to parse the HTML page and find all the links that end with .xml.

- Selenium:
    - Selenium is used for automating web browser interaction. Beautiful Soup can only parse static HTML content. It cannot execute JavaScript, so if the content is loaded dynamically with JavaScript, Beautiful Soup won't see it. Selenium can execute JavaScript to get the fully rendered HTML. The Chrome object is used to open the webpage, and Options allows configuring the browser to run in headless mode (without a graphical user interface).

## Quick Start 

> Get the code

```bash
$ git clone https://github.com/adnantushar/gov_info.git
$ cd gov_info
```

> Install the required dependencies

```bash
$ pip install -r requirements.txt
```
Download and install the Chrome WebDriver to enable Selenium interaction with Chrome. Ensure the WebDriver version matches your installed Chrome browser version. Add the WebDriver executable to your system's PATH.

>Run the script

```bash
$ python src/main.py
```

## Notes
- Ensure that the Chrome WebDriver is installed and properly configured to run the script in headless mode.
- The script is set up to work with the 2024 edition of the title-12 directory, but it can be easily modified to work with other directory, titles or years by changing the parameters in fetch_latest_xml.

## License

[MIT](https://choosealicense.com/licenses/mit/)
