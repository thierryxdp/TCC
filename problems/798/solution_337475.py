def freq_palavras(x):
    """Função que dado uma string, retorna um dicionário onde cada palavra da string é uma chave e tenha como valor o número de vezes que aparece."""
    resposta={}
    i=0
    palavras=x.split()
    while i<len(palavras):
        n=list.count(palavras,palavras[i])
        resposta[palavras[i]]=n
        i+=1
    return resposta