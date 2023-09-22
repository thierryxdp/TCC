def inverte(s):
    a = [".","_", "-", ",", ";", ":","/","?","!"]
    for n in range(len(a)):
        x = a[n]
        s = str.lower(str.replace(s, x, " "))
    s = reverse(str.split(s))
    return s