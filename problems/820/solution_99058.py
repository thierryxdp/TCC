def posLetra(frase,letra,num):
    """funcao que, dada uma frase, uma letra e um numero que indica a ocorrencia da letra, retorna em que posicao da string frase aquela ocorrencia esta. Caso nao exista tantas ocorrencias quanto  a ocorrencia pedida, retorna -1
    str,str,int--->int"""
    i=0
    if letra not in frase or num>str.count(frase,letra):
        return -1
    ocorrencia=0
    while i<len(frase):
        if frase[i]=letra:
            ocorrencia=ocorrencia+1
        i=i+1
    return ocorrencia