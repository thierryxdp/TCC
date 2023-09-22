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
    return len(str.split(frase,"!"or"."or"?"or"..."))