def posLetra(frase,letra,b):
    """funcao que recebe como e que recebe como entrada uma string, uma letra, e um numero que indica a
ocorrencia desejada da letra, que retorne em que posicao da string aquela ocorrencia da letra esta.E que caso exista menos ocorrencias da letra do que a ocorrencia pedida, a funcao deve retornar -1. str, str, int-> int"""
    frase1 = str.replace(frase,letra,'+',b-1)
    return str.find(frase1,letra)