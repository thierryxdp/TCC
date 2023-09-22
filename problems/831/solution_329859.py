def lingua_p(palavra):
    """funcao que recebe de entrada uma palavra (em portugues)
    e retorna esta mesma palavra traduzida para a lingua do P;
    str -> str"""
    
    l_palavra = str.lower(palavra)
    l_palavra = str.replace(l_palavra, a,apa)
    l_palavra = str.replace(l_palavra, e,epe)
    l_palavra = str.replace(l_palavra, i,ipi)
    l_palavra = str.replace(l_palavra, o,opo)
    l_palavra = str.replace(l_palavra, u,upu)
    return l_palavra