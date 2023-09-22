def posLetra(frase,letra, pos):
    '''funç̃ao posLetra que recebe como entrada uma string, uma letra, e um número que indica a
ocorrência desejada da letra,deve retornar que posiç̃ao da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que
a ocorrência pedida, a funç̃ao deve retornar -1; str, str,int-> int'''
    inicio=frase.find(letra)
    while(inicio >=0 and pos>1):
        inicio=frase.find(letra,inicio+1)
        pos=pos-1
    return inicio