def inverte(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        s = str.lower(str.replace(s, x, " "))
    s = str.split(s)
    s = reversed(s)
    s = str.join(" ",s)
    return s