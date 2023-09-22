def posLetra(frase:str,letra:str,numero:int)->int:
    """A função recebe como parâmetro uma frase, uma letra e um número que indica a ocorrência desejada da letra. Essa função retorna a posição em que aquela ocorrência está.Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    ocorrencia = numero
    indice = 0
    resposta = -1
    while indice < len(frase) :
        if numero < str.count(frase,letra):
            resposta = resposta  + str.index(frase,letra)
        else:
            resposta 
        indice =  indice + 1
        
    return resposta