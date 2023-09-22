def posLetra(frase, letra, ocorrencia):
    '''A funcao recebe tres argumentos, frase, letra e ocorrencia
       Eh feita uma analise da quantidade de caracteres da frase
       e depois, com o auxilio do while e de contadores, retorna-se
       em qual posicao estah a letra na ocorrencia desejada.
       Caso a ocorrencia desejada seja maior que a aparicao da letra
       na frase, retorna-se -1.

       (str, str, int -> int)'''
    
    qntCaracter = len(frase)
    cont = 0
    cont_letra = 0

    if frase.count(letra) < ocorrencia:
        return -1

    while cont < qntCaracter:
        if frase[cont] == letra:
            cont_letra += 1
            if cont_letra == ocorrencia:
                return cont
        cont += 1