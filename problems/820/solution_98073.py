def posLetra(string,letra,numero):
    """A função recebe uma string, uma letra, e um número
    que indica a ocorrência desejada da letra. Ela deve
    retornar em que posição da string aquela letra em 
    questão está. Caso exista menos ocorrências da letra
    do que a ocorrência pedida(numero), a função retornará
    -1.
    Entrada: String,String,Int
    Saída: Int"""
    
    
    posicao=string.find(letra)
    while numero>1 and posicao>=0:
        posicao=frase.find(letra,posicao+1)
        numero-=1
    return posicao