def posLetra(frase, letra , n):
    i=0
    qnt=[]
    frase=[frase]
    while  i < len(frase):           
        if frase[i:i+1] == letra:
            return  [list.index(frase,letra,n)]