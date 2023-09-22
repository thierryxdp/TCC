def posLetra(frase,letra,n: str,str,int)->int:
    '''...'''
    resposta = ()
    posicao = str.index(frase,letra)*n
    i=0
    
    while i<len(frase):
        posicao