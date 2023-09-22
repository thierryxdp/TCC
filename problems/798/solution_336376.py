def freq_palavras(frase):
    """Funçao que recebe uma string e retorna um dicionário onde cada palavra dessa string seja uma chave e tenha como valor o número de vezes que a palavra aparece
    entrada: str
    saída: dict"""
    frase_modificada=str.split(frase)
    dicionario_final={}
    for palavra in frase_modificada:
        if palavra in dicionario_final:
            dicionario_final[palavra]+=1
        else:
            dicionario_final[palavra]=1
    return dicionario_final