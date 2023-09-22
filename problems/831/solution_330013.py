def lingua_p (palavra):
    '''Recebe como parâmetro uma palavra em português e retorne 
    a mesma palavra traduzida para a língua do P;
    str -> str'''
    vogais = 'áaàãeéêiíoóõuúAÁÀÃEÉÊIÍOÓÕUÚ'
    traducao=''
    palavra_a_traduzir=str.lower(palavra)
    for letra in palavra_a_traduzir:
        if letra in vogais:
            traducao=traducao+letra+'p'+letra
        else:
            traducao=traducao+letra
    return traducao