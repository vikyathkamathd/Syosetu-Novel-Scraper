# Syosetu Novel Scraper

A Python script that scrapes chapters of novels/books from Syosetu (ncode.syosetu.com) using the `cloudscraper` and `BeautifulSoup` libraries.

## Features
- Scrapes all chapters from a specified Syosetu novel URL.
- Extracts chapter titles and contents.
- Saves the chapters into a single `.txt` file with proper formatting.

## Requirements
- Python 3.x
- Libraries:
  - `cloudscraper`
  - `beautifulsoup4`

## Installation
1. Clone the repository:
    ```git clone https://github.com/vikyathkamathd/Syosetu-Novel-Scraper.git
    cd Syosetu-Novel-Scraper
    ```

2. Install the required libraries:
    ```pip install cloudscraper beautifulsoup4
    ```

## Usage
1. Run the script:
    ```python syosetu_scraper.py
    ```

2. Enter the required inputs when prompted:
   - **Book Name**: The desired filename for the output file (e.g., `MyNovel`).
   - **Novel URL**: The base URL of the Syosetu novel (e.g., `https://ncode.syosetu.com/n0488jh/`).

3. Once the script completes, the `.txt` file will be saved with the specified book name.

## Example
**Input:**
```plaintext
Enter book name: MyNovel
Enter novel URL (Ex: https://ncode.syosetu.com/n0488jh/): https://ncode.syosetu.com/n0488jh/
