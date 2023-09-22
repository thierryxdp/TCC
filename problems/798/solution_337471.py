def freq_palavras(x):
    """Função que dado uma string, retorna um dicionário onde cada palavra da string é uma chave e tenha como valor o número de vezes que aparece."""
    resposta={}
    i=0
    while i<len(x):
        n=str.count(x,x[i])
        resposta[x[i]]=n
        i+=1
    return resposta