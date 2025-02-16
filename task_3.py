import timeit
import csv
from typing import List

# Knuth-Morris-Pratt algorithm (KMP)
def compute_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text: str, pattern: str) -> int:
    lps = compute_lps(pattern)
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == len(pattern):
            return i - j
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

# Boyer-Moore algorithm (BM)
def bm_search(text: str, pattern: str) -> int:
    m, n = len(pattern), len(text)
    if m == 0: return -1
    bad_char = {pattern[i]: i for i in range(m)}
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1

# Rabin-Karp algorithm (RK)
def rk_search(text: str, pattern: str, prime: int = 101) -> int:
    m, n = len(pattern), len(text)
    if m == 0: return -1
    base = 256
    h, p_hash, t_hash = pow(base, m - 1, prime), 0, 0
    for i in range(m):
        p_hash = (base * p_hash + ord(pattern[i])) % prime
        t_hash = (base * t_hash + ord(text[i])) % prime
    for i in range(n - m + 1):
        if p_hash == t_hash and text[i:i+m] == pattern:
            return i
        if i < n - m:
            t_hash = (base * (t_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if t_hash < 0:
                t_hash += prime
    return -1

# Читання текстів
with open("article1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()
with open("article2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()

# Test substrings
existing_substring = "якщо середній елемент – цільовий елемент"
non_existing_substring = "якщо СУРЕДНІй елемент – цільовий елемент" 

# Time measurement
results = []
articles = {"Article 1": text1, "Article 2": text2}
patterns = {"Existing": existing_substring, "Non-Existing": non_existing_substring}
algorithms = {"Boyer-Moore": bm_search, "Knuth-Morris-Pratt": kmp_search, "Rabin-Karp": rk_search}

for article_name, text in articles.items():
    for pattern_type, pattern in patterns.items():
        for algo_name, algo in algorithms.items():
            time_taken = timeit.timeit(lambda: algo(text, pattern), number=10)
            results.append([article_name, pattern_type, algo_name, time_taken])

# Write results to CSV
with open("results.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Article", "Pattern Type", "Algorithm", "Time (s)"])
    writer.writerows(results)

# Write results to Markdown
with open("results.md", "w", encoding="utf-8") as mdfile:
    mdfile.write("# Comparison of substring search algorithms\n\n")
    mdfile.write("| Article | Pattern Type | Algorithm | Time (s) |\n")
    mdfile.write("|--------|-------------|----------|---------|\n")
    for row in results:
        mdfile.write(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]:.6f} |\n")


print("Results saved to results.csv and results.md")
