#Problemas propostos no Machine Teaching
def filtraMultiplos(lista_de_numeros,num):
    """Dado uma lista de números e um número, retorna outra lista contendo somente os elementos da lista
    originais divisíveis por n (list[float,float,...,float],float --> list[float,float,...,float])""" """
    Essa função funciona com todos os tipos de dado númerico, exceto complex"""
    i = 0  #define-se o contador
    lista_de_multiplos = [] #cria-se o acumulador, a lista que será modificada e eventualmente retornada
    while i < len(lista_de_numeros) :   #repete-se os comandos da linha 8 a 10 enquanto i for menor que o comprimento da lista, ou seja, o processo será repetido para todos os termos da lista_de_numeros
        if lista_de_numeros[i] % num == 0 : #se o termo i da lista_de_numeros for divisível por num, é acrescentado a lista_de_multiplos o elemento i da lista_de_numeros. Caso o termo i da lista_de_numeros não seja divisível por num, à lista_de_multiplos não é adicionado nada
            lista_de_multiplos = lista_de_multiplos + [lista_de_numeros[i]]  #aqui se acrescenta um termo i da lista_de_numeros múltiplo de num
        i = i+1  #aqui se aumenta o valor do contador para repetir o processo com o próximo elemento da lista_de_numeros
    return lista_de_multiplos #aqui se retorna a lista de múltiplos pronta. Caso não haja nenhum múltiplo, essa lista será vazia