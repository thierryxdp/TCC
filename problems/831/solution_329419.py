def lingua_p(palavra):
    '''funcao que, dada uma palavra, retorna a palavra traduzida para a lingua do p, ou
    seja, toda em minusculas e adicionando a letra p apos cada vogal da palavra original;
    str->str'''
    traduzida=''
    consoante='bcdfghjklmnpqrstvwxyzç'
    for letra in palavra:
        if str.lower(letra) not in consoante:
            nova = letra + 'p' + letra
            traduzida = traduzida + nova
        if str.lower(letra) in consoante:
            traduzida = traduzida + letra
    return traduzida