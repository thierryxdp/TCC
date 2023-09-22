def repetidos(lista): #Recebe uma lista de numeros
    contador = 0
    ponteiro = 0
    while ponteiro < len(lista):
        if ponteiro == 0:
            ponteiro = ponteiro + 1
        if lista[ponteiro] == lista[ponteiro - 1]: #Compara o número com seu antecessor
            contador = contador + 1
        ponteiro = ponteiro + 1
    return contador #Retorna o número de vezes que um número é igual ao seu antecessor