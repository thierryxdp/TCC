def lingua_p(palavra):
    """funcao que recebe uma palavra em portugues e retorna essa mesma palavra traduzida em lingua do p.
    str->str"""
    lista=list(str.lower(palavra)
    lista_p=[]
    for letra in lista:
        if letra in "aeiouâêîôûáéíóúãõàèìòù":
               letra=letra+'p'+letra
        list.append(lista_p,letra)
               return ''.join(lista_p)