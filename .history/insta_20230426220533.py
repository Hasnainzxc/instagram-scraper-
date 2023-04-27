import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_instagram(username):
    # Send a GET request to the user's Instagram page
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)

    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the user's phone number, if it's available
    phone_number = soup.find("span", {"class": "glyphsSpriteMobile_nav_type_large"}).parent.get_text().strip()

    # Return the username and phone number as a tuple
    return (username, phone_number)

# Get a list of usernames to scrape
usernames = ["hasnainzxc", "tayyabaamir67", "username3"]

# Scrape the usernames and phone numbers
results = []
for username in usernames:
    try:
        result = scrape_instagram(username)
        results.append(result)
    except:
        pass

# Convert the results to a pandas dataframe
df = pd.DataFrame(results, columns=["Username", "Phone Number"])

# Save the dataframe to a CSV file
print(df)

df.to_csv("instagram_data.csv", index=False)


print(df)
