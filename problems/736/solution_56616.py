def concatenacao(a, b):
    """ funçao que concatena as duas strings a e b no formato abba;
    str, str --> str;
    exemplo 1 -> 'oi' + 'ai'== 'oiaiaioi';
    exemplo 2 -> 'tudo bem' + 'tchau' == 'tudobemtchauctchautudobem' """
    return str(a) + str(b) + str(b) + str(a)