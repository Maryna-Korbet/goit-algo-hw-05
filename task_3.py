import timeit
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
algorithms = {"KMP": kmp_search, "BM": bm_search, "RK": rk_search}
results = {}

results = {
    "Article 1": {
        "Existing": {
            "Boyer-Moore": timeit.timeit(lambda: bm_search(text1, existing_substring), number=10),
            "Knuth-Morris-Pratt": timeit.timeit(lambda: kmp_search(text1, existing_substring), number=10),
            "Rabin-Karp": timeit.timeit(lambda: rk_search(text1, existing_substring), number=10),
        },
        "Non-Existing": {
            "Boyer-Moore": timeit.timeit(lambda: bm_search(text1, non_existing_substring), number=10),
            "Knuth-Morris-Pratt": timeit.timeit(lambda: kmp_search(text1, non_existing_substring), number=10),
            "Rabin-Karp": timeit.timeit(lambda: rk_search(text1, non_existing_substring), number=10),
        },
    },
    "Article 2": {
        "Existing": {
            "Boyer-Moore": timeit.timeit(lambda: bm_search(text2, existing_substring), number=10),
            "Knuth-Morris-Pratt": timeit.timeit(lambda: kmp_search(text2, existing_substring), number=10),
            "Rabin-Karp": timeit.timeit(lambda: rk_search(text2, existing_substring), number=10),
        },
        "Non-Existing": {
            "Boyer-Moore": timeit.timeit(lambda: bm_search(text2, non_existing_substring), number=10),
            "Knuth-Morris-Pratt": timeit.timeit(lambda: kmp_search(text2, non_existing_substring), number=10),
            "Rabin-Karp": timeit.timeit(lambda: rk_search(text2, non_existing_substring), number=10),
        },
    },
}

# Output of results
print(results)

