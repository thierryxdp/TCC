def substitui(s,x,i):
    'Função substitui posicionamento i para item x'
    if i>=0 and i<=len(s):
        return s[:i]+x+s[i+1:]