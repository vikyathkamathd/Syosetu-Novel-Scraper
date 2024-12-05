import cloudscraper
from bs4 import BeautifulSoup

def scrape_syosetu():
    # Get user input for book name and novel URL
    book_name = input("Enter book name: ").strip() + ".txt"
    url = input("Enter novel URL (Ex: https://ncode.syosetu.com/n0488jh/): ").strip()
    scraper = cloudscraper.create_scraper()
    chapter_number = 1

    while True:
        chapter_url = f"{url}{chapter_number}"
        try:
            response = scraper.get(chapter_url)
            if response.status_code != 200:
                print("No more chapters or invalid URL.")
                break
        except Exception as e:
            print(f"Error retrieving URL: {e}")
            break

        # Parse the HTML response
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Extract title
        try:
            title = soup.title.text.split("-")[1].strip()
        except (IndexError, AttributeError):
            try:
                title = soup.find('div', class_='p-novel__subtitle-episode').text.strip()
            except AttributeError:
                print(f"Could not extract title for chapter {chapter_number}.")
                break

        # Extract chapter content
        try:
            content_div = soup.find('div', class_='p-novel__body')
            paragraphs = content_div.find_all('p')
            chapter_content = "\n\n".join(p.text.strip() for p in paragraphs if p.text.strip())
        except AttributeError:
            print(f"Could not extract content for chapter {chapter_number}.")
            break

        # Write to file
        with open(book_name, "a", encoding="utf-8") as file:
            file.write(f"{title}\n\n")
            file.write(f"{chapter_content}\n\n")
        print(f"Chapter {chapter_number}: {title} saved successfully.")

        # Move to the next chapter
        chapter_number += 1

    print(f"Scraping completed. Book saved as '{book_name}'.")

if __name__ == "__main__":
    scrape_syosetu()