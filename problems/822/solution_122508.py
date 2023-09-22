def repetidos(lista_de_numeros):
    """Recebe como entrada uma lista de números e retorna o número de vezes que um elemento da lista é igual ao
    elemento anterior (list[float,float,....,float] --> int)""" """A função funciona com o todos os tipos numéricos"""
    i = 1 #define-se o contador
    numero_de_vezes = 0 #define-se o acumulador, o número de vezes que um elemento da lista é igual ao elemento anterior
    while i < len(lista_de_numeros) : #repete-se os comandos da linha 7 a 9 enquanto i for menor que o comprimento da lista_de_numeros, ou seja, o processo será repetido para todos os elementos de lista_de_numeros
        if lista_de_numeros[i] == lista_de_numeros[i-1] : #checa-se se o elemento i da lista_de_numeros é igual ao elemento anterior (começa-se a checar pelo segundo elemento)
            numero_de_vezes = numero_de_vezes+1 #se o elemento i é igual ao elemento anterior, é somado 1 ao numero_de_vezes
        i= i+1 #aqui se aumenta o valor do contador para repetir o processo com o próximo elemento da lista_de_numeros
    return numero_de_vezes #retorna o número de vezes que um elemento da lista é igual ao elemento anterior