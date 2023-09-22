def vogal(x):
    d=list(x)
    return d
        
def lingua_p(x):
    d=[]
    letras=('a','e','i','o','u')
    for i in vogal(x):
        if i in letras:
            d.append(i+'p')
        else:
            d.append(i)
    return ''.join(d)