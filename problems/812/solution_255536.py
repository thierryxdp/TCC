import re

s = "string. With. Punctuation?"
out = re.sub(r'[^\w\s]','',s)
print(out)