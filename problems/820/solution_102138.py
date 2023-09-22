def posLetra(palavra,letra,numero):
    'dado uma string,uma letra e um numero retorne a posição da letra na palavra dado o numero de ocorrencia.str,str,int-->int'
    indice=0
    ocorrencia=0
    while indice<len(frase) and ocorrencia<numero:
        if palavra[indice]==letra:
            ocorrencia=ocorrencia+1
        indice=indice+1 
    return ocorrencia