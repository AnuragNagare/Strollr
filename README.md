
# Kids Activity Scraper

## Overview
This project is a web scraper built using Scrapy to extract data about kids' activities from a specified website. The tool collects event details such as event names, descriptions, dates, locations, and age groups, and saves the output in a CSV file for further analysis or integration.

## Project Structure

kids_activity_scraper/
├── kids_activity_scraper/
│   ├── __init__.py
│   ├── items.py
│   ├── middlewares.py
│   ├── pipelines.py
│   ├── settings.py
│   ├── spiders/
│   │   ├── __init__.py
│   │   └── kids_activity_spider.py
├── scrapy.cfg


## Installation

### Prerequisites
- Python 3.6+
- Scrapy library



## Running the Scraper

To run the spider and save the output as a CSV file, navigate to the root directory of the project and run:

scrapy crawl kids_activity -o kids_activity_data.csv


This command will start the spider, which will scrape data from the specified website and save it into `kids_activity_data.csv`.

## Code Explanation
### kids_activity_spider.py
- **`start_urls`**: The initial URL to begin scraping.
- **`parse` method**: Extracts data fields such as event name, description, date, location, and age group.
- **`extract_age_group` method**: A helper function to extract or assign a default value if age group information is not available.

### Customizations
- **Selectors**: Ensure the CSS selectors in the spider match the HTML structure of the target website.
- **Output Format**: The spider saves the data as CSV by default, but this can be changed to other formats such as JSON by altering the output command.

## Troubleshooting
- **Empty CSV File**: Ensure that the CSS selectors in the spider match the structure of the website.
- **Dynamic Content**: If the site uses JavaScript to load data, consider using Scrapy with Selenium or Splash for rendering JavaScript.

