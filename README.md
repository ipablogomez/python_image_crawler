# python_image_crawler
This is a simple web crawler written in Python that crawls a given URL and its links up to a given depth, extracts images from the pages, and saves the results into a JSON file

## Installation
To install the dependencies, run the following command:  
```
pip install -r requirements.txt
```

## Usage
To run the web crawler, use the following command:
```
python crawler.py <start_url> <depth>
```
- `start_url`: The URL to start crawling from.
- `depth`: The maximum depth to crawl to.
The results will be saved into a results.json file in the following format:
```
{
    "results": [
        {
            "imageUrl": "string",
            "sourceUrl": "string",
            "depth": "number"
        }
    ]
}
```

The crawling activity will be logged to a file named crawler.log.

## Example
To crawl the https://en.wikipedia.org/wiki/Web_crawler website up to a depth of 1 and save the results into a file named example_results.json, use the following command:

```
python crawler.py https://en.wikipedia.org/wiki/Web_crawler 0
```