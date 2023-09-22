def posLetra(frase,letra,n):
    '''Função que recebe uma str(frase), outra str(letra);
e um int(n) indicando a ocorrência desejada da letra.
Retorna em que posição da frase a ocorrência da letra está.
Caso exista menos ocorrências que a indicada, retorna -1.
str, str, int-> int'''
    p = frase.find(letra)
    while p>=0 and n>1:
        p = frase.find(letra, p +1)
        n-=1
    return p