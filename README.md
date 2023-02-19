# Class Scraper

This project is a web scraper that extracts data from a web page and generates a JSON table based on a configuration file. The scraper is built in Python and uses the BeautifulSoup library for parsing HTML.

<br/>

**Motivation:**

The motivation behind this project is to provide a tool for extracting data from web pages in a flexible and customizable way. With this scraper, users can specify a configuration file that defines which HTML elements to extract data from and how to format the resulting JSON table. This allows for easy customization of the scraping process and makes it possible to extract data from a wide variety of web pages.

## Installation

Clone the repository to your local machine:

```
git clone https://github.com/kyza2/class-scraper
```

Install the prerequisites using pip:

```
pip install -r requirements.txt
```

Run the scraper with a configuration file:

```
python scrape.py <config_file>
```

## Installing dependencies

```
pip install -r requirements.txt
```

## Configuration file

Create a configuration file in JSON format that specifies the URL to scrape and how to format the resulting JSON table.

```
{
  "url": "https://www.example.com,
  "format": {
    <name>: <class_name>
    ...
  }
}
```

Run the scraper with the configuration file:

```
python scrape.py <config_file>
```

The scraper will extract data from the URL specified in the configuration file and generate a JSON table based on the format specified in the configuration file.

## Roadmap

- [ ] Support for more complex HTML parsing and extraction, such as extracting data from nested elements or elements with specific attributes.
- [ ] Support for exporting the JSON table to other formats, such as CSV or Excel.
- [ ] Support for scraping multiple pages or URLs in a single run.
- [ ] Support for scheduling periodic scrapes using a cron job or other scheduling mechanism.
