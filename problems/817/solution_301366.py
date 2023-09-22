def acima_da_media(lista_notas):
    '''dada uma lista de inteiros de entrada e um número inteiro, 
    retorna outra lista, que contém todos os números da lista original
    maiores que a média dos números da lista;
    list -> list'''
    soma=sum(lista_notas)
    elementos=len(lista_notas)
    media=(soma/elementos)
    return maiores(lista_notas, media)