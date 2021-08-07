import re
import entropy
import math
from Levenshtein import distance
import sys
import brandseg
from confusables import unconfuse
from suspicious import tlds, brands, popular_keywords
sys.path.append("../../Common/utils")
from domain_tools import get_fqdn, get_path, get_query, get_scheme

def get_features_one_url(url, bseg):
    features = dict()
    features["url"] = url
    features["protocol"] = get_scheme(url)
    fqdn = get_fqdn(url)
    query = get_query(url)
    path = get_path(url)
    features["num_queries"] = 0
    if query != None and query != "":
        features["num_queries"] = len(query.split('&'))
    features["path_depth"] = 0
    if path != None and path != "":
        features["path_depth"] = len(path.split('/'))
    features_dom = get_features_one(fqdn, bseg)
    for key, value in features_dom.items():
        features[key] = value
    return features

def get_features_one(domain, bseg):
    features = dict()
    features["domain"] = domain

    #segment the brand
    res = bseg.segment_domain(domain)
    sub_words = res[0]
    dom_words = res[1]
    all_words = sub_words + dom_words
    tld = res[2]

    # Suspicious TLD
    features["suspicious_tld"] = 0
    for t in tlds:
        if t == tld:
            features["suspicious_tld"] = 1
            break

    features["length"] = len(domain)

    # Entropy
    # Higher entropy is kind of suspicious
    features["entropy"] = entropy.shannon_entropy(domain)

    # IDN characters
    domain = unconfuse(domain)

    # Contains embedded TLD/ FAKE TLD
    features["fake_tld"] = 0
    #exclude tld
    for word in all_words:
        if word in ['com', 'net', 'org', 'edu', 'mil', 'gov', 'info', 'asia']:
            features["fake_tld"] += 1

    # No. of popular brand names appearing in domain name
    features["brand"] = 0
    for br in brands:
        for word in all_words:
            if br in word:
                features["brand"] += 1

    # Appearance of popular keywords
    features["pop_keywords"] = 0
    for word in popular_keywords:
        if word in all_words:
            features["pop_keywords"] += 1

    # Testing Levenshtein distance for keywords
    # Let's go for Levenshtein distance less than 2
    features["similar"] = 0
    for br in brands:
        # Removing too generic keywords (ie. mail.domain.com)
        for word in [w for w in all_words if w not in ['email', 'mail', 'cloud']]:
            if distance(str(word), str(br)) <= 2:
                features["similar"] += 1

    # Deeply nested subdomains (ie. www.paypal.com.security.accountupdate.gq)
    features["num_subdomains"] = domain.count('.') - 1

    return features

def get_features(domains):
    bs = brandseg.BrandSeg()
    features = []
    for domain in domains:
        features.append(get_features_one(domain, bs))
    return features

def get_features_urls(urls):
    bs = brandseg.BrandSeg()
    features = []
    for url in urls:
        features.append(get_features_one_url(url, bs))
    return features

if __name__ == "__main__":
    sample = ["www.paypal.com.security.accountupdate.gq", 
              "apple-com.evil.com",
              "bbc.co.uk",
              "apply-paypal-icloud.com"]
    print(get_features(sample))
