def uppCons(frase):
    """ Função que recebe uma frase com entrada e retona uma nova frase com
        as consoantes em maiúsculo. str --> str """
    fraseNova = []
    for m in frase:
        if m in " bcdfghjklmnpqrstvxwyzç":
        	fraseNova += sr.upper(m)
        else:
            fraseNova += m
    return fraseNova