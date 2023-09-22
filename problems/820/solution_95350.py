def posLetra(frase, letra, posi):
    ''' Recebe recebe como entrada uma string, uma letra, e um n ́umero que indica a
    ocorrˆencia desejada da letra.
    str,str,int -> int'''
    lista = list(frase)
    return lista.index(posi,letra