def uppCons(frase):
    """retorna a frase de entrada com as consoantes
    em maiusculas
    string-->string"""
    count=0
    lista_frase=list(frase)
    tamanho_lista=lista_frase[:]
    while count<len(tamanho_lista):
        if lista_frase[count] not in 'AEIOUaeiouÁÃÀÂÉÊÍÓÕÔÒÚáãàâéêíóõôòú':
            lista_frase[count]=lista_frase[count].upper()
        count=count+1
    return ''.join(lista_frase)