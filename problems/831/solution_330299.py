def lingua_p(palavra):
    traduzido=''
    vogal='aeiouéáú'
    for letra in palavra:
        if letra in vogal:
            traduzido=traduzido+letra+'p'+letra+vogal
    return traduzido