def inverte(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        s = str.lower(str.replace(s, x, " "))
    s = str.split(s)
    idx = len(s) - 1
    c = []
    while (idx >= 0):
    c = c.append(s[idx])
    idx = idx - 1
    return s