def posLetra (frase,letra,ocorr):
    '''função que dada uma frase, uma letra, 
       verifica o indice da letra na informada ocorrencia
       str,str,int->int'''
    i=0
    lista=[]

    while i < len(frase):
        

        indice=frase.find(letra,i)

        if indice not in lista and indice!=-1:
            lista.append(indice)
        elif frase.find(letra)==-1:
            break
          
        i+=1

    if ocorr <=len(lista):
        return lista[ocorr-1]
    else:
        return -1