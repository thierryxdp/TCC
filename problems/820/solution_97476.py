def posLetra(frase,letra,numero):
    """função que dada uma frase, letra e numero que indica uma ocorrencia, retorne em qual posição da frase a ocorrencia da letra esta; string,string,int-->int"""
    if frase.count(letra)<numero:
        return -1
    a=0
    x=0
    while x!=numero:
        if letra==frase[a]:
            posOcorrencia=a
            x+=1
        a+=1
        return posOcorrencia