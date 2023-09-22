def lingua_p(palavra):
    """dada uma string palavra de entrada,
    retorna essa palavra na lingua do P,
    ou seja após cada vogal será inserida a letra P
    str --> str"""
    indice=0
    lista_letras=list(palavra)
    for letra in lista_letras:
        if letra in 'AEIOUaeiou':
            list.insert(lista_letras,indice+1,'p'+lista_letras[indice])
        indice=indice+1
    return str.join('',lista_letras)