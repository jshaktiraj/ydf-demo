import os
import requests
from bs4 import BeautifulSoup

# Function to download images from the URLs
def download_images(image_urls, folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    for i, url in enumerate(image_urls):
        try:
            image_data = requests.get(url).content
            file_path = os.path.join(folder_name, f'image_{i+1}.jpg')
            with open(file_path, 'wb') as handler:
                handler.write(image_data)
            print(f"Image {i+1} downloaded: {file_path}")
        except Exception as e:
            print(f"Failed to download image {i+1}: {e}")

# Function to scrape image URLs from Google Images using BeautifulSoup
def scrape_images(query, num_images=10):
    # Prepare the Google search URL
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"
    
    # Send an HTTP request to get the content of the search results page
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(search_url, headers=headers)
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all image elements ('img' tags)
    img_elements = soup.find_all('img')
    
    # Extract the 'src' attribute of each image tag (thumbnail URLs)
    image_urls = []
    for img in img_elements:
        src = img.get('src')
        if src and src.startswith('http'):
            image_urls.append(src)
        if len(image_urls) >= num_images:
            break

    return image_urls

if __name__ == "__main__":
    # User inputs the search query
    search_title = input("Enter the title of images you want to download: ")
    
    # Scrape image URLs from Google
    image_links = scrape_images(search_title, num_images=10)
    
    # Download images to a folder
    download_images(image_links, folder_name=search_title.replace(' ', '_'))
