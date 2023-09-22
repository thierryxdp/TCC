def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra e 
    retorna essa mesma palavra traduzida para a língua
    do P.
    str->str"""
    s=""
    for i in range(len(palavra)):
        if palavra[i] not in "bcdfghjklmnpqrstvwxyzç":
            s+=palavra[i]+"p"+palavra[i]
        else:
            s+=palavra[i]
    return s