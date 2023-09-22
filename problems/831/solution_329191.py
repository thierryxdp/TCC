def lingua_p(palavra):
    '''funcao que, dada uma palavra, retorna a palavra traduzida para a lingua do p, ou
    seja, toda em minusculas e adicionando a letra p apos cada vogal da palavra original;
    str->str'''
    traduzida=''
    for letra in palavra:
        if letra not in 'bcdfghjklmnpqrstvwxyzç':
            traduzida=str.replace(palavra,letra,letra+'p')
    return str.lower(traduzida)