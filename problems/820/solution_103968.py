def posLetra(frase,letra,num):
    ocorrencia=0
    indice=0
    while ((ocorrencia<num)and(indice<len(frase):
         indice=frase.find(letra,indice)
         if indice!=-1:
              ocorrencia=ocorrencia+1
              indice = indice+1
    if indice!=len(frase):
        if indice==-1:
             return indice
        else:
             return indice-1
    else:
         indice=-1
         return indice