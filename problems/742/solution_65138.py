def substitui(s: str,x,i: int):
    0<= i <= len(s)
    if i=0:
        return str(x) + s[1:]
    elif i= len(s):
        return s[0:-2] + str(x)
    elif 0< i< len(s):
        return s[0: i] + s[(i+1):-1]
    endif