#QUESTAO 2
def uppCons(frase):
    '''Essa funcao recebe como argumento uma frase(str)
       e escaneia atraves do while e contador possiveis
       consoantes, que, utilizando-se str.upper(), transforma-as
       em maiusculas, deixando as vogais intactas.

       (list, -> list)'''
    
    qntCaracter = len(frase)
    cont = 0
    frase_nova = ""

    while cont < qntCaracter:
        if frase[cont] not in "aeiouAEIOU":
            frase_nova += frase[cont].upper()
        else:
            frase_nova += frase[cont]

        cont += 1

    return frase_nova