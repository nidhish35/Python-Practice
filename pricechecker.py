from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import requests
from fake_useragent import UserAgent  # For fallback requests

# Function to setup Selenium WebDriver
def setup_driver():
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument(f"user-agent={UserAgent().random}")  # Random user agent to avoid blocking

    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Fallback function using requests if Selenium fails
def fallback_scrape(url):
    headers = {"User-Agent": UserAgent().random}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")
    except Exception as e:
        print(f"❌ Fallback Scraping Error: {e}")
        return None

# Function to search Amazon for the product
def search_amazon(product):
    search_url = f"https://www.amazon.in/s?k={product.replace(' ', '+')}"
    
    # Try Selenium first
    try:
        driver = setup_driver()
        driver.get(search_url)
        time.sleep(5)  # Increased wait time for dynamic content
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
    except Exception as e:
        print(f"❌ Amazon Selenium Error: {e}")
        soup = fallback_scrape(search_url)

    if not soup:
        return None

    try:
        # Updated selectors based on current Amazon structure
        product_element = soup.select_one("h2 a.s-underline-text span")
        price_element = soup.select_one("span.a-price-whole")

        if product_element and price_element:
            return {
                "name": product_element.text.strip(),
                "price": f"₹{price_element.text.strip()}",
                "url": "https://www.amazon.in" + product_element.find_parent("a")["href"]
            }
        else:
            print("\n🔴 Amazon: No product found. Debugging HTML:\n", soup.prettify()[:1000])
            return None
    except Exception as e:
        print(f"❌ Amazon Parsing Error: {e}")
        return None

# Function to search Flipkart for the product
def search_flipkart(product):
    search_url = f"https://www.flipkart.com/search?q={product.replace(' ', '+')}"
    
    # Try Selenium first
    try:
        driver = setup_driver()
        driver.get(search_url)
        time.sleep(5)  # Increased wait time for dynamic content
        soup = BeautifulSoup(driver.page_source, "html.parser")
        driver.quit()
    except Exception as e:
        print(f"❌ Flipkart Selenium Error: {e}")
        soup = fallback_scrape(search_url)

    if not soup:
        return None

    try:
        # Updated selectors based on current Flipkart structure
        product_element = soup.select_one("a.KzDlHZ, a.s1Q9rs")  # Updated class names
        price_element = soup.select_one("div.Nx9bqj")  # Updated price class

        if product_element and price_element:
            return {
                "name": product_element.text.strip(),
                "price": price_element.text.strip(),
                "url": "https://www.flipkart.com" + product_element["href"]
            }
        else:
            print("\n🔴 Flipkart: No product found. Debugging HTML:\n", soup.prettify()[:1000])
            return None
    except Exception as e:
        print(f"❌ Flipkart Parsing Error: {e}")
        return None

# Main execution
if __name__ == "__main__":
    # Install fake_useragent if not already installed: pip install fake-useragent
    try:
        product_name = input("Enter the product name: ").strip()

        print("\n🔍 Searching for:", product_name)
        
        amazon_result = search_amazon(product_name)
        flipkart_result = search_flipkart(product_name)

        print("\n📊 Price Comparison Results:\n")

        if amazon_result:
            print(f"🛒 Amazon: {amazon_result['name']}")
            print(f"💰 Price: {amazon_result['price']}")
            print(f"🔗 Link: {amazon_result['url']}\n")
        else:
            print("❌ Amazon: No results found.\n")

        if flipkart_result:
            print(f"🛍️ Flipkart: {flipkart_result['name']}")
            print(f"💰 Price: {flipkart_result['price']}")
            print(f"🔗 Link: {flipkart_result['url']}\n")
        else:
            print("❌ Flipkart: No results found.\n")

        print("✅ Done!")
    except KeyboardInterrupt:
        print("\n🛑 Search interrupted by user.")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")