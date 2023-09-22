def lingua_p(palavra):
    traduzido=''
    vogal='aeiouéáú'
    for letra in palavra:
        if letra in vogal:
            traduzido=traduzido+letra+'p'+letra
        if letra not in vogal:
            traduzido=traduzido+letra
    return traduzido