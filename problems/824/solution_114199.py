def uppCons(texto):
    '''função recebe texto e retorna o mesmo texto 
    com as consoantes em maiúsculo.
    str--> str'''
    lista_texto = list(texto)  #quebra a string texto e coloca em uma lista
    contador = 0 #inicia o contador 
    letras = []  #abre uma lista vazia    

    while contador < len(lista_texto):  #enquanto contador for menor que lista com o texto
        if lista_texto[contador] in 'çbcdfghjklmnpqrstvwxyz':  #se elemento da lista com o texto for consoante
            letras.insert(contador, lista_texto[contador].upper())  #insere elemento em maiúsculo na lista letras
            
            contador = contador + 1  #incrementa contador

        else:  #se não for consoante
            letras.insert(contador, lista_texto[contador])  #insere elemento do texto na lista letras

            contador = contador + 1  

    return ''.join(letras)  #junta os elementos da lista letras e retorna string