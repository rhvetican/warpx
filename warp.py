import re
import requests
import random

SOURCES = [
    "https://t.me/s/warpplus",
    "https://t.me/s/warppluscn"
]

PATTERN = re.compile(r"<code>([A-Za-z0-9-]+)</code>")

def main():
    keys = set()

    for url in SOURCES:
        print(f"Currently searching in {url}...")
        response = requests.get(url)
        response.raise_for_status()
        body = response.text

        for match in PATTERN.finditer(body):
            key = match.group(1)
            keys.add(key)

    with open("full.txt", "w") as full_file, open("lite.txt", "w") as lite_file:
        keys_list = list(keys)
        if keys_list:
            print("Selecting keys...")
            full_keys = random.sample(keys_list, min(150, len(keys_list)))
            lite_keys = random.sample(keys_list, min(75, len(keys_list)))

            full_file.write("\n".join(full_keys) + "\n")
            lite_file.write("\n".join(lite_keys) + "\n")

if __name__ == "__main__":
    main()
