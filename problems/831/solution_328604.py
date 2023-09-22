def lingua_p(palavra):
    """"""
    """"""
    traducao=''
    for letra in palavra:
        if letra in 'aeiouAEIOUáàâãéíóôõú':
            traducao+letra+'p'+letra
        else:
            traducao+letra
    return traducao