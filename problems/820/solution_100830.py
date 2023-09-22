def posLetra(string,letra,n):
    """retorna a posicao da ocorrencia n da letra na string
    retorna -1 caso haja menos ocorrencias do que o informado;
    str,str,int -> int"""
    i=0
    
    if str.count(string,letra)<n:
        return -1
        
    while i<len(string):
        if string[i]==letra