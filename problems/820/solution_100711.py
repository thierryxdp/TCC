def posLetra(frase,letra,n):
    """função que recebe como entrada uma string,uma letra e um numero e retorna que posição da string aquela ocorrencia da letra esta; str,str,str-->int"""
    frase1 = str.replace(frase,letra, "+", n-1)
    return str.find(frase1,letra)