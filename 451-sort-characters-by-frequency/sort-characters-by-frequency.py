from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        sorted_chars = sorted(counts.items(), key=lambda x: -x[1])
        return ''.join(ch * freq for ch, freq in sorted_chars)