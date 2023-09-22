def lingua_p(palavras):
    '''Função que retorna uma palavras traduzida para a língua
    p; recebe como parâmetro uma palavra em português;String-->String'''
    palavra_minusculo=str.lower(palavras)
    traduzida=''
    for caracter in palavra_minusculo:
        if caracter in 'aeiou':
            forma= caracter+'p'+caracter
            traduzida+=forma
        else:
            traduzida+=caracter
    return traduzida