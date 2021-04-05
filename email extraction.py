import re
str = input()
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
match = re.search(pattern, str)
if match:
    print(match.group())
