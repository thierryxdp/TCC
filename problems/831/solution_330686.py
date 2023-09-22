def lingua_p(palavra):
    '''Função que recebe uma palavra em portugues e retorna a palavra traduzida na lingua do P;
    str->str'''
    traducao=''
    for letra in palavra:
        if letra in 'aeiouAEIOUáàâãéíóôõú':
            traducao=traducao+letra+'p'+letra
        else:
            traducao=traducao+letra
    return traducao