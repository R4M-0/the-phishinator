import re

import math

def entropy(s):
    from collections import Counter
    counts = Counter(s)
    probs = [freq / len(s) for freq in counts.values()]
    return round(-sum(p * math.log2(p) for p in probs), 4)

from urllib.parse import urlparse

def extract_features(url: str) -> dict:
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path + parsed.params + parsed.query

    return {
        'url_length': len(url),
        'domain_length': len(domain),
        'path_length': len(path),
        'has_ip': int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', domain))),
        'has_at_symbol': int('@' in url),
        'count_dots': url.count('.'),
        'count_subdirs': path.count('/'),
        'has_https': int(parsed.scheme == 'https'),
        'count_digits': sum(c.isdigit() for c in url),
        'count_hyphens': url.count('-'),
        'entropy': entropy(url),
        'suspicious_words': int(any(w in url.lower() for w in ['login', 'secure', 'verify', 'update', 'signin', 'bank', 'account'])),
        'long_domain': int(len(domain) > 30),
        'starts_with_http': int(url.startswith("http")),
    }
