def vogal(x):
    d=list(x)
    return d
        
def lingua_p(x):
    d=[]
    letras=('a','e','i','o','u','é','ó','ô','ã''õ')
    for i in vogal(x):
        if i in letras:
            d.append(i+'p'+i)
        else:
            d.append(i)
    return ''.join(d)