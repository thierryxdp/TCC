def lingua_p(palavra):
    '''Traduz uma palavra para a lingua do P;
    str -> str'''
    minuscula = str.lower(palavra)#Deixa todas as letras da palavra minusculas
    lista = list(minuscula)#Cria uma lista com cada letra da palavra
    letra = 0#Letra a ser testada
    indice = 0#indice da letra
    for letra in lista:
        if letra in 'aeiouáéíóú': 
            lista.insert(indice + 1,'p' + letra)#Insere p mais a letra no indice depois da letra 
        indice = indice + 1
    return ''.join(lista)