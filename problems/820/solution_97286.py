def posLetra(string, letra, num):
    """Funcao que retorna em que posicao da string na ocorrencia desejada
    da letra esta; str,str,int -> int"""
    
    posicao = str.find(string,letra)
    
    while str.find(string,letra) != -1 and num > 1:
        posicao = str.find(string,letra,posicao+1)
        num = num - 1
    return posicao