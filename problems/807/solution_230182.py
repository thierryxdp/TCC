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
    str.partition(frase,'.')
    frase2 = str.partition(frase,'.')
    str.partition(frase2,'!')
    frase3 = str.partition(frase2,'!')
    str.partition(frase3,'?')
    frase4 = str.partition(frase3,'?')
    str.partition(frase4,'...')
    frase5 = str.partition(frase4,'...')
    str.partition(frase5,';')
    frase6 = str.partition(frase5,';')
    return len(frase6)