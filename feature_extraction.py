def extract_features(url):
    return [
        len(url),
        url.count('.'),
        int('@' in url),
        int('-' in url),
        int('https' in url),
        sum(c.isdigit() for c in url),
        url.count('/'),
        url.count('?'),
        url.count('='),
        url.count('&'),
        url.count('%'),
        url.count('_'),
        url.count('~'),
        url.count(':'),
        int('login' in url.lower()),
        int('verify' in url.lower()),
        int('account' in url.lower()),
        int('secure' in url.lower()),
        int('update' in url.lower()),
        int('bank' in url.lower())
    ]