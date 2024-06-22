
import requests
from bs4 import BeautifulSoup

def fetch_trending_repositories(language="python"):
    url = f"https://github.com/trending/{language}?since=daily"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        repo_list = soup.find_all('article', class_='Box-row')
        
        for repo in repo_list:
            repo_name_tag = repo.find('h1', class_='h3 lh-condensed')
            repo_name = repo_name_tag.text.strip() if repo_name_tag else "No name"
            
            repo_url_tag = repo_name_tag.find('a') if repo_name_tag else None
            repo_url = "https://github.com" + repo_url_tag['href'] if repo_url_tag else "No URL"
            
            repo_desc_tag = repo.find('p', class_='col-9 color-fg-muted my-1 pr-4')
            repo_desc = repo_desc_tag.text.strip() if repo_desc_tag else "No description"
            
            repo_stars_tag = repo.find('a', class_='Link--muted d-inline-block mr-3')
            repo_stars = repo_stars_tag.text.strip() if repo_stars_tag else "0"
            
            repo_forks_tag = repo.find_all('a', class_='Link--muted d-inline-block mr-3')
            repo_forks = repo_forks_tag[1].text.strip() if len(repo_forks_tag) > 1 else "0"
            
            print(f"Repository Name: {repo_name}")
            print(f"URL: {repo_url}")
            print(f"Description: {repo_desc}")
            print(f"Stars: {repo_stars}")
            print(f"Forks: {repo_forks}")
            print("-" * 40)
    else:
        print(f"Failed to fetch trending repositories. Status code: {response.status_code}")

# Fetch and display trending repositories for Python
fetch_trending_repositories("python")


