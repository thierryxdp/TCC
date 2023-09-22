def lingua_p(palavra):
    '''retrona a traduçao da lingua p em que quando há uma vogal é adicionado a palavra p mais a vogal;
    str->str'''
    str.lower(palavra)
    traducao=''
    for letra in palavra:
        if letra in 'aeiouáéíóúâêîôûãõ':
            traducao=traducao+letra+'p'+letra
        else:
            traducao=traducao+letra
    return traducao