def posLetra(frase:str,letra:str,numero:int)->int:
    """A função recebe como parâmetro uma frase, uma letra e um número que indica a ocorrência desejada da letra. Essa função retorna a posição em que aquela ocorrência está.Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deve retornar -1"""
    ocorrencia = numero
    indice = 0
    resposta = 0
    while numero > str.count(frase,letra):
        if letra in frase:
            resposta = resposta  + 2
        else:
            resposta = resposta - 1
        indice =  indice + 1
        
    return resposta