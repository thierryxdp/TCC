def posLetra(frase, letra, numero):
    '''função que retorna em que posição da string a ocorrencia da letra pedida está; str, str, int -> int'''
    lista = []
    i = 0
    while i < len(frase):
        if letra in frase[i]:
            list.append(lista,letra)
        if len(lista) >= numero:
            return i
        i = i + 1
        if len(letra) < numero:
            return -1