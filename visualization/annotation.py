import requests
from collections import defaultdict

def fetch_and_print_grid(url):
    # Fetch the content of the Google Doc
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch the document. HTTP status code: {response.status_code}")
    
    # Split the document content into lines
    lines = response.text.splitlines()
    
    # Parse the data into a list of (x, y, character) tuples
    grid_data = []
    i = 0
    while i < len(lines):
        try:
            x = int(lines[i])
            char = lines[i + 1]
            y = int(lines[i + 2])
            grid_data.append((x, y, char))
            i += 3
        except (ValueError, IndexError):
            raise Exception("Error parsing the document. Ensure the format matches the expected input.")
    
    # Determine the size of the grid
    max_x = max(data[0] for data in grid_data)
    max_y = max(data[1] for data in grid_data)
    
    # Initialize a 2D grid with spaces
    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    
    # Fill the grid with characters based on the coordinates
    for x, y, char in grid_data:
        grid[y][x] = char
    
    # Print the grid row by row
    for row in grid:
        print("".join(row))

# Example usage: Provide the URL to the Google Doc as plain text
google_doc_url = "YOUR_GOOGLE_DOC_https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
fetch_and_print_grid(google_doc_url)