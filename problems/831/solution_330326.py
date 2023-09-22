def lingua_p(palavra):
    traduzido=''
    vogal='aeiouéáú'
    for letra in palavra:
        if letra in vogal:
            traduzido=traduzido+vogal+'p'+vogal
    return traduzido