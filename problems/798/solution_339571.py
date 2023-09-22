def freq_palavra(x):
    """Dada uma funcao que recebe uma string e retorne um dicionario onde cada
    palavra dessa string e uma chave como valor o numero de vezes que a palavra
    aparece. Entrada: str,dict-->str,int"""
    s = str.split(x," ")
    b = {}
    for x in s:
        if x in s:
            b[x] = list.count(s,str(x))
    return b