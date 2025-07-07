import re

text = "Line1\n# This is a comment line\nLine2\nSome text # not a comment\n# Another comment line"
matches = re.findall(r'\n#.*', text)
print(matches)