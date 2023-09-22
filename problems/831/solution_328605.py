def lingua_p(palavra):
    """"""
    """"""
    traducao=''
    for letra in palavra:
        if letra in 'aeiouAEIOUáàâãéíóôõú':
            traducao=traducao+letra+'p'+letra
        else:
            traducao=traducao+letra
    return traducao