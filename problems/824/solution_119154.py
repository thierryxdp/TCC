def uppCons(s):
    """Recebe como parâmetro uma string contendo uma frase e retorna a frase com todas as suas consoantes maiúsculas;
    assinatura: str --> str
    Casos de teste:
    uppCons('abcde fghij') == 'aBCDe FGHiJ'
    uppCons('Olá, meu nome é Luciano.') == 'OLá, Meu NoMe é LuCiaNo.'
    """
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    s = s.split()
    for i, p in enumerate(s):
        for ch in p:
            if ch in cons:
                p = p.replace(ch, ch.upper())
                s[i] = p
    return ' '.join(s)