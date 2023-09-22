def posLetra(frase,letter,n):
    index= 0
    ocorrencia=0
    texto= list(frase)
    
    while len(frase) > index:
        if letter in texto[index]:
            ocorrencia+= 1
            if ocorrencia == n:
                return index
        index= index+=1
    if ocorrencia > n
      return -1