def filtraMultiplos (lista_de_algarismos, numero):

    """Desejamos ter uma função que, analogamente à função filtra pares,
        filtre agora os múltiplos de qualquer número fornecido pela função
        de uma lista também fornecida.

        list, int -> list
    """

    multiplos=[]
    i = 0

    while i<len(lista_de_algarismos):
        if (lista_de_algarismos[i] % numero == 0):
            
            multiplos = multiplos + [lista_de_algarismos[i]]
        i = i + 1
        
    return multiplos