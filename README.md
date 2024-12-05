Syosetu Novel Scraper

This Python script scrapes novels from Syosetu (ncode.syosetu.com) and saves them into a single .txt file, with chapters properly ordered and formatted.

📋 Features

Scrapes all chapters from a Syosetu novel URL.

Extracts chapter titles and content.

Saves the scraped content into a text file with the provided name.

Gracefully handles errors and skips invalid chapters.


🛠️ Requirements

Python 3.6+

Libraries:

'cloudscraper'

'beautifulsoup4'



Install the required libraries with:

'''pip install cloudscraper beautifulsoup4'''

🚀 Usage

1. Clone this repository or download the script:

git clone https://github.com/vikyathkamathd/Syosetu-Novel-Scraper.git
cd Syosetu-Novel-Scraper


2. Run the script:

'''python syosetu_scraper.py'''


3. Provide the required inputs:

Book Name: The desired filename for the novel (e.g., MyNovel).

Novel URL: The base URL of the Syosetu novel (e.g., https://ncode.syosetu.com/n0488jh/).



4. The script will automatically scrape all chapters and save them to a .txt file.



Example

Input:

Enter book name: MyNovel
Enter novel URL (Ex: https://ncode.syosetu.com/n0488jh/): https://ncode.syosetu.com/n0488jh/

Output:

Chapter 1: Title 1 saved successfully.
Chapter 2: Title 2 saved successfully.
...
Scraping completed. Book saved as 'MyNovel.txt'.

📝 Notes

Ensure the novel URL is valid and follows the format https://ncode.syosetu.com/{novel_id}/.

The script appends chapters to the text file. Use a new filename for each novel to avoid overwriting.

💻 Contributing

Contributions are welcome! If you encounter bugs or have suggestions, feel free to submit an issue or a pull request.
