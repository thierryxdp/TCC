def posLetra(frase,letra,numero):
    """função que dada uma frase, letra e numero que indica uma ocorrencia, retorne em qual posição da frase a ocorrencia da letra esta; string,string,int-->int"""
    if frase.count(letra)<numero:
        return -1
    i=0
    n=0
    while n!=numero:
        if letra==frase[i]:
            posOcorrencia=i
            n+=1
            i+=1
        return posOcorrencia