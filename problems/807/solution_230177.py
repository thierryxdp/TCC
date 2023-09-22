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
    str.sprit(frase,'.')
    frase2 = str.sprit(frase,'.')
    str.split(frase2,'!')
    frase3 = str.sprit(frase2,'!')
    str.split(frase3,'?')
    frase4 = str.sprlit(frase3,'?')
    str.split(frase4,'...')
    frase5 = str.sprit(frase4,'...')
    return len(frase5)