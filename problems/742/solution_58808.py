def substitui(s,x,i):
    if i>0 or i>len(s):
        return "Insira um numero valido"
    else:
        return s[0:i]+x+s[i+1:]