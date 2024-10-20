import requests
from bs4 import BeautifulSoup

def search_duckduckgo():
    # Ask the user for a query
    query = input("Enter your search query: ")

    # Make the API request
    url = "https://duckduckgo.com/html/"
    params = {
        "q": query
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except requests.RequestException as e:
        print(f"Error making API request: {e}")
        return

    # Extract search results from the HTML
    results = []
    for result in soup.find_all('a', {'class': 'result__a'}):
        title = result.get_text(strip=True)
        link = result['href']
        results.append({'title': title, 'link': link})

    # Print the results
    if results:
        print(f"Search results for '{query}':")
        for i, res in enumerate(results, 1):
            print(f"{i}. {res['title']}")
            print(f"   {res['link']}")
            print()
    else:
        print(f"No results found for '{query}'. Please try rephrasing your query.")

if __name__ == "__main__":
    while True:
        search_duckduckgo()
        print("\n---\n")
