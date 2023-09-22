def lingua_p(palavra):
    traducao=''
    vogais='aeiouAEIOUáéíóúÁÉÍÓÚ'
    for letra in palavra:
        if letra in vogais:
            traducao=traducao+letra+'p'+letra
        else:
            traducao=traducao+letra
    return traducao