def posLetra(texto,letra,ocorrencia):
    '''função que retorna a posição da string que a ocorrência da letra se
    encontra no texto
    str, str, int -> int'''
    contagem = str.count(texto,letra)
    if contagem >= ocorrencia:
        posicao_proximo = 0
        i = 0
        while i < ocorrencia:
            resultado = str.find(texto,letra,posicao_proximo)
            posicao_proximo = str.find(texto,letra) + 1
            i += 1
        return resultado
    else:
        return -1