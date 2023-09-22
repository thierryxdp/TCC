def poaLetra(frase,letra,numero):
    indice=0
    numocorrencias=str.count(frase,letra)
    y=0
   
    if numero > numocorrencias:
        return -1
    while indice < len(frase):
        if frase[indice] == letra :
            y= y+1
        if y==numero :
            return  str.find(frase,letra,indice)
        indice=indice+1