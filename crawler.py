import requests
from bs4 import BeautifulSoup
import json
import re
import argparse
import logging

def crawl(start_url, depth) -> None:
    """
    Crawls a given URL and saves the results into a JSON file.

    Args:
        start_url: The URL to start crawling from.
        depth: The maximum depth to crawl to.

    Returns:
        None
    """
    # Set up logging to a file.
    logging.basicConfig(filename='crawler.log', level=logging.DEBUG)

    # List of crawled image URLs with source URL and depth.
    results = []

    def crawl_helper(url, curr_depth) -> None:
        """
        Helper function that recursively crawls a URL and its links up to a given depth.

        """
         
        # Stop crawling if the maximum depth has been reached.
        if curr_depth > depth:
            return

        # Log the URL and depth being crawled.
        logging.info(f"Crawling {url} at depth {curr_depth}")

        # Create a session to maintain cookies across requests.
        session = requests.Session()

        # Make a GET request to the URL.
        response = session.get(url)

        # Check if the request was successful.
        if response.status_code != 200:
            logging.error(f"Failed to crawl {url}")
            return

        # Add the URL to the set of visited URLs.
        visited_urls.add(url)

        # Parse the HTML using BeautifulSoup.
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract images from the parsed HTML.
        images = soup.find_all("img")
        for img in images:
            img_url = img.get("src")
            # If the image URL is relative, make it absolute using the base URL.
            if not img_url.startswith(("http://", "https://")):
                img_url = url + img_url
            # Add the image URL to the results list with source URL and depth.
            results.append({
                "imageUrl": img_url,
                "sourceUrl": url,
                "depth": curr_depth
            })

        links = soup.find_all("a")
        for link in links:
            href = link.get("href")
            if href and re.match("^https?://", href):
                if href not in visited_urls:
                    crawl_helper(href, curr_depth + 1)

    # Set of visited URLs to prevent visiting the same URL multiple times.
    visited_urls = set()

    # Set of visited URLs to prevent visiting the same URL multiple times.
    crawl_helper(start_url, 0)

    # Save the results to a JSON file.
    with open("results.json", "w") as f:
        json_string = json.dumps({"results": results}, indent=4)
        f.write(json_string)

def get_args():
    # Create a parser object 
    parser = argparse.ArgumentParser(description="Web crawler exercise.")

    # Add arguments to the parser object 
    parser.add_argument("start_url", type=str, help="Starting URL.")
    parser.add_argument("depth", type=int, help="The maximum depth of pages to crawl from the starting URL.")
    args = parser.parse_args()

    return args

if __name__ == "__main__":
    # Get args 
    args = get_args()
    start_url = args.start_url
    depth = args.depth

    # Call crawl function 
    crawl(start_url, depth)