def posLetra(frase,letra,num):
    '''Crie uma função que receba uma string, uma letra, e um n
    úmero que indica a ocorrência desejada da letra, e retorne 
    em que posição da string aquela ocorrência da letra está. 
    Caso exista menos ocorrências da letra do que a ocorrência
    pedida, a função deve retornar -1. Sendo str,str,int-->int.'''
    contagem=str.count(frase,letra)
    posicao=0
    indice=-1
    if num == contagem:
        return frase.rfind(letra)
    elif 0<num<contagem:
        while posicao != num:
            indice=indice+1
            if frase[indice] == letra:
                posicao=posicao+1
        return indice
    elif not 0<num<=contagem:
        return -1