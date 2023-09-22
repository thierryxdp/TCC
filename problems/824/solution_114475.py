def uppCons(string):
    '''funcao que retorna uma string
    com todas as vogais dadas uma frase
    como parametro
    entrada: string
    saida: string
    '''
    lista_string= list(string)
    indice= 0
    vogais= ''
    while indice<len(lista_string):
        if lista_string[indice] not in "aeiou":
            lista_string= lista_string[indice].upper()
        indice= indice + 1
    return ''.join(lista_string)