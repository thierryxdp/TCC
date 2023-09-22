def posLetra(frase,letra,ocorrencia):
    contador=0
    cont_ocorrencia=0
    pos=0
    if letra in frase:
        while cont_ocorrencia<ocorrencia:
            if frase[contador]==letra:
                cont_ocorrencia+=1
                pos=contador
            contador+=1
        return pos
    else:
          return -1