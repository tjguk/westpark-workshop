#!python3
import re

with open("all-words.txt", encoding="utf-8") as inf, open("words.txt", "w") as outf:
    for word in sorted(set(w.upper() for w in inf.read().split())):
        if re.match(r"\w{3}$", word):
            outf.write("%s\n" % word)
