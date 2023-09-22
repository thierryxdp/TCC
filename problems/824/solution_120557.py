def uppCons(frs):
    """Dada uma frase como entrada, o retorno mantém as vogais e coloca as consoantes em maiúsculo.
    assinatura:
    str -> str
    testes:
    uppCons('ola') == ('oLa')
    uppCons('Ola') == ('OLa')
    """
    vogals = ['a', 'e', 'i', 'o', 'u']
    fr = list(frs) 
    for l in range(len(fr)):
        if not fr[l] in vogals:
            fr[l] = str.upper(fr[l])
    return str.join('', fr)