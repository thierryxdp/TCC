def uppCons(frase):
    con= 'mnbvcxzçlkjhgfdsqwrtyp'
    a=0
    while a< len(con):
        frase=frase.replace(con[a],con[a].upper())
        a=a+1
    return frase