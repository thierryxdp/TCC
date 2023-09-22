def substitui(s,x,i):
    
    if i < 0:
        return x + s
    
    if i > len(s):
        return s + x
    
    return s[:index] + x + s[index + 1:]