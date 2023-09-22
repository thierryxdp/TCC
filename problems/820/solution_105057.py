def posLetra(texto,letra,numero_ocorrencia):
    '''dado um texto e uma letra do mesmo a funcao
    encontra a posicao da letra no texto na devida 
    ocorrencia
    str,str,int -> int'''
    resposta = 0
    posicao = 0
    if letra not in texto:
        return -1
    while resposta < numero_ocorrencia:
        if letra in texto:           
        	posicao = texto.find(letra)
            resposta += 1
    return posicao