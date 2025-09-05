import requests
import time

# --- online word list ---
words_url = "https://raw.githubusercontent.com/dwyl/english-words/refs/heads/master/words_alpha.txt"
response = requests.get(words_url)
if response.status_code != 200:
    print("Failed to fetch the word list")
    exit()

words = response.text.splitlines()
print(f"{len(words)} words fetched. Starting control...\n")

# --- github control ---
available = []
for i, word in enumerate(words):
    # GitHub org URL
    url = f"https://github.com/{word}"
    try:
        res = requests.get(url)
        if res.status_code == 404:
            print(f"✅ Available: {word}")
            available.append(word)
        else:
            print(f"❌ Taken: {word}")
    except Exception as e:
        print(f"⚠️ Error: {word} -> {e}")
    time.sleep(0.5)

print("\n--- RESULT ---")
print(f"Available: {len(available)}")
for w in available:
    print("-", w)
