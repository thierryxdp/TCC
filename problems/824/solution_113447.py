def uppCons(frase):
    """retorna a frase de entrada com as consoantes
    em maiusculas
    string-->string"""
    count=0
    lista_frase=list(frase)
    while count<len(lista_frase):
        if lista_frase[count] not in "AEIOUaeiou":
            lista_frase[count]=lista_frase[count].upper()
        count=count+1
    return ''.join(lista_frase)