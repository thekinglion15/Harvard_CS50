import re
import sys

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'.+src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9A-Z]+)"'
    match = re.search(pattern, s)

    if match:
        return "https://youtu.be/" + match.group(1)
    else:
        return None

if __name__ == "__main__":
    main()