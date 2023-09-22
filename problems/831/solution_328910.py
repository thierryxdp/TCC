def lingua_p(palavra):
    traducao=''
    vogais='aeiouAEIOU'
    for el in palavra:
        if el in vogais:
            traducao=traducao+el+'p'+el
        else:
            traducao=traducao+el
    return traducao