import os
from fetch_latest_xml import fetch_latest_xml
from xml_to_pdf import xml_to_pdf

def save_file(content: bytes, file_path: str):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'wb') as file:
        file.write(content)

def main():
    base_url = "https://www.govinfo.gov/"
    base_dir = "bulkdata/CFR"
    title = "title-12"
    year = "2024"
    try:
        xml_content, latest_file = fetch_latest_xml(base_url, base_dir, title, year)
        
        #Save Xml content in file
        data_dir = "./data/2024"
        xml_file_path = os.path.join(data_dir, latest_file)
        save_file(xml_content, xml_file_path)
        
        #create pdf file from xml content
        pdf_file_path = os.path.splitext(xml_file_path)[0] + ".pdf"
        xml_to_pdf(xml_content, pdf_file_path)
        
        print(f"PDF file created and saved at: {pdf_file_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()
