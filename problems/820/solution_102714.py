def posLetra(palavra,letra,ocorrencia):
    '''funcao que retorna em qual posicao a ocorrencia 
    da letra de entrada na str palavra se encontra.
    caso a ocorrencia nao exista o retorno e -1
    str,str,int->int'''
    if str.count(palavra,letra)<ocorrencia:
        return -1
    else:
        contador = 0
        contador2 = 0
        while contador < ocorrencia:
            if palavra[contador2]==letra:
                contador = contador + 1
            contador2 = contador2 + 1
        return contador2-1