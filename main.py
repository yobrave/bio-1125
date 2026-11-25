"""AI dating bio exporter with paired-gate check, build 4."""
import json
import os
import pathlib

BIO_CAP = 180
CODE_NAME = "bio4-agent-bio-r4"


def pull():
    return (pathlib.Path(__file__).resolve().parent / "entry.txt").read_text(encoding="utf-8").strip()


def judge(n):
    return 1 <= n <= BIO_CAP


def push(body):
    out = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_text(body + "\n", encoding="utf-8", newline="\n")


def go():
    body = pull()
    n = len(body)
    push(body)
    print(json.dumps({"code": CODE_NAME, "n": n, "judge": judge(n), "cap": BIO_CAP, "build": 4}))


go()
