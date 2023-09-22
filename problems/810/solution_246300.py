def inverte(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        s = str.lower(str.replace(s, x, " "))
    s = str.split(s)
    idx = len(s) - 1
    newList = []
    while (idx >= 0):
    newList.append(s[idx])
    idx = idx - 1
    return s