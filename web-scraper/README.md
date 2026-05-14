# Web Scraper Demo

Professional web scraping tool with data export capabilities.

## Features

✅ **Multi-page scraping** - Automatically scrapes multiple pages
✅ **Error handling** - Robust error handling and logging
✅ **Multiple export formats** - CSV and JSON output
✅ **Clean code** - Well-documented and maintainable
✅ **Rate limiting** - Respects website resources

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from scraper import ProductScraper

# Initialize scraper
scraper = ProductScraper('https://example.com/products')

# Scrape products
products = scraper.scrape_products(max_pages=3)

# Export data
scraper.export_to_csv(products, 'output.csv')
scraper.export_to_json(products, 'output.json')
```

## Example Output

```json
[
  {
    "name": "Product Name",
    "price": "$99.99",
    "rating": "4.5/5",
    "url": "https://example.com/product/123",
    "scraped_at": "2026-05-14T18:10:00"
  }
]
```

## Customization

Easily customize for any website by modifying the CSS selectors in `_scrape_page()` method.

## Use Cases

- Price monitoring
- Product catalog extraction
- Market research
- Competitor analysis
- Data aggregation

---

**Need a custom scraper?** Contact me on Fiverr: @dungki_dev
