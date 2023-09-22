def substitui (string1,x,i):
    string1[i] = x
    return string1[0:i] + x + string1[i + 1:]