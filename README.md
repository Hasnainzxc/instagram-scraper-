# Instagram Scraper

This is a simple Python script for scraping Instagram profiles and extracting phone numbers, using the `requests` and `BeautifulSoup` libraries.

## Installation

To use this script, you'll need to have Python 3 and the `requests`, `BeautifulSoup`, and `pandas` libraries installed. You can install these libraries using `pip`. 

```bash
pip install requests BeautifulSoup pandas
```

## Usage

To use the script, simply modify the `usernames` list in the script with the usernames you want to scrape, and run the script using Python:

```bash
python insta.py
```

The script will scrape the profiles for the specified usernames and save the results to a CSV file named `instagram_data.csv` in the same directory as the script.

Note that some Instagram profiles may not have a phone number listed, in which case the script will skip over those profiles.

## License

This script is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.
