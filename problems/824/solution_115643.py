def uppCons(frase):
    'retorna todas as consoantes maiusculas dada uma frase; list->list'
    con= 'mnbvcxzçlkjhgfdsqwrtyp'
    a=0
    while a< len(con):
        frase=frase.replace(con[a],con[a].upper())
        a=a+1
    return frase