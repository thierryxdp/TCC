def acima_da_media(lista):
    """função recebe lista e retorna lista ordenada
    list--> list"""
    media = int(sum(lista) / len(lista)) 
    #faz a divisão entre a soma de todos os elementos da lista e o tamanho da lista e atribui  a uma variável qualquer
    #retorna chamando a função maiores e usa como parâmetros a lista e variável qualquer da divisão 
    return maiores(lista, media)