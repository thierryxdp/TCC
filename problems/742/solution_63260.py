def substitui(s,x,i):
    string = s.split()
    string.remove(s[i])
    string.insert(x,i)
    return string