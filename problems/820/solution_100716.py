def posLetra(frase,letra,n):
    """funcao que recebe como entrada uma string, uma letra
    e um numero que indica a ocorrencia desejada da letra, e
    retorna a posicao da string que aquela ocerrencia da letra
    esta; Caso exista menos ocorrencias da letra do que a 
    ocorrencia pedida, a funcao retorna -1;
    str, str, int -> int"""
    
    l = 0
    lista = []
    if letra in frase and str.count(frase,letra)>= n:
        while l < len(frase):
            if frase[l] in frase:
                lista = lista + l
                l = l + 1
        return lista[n-1]        
    else: 
        return -1