from playwright.sync_api import sync_playwright

SEEDS = list(range(89, 99))  # 89 to 98

def scrape_seed(seed):
    url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
    total = 0

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)

        # Wait for tables to load
        page.wait_for_selector("table")

        # Get all numbers inside table cells
        cells = page.query_selector_all("td")

        for cell in cells:
            text = cell.inner_text().strip()
            if text.isdigit():
                total += int(text)

        browser.close()

    return total


if __name__ == "__main__":
    grand_total = 0

    for seed in SEEDS:
        seed_total = scrape_seed(seed)
        print(f"Seed {seed} total = {seed_total}")
        grand_total += seed_total

    print("\nFINAL TOTAL =", grand_total)
