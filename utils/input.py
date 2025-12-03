import urllib.request


def get_input_from_gist(url: str) -> str:
    content: str = ""
    try:
        with urllib.request.urlopen(url) as resp:
            content = resp.read().decode()
    except urllib.error.URLError as e:
        print(f"Error opening gist: {e.reason}")
    finally:
        return content
