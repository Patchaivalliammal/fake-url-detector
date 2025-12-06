def extract_features(url):
    url = url.strip()
    return {
        "url_len": len(url),
        "host_len": len(url.split("//")[-1].split('/')[0]),
        "dots": url.count("."),
        "digits": sum(c.isdigit() for c in url)
    }
