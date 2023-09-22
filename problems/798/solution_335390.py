def freq_palavras(frase):
    """funcao que retorna um dicionario, cujas chaves sao as palavras presentes na string de entrada e os valores de acesso sao as frequencas das palavras;
    str -> dict"""
    palavras=str.split(frase, ' ')
    dicionario={}
    i=0
    while i<len(palavras):
        dicionario[palavras[i]]=list.count(palavras,palavras[i])
        i=i+1
    return dicionario