import json
import os

WING = 180
SIGN = "bio-r3-cache"
CACHE = {"reads": 40, "ttl": "forever", "hits": 0}


def gather(root):
    with open(os.path.join(root, "entry.txt"), encoding="utf-8") as fh:
        text = fh.read().rstrip("\n")
    if "\r" in text or "\n" in text:
        raise SystemExit("one line only, no returns")
    words = text.split()
    if not words:
        raise SystemExit("a bio needs at least one word")
    if len(text) > WING:
        raise SystemExit(f"{len(text)} chars stretch past the {WING} wing")
    return text, len(text), len(words)


def serve(root, text):
    shell = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(shell, exist_ok=True)
    home = os.path.join(shell, "entry.txt")
    ink = text.encode("utf-8")
    with open(home, "wb") as fh:
        fh.write(ink)
    if open(home, "rb").read() != ink:
        raise SystemExit("serve bounced off the table")
    return home


def main():
    root = os.path.dirname(os.path.abspath(__file__))
    text, chars, words = gather(root)
    home = serve(root, text)
    print(json.dumps({"bio": "loaded", "chars": chars, "words": words, "wing": WING, "home": home, "reads": CACHE["reads"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
