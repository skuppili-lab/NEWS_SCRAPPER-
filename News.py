import requests
from bs4 import BeautifulSoup

url = "https://news.google.com/home?hl=en-IN&gl=IN&ceid=IN:en"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

with open("news.txt", "w", encoding="utf-8") as f:
    
    # 1. Get the Page Title
    f.write(f"Title: {soup.title.text}\n\n")
    
    # 2. Get all Article Details (Headline, Org, Time)
    f.write("--- ARTICLES ---\n")
    
    # In Google News, we can look for all <time> tags to find articles
    for time_tag in soup.find_all('time'):
        
        # Go up the HTML tree to get the container that holds the entire article
        article_box = time_tag.parent.parent
        
        # 1. Get the Time Published
        published_time = time_tag.text.strip()
        
        # 2. Get the Headline and URL
        headline_tag = article_box.find('a', class_='gPFEn')
        
        # 3. Get the Organization
        org_tag = article_box.find('div', class_='vr1PYe')
        
        # If we successfully found the headline, save all the details!
        if headline_tag:
            headline = headline_tag.text.strip()
            link = headline_tag.get('href')
            organization = org_tag.text.strip() if org_tag else "Unknown Organization"
            
            f.write(f"Headline: {headline}\n")
            f.write(f"Organization: {organization}\n")
            f.write(f"Time: {published_time}\n")
            f.write(f"URL: {link}\n")
            f.write("-" * 40 + "\n")
