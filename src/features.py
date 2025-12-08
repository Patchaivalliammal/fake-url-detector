# src/features.py
def extract_features(url):
    u = url.strip()
    host = u.split("//")[-1].split("/")[0]
    return {
        "url_len": len(u),
        "host_len": len(host),
        "dots": u.count("."),
        "digits": sum(c.isdigit() for c in u)
    }
