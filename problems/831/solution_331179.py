def lingua_p(palavra):
    p_final = ''
    v = 'a,e,i,o,u,A,E,I,O,U,á,é,í,ó,ú'
    for x in palavra:
        if x not in v:
            p_final = p_final + x
        if x in v:
            p_final = P_final + x + 'p' + x
    return p_final