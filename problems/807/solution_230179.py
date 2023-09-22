def conta_frases(frase):
    """ função que retorna a quantidade de
    frases que aparecem no texto selecionado
    , contando a separação de palavras entre as
    pontuações : ".","...","!" e "?".
    assinatura: lista --> int
    testes: 
    conta_frases(olá!) == 1
    conta_frases(Olá!Meu nome é MP.) == 2
    conta_frases(A Aranha morreu... Mas seus filhos não!)== 2
    """
    str.strip(frase,'.')
    frase2 = str.strip(frase,'.')
    str.strip(frase2,'!')
    frase3 = str.strip(frase2,'!')
    str.strip(frase3,'?')
    frase4 = str.strip(frase3,'?')
    str.strip(frase4,'...')
    frase5 = str.strip(frase4,'...')
    return len(frase5)