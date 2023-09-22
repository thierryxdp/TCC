def lingua_p(palavra):
    traducao=''
    vogais='aeiouAEIOUáéíóúÁÉÍÓÚ'
    for el in palavra:
        if el in vogais:
            traducao=traducao+el+'p'+el
        else:
            traducao=traducao+el
    return traducao