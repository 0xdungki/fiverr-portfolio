#!/usr/bin/env python3
"""
Web Scraper Demo - Fiverr Portfolio
Scrapes product data from example e-commerce site and exports to CSV/JSON
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import logging
from datetime import datetime
from typing import List, Dict

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ProductScraper:
    """Scrapes product information from e-commerce websites"""
    
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def scrape_products(self, max_pages: int = 3) -> List[Dict]:
        """Scrape products from multiple pages"""
        products = []
        
        for page in range(1, max_pages + 1):
            logger.info(f"Scraping page {page}...")
            page_products = self._scrape_page(page)
            products.extend(page_products)
            logger.info(f"Found {len(page_products)} products on page {page}")
        
        logger.info(f"Total products scraped: {len(products)}")
        return products
    
    def _scrape_page(self, page: int) -> List[Dict]:
        """Scrape a single page"""
        try:
            url = f"{self.base_url}?page={page}"
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            products = []
            
            # Example: scraping product cards
            # Adjust selectors based on actual website structure
            for item in soup.select('.product-card'):
                product = {
                    'name': item.select_one('.product-name').text.strip(),
                    'price': item.select_one('.product-price').text.strip(),
                    'rating': item.select_one('.product-rating').text.strip(),
                    'url': item.select_one('a')['href'],
                    'scraped_at': datetime.now().isoformat()
                }
                products.append(product)
            
            return products
            
        except Exception as e:
            logger.error(f"Error scraping page {page}: {e}")
            return []
    
    def export_to_csv(self, products: List[Dict], filename: str = 'products.csv'):
        """Export products to CSV file"""
        if not products:
            logger.warning("No products to export")
            return
        
        keys = products[0].keys()
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(products)
        
        logger.info(f"Exported {len(products)} products to {filename}")
    
    def export_to_json(self, products: List[Dict], filename: str = 'products.json'):
        """Export products to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(products, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Exported {len(products)} products to {filename}")


def main():
    """Main execution"""
    # Example usage
    scraper = ProductScraper('https://example.com/products')
    
    # Scrape products
    products = scraper.scrape_products(max_pages=3)
    
    # Export to both formats
    scraper.export_to_csv(products, 'products.csv')
    scraper.export_to_json(products, 'products.json')
    
    # Print summary
    print(f"\n✅ Scraping complete!")
    print(f"📊 Total products: {len(products)}")
    print(f"📁 Files created: products.csv, products.json")


if __name__ == '__main__':
    main()
