def inverte(frase):
    """ pega string, deixa caixa baixa, retira
    acentos, inverte e depois transforma em string
    novamente. string -> string """
    frase = str.lower(frase)
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, ',', ' ')
    lista = str.split(frase)
    lista_nova = lista[::-1]
    lista_nova2 = ' '.join(lista_nova)
    return lista_nova2