def conta_frases (texto):
    
    """Função que, dado um texto, conte o número de frases que aparecem neste texto. 
    Cada frase do texto é terminada com um ponto final, ponto de exclamação, interrogação ou reticências.
    
    Exemplo:
    
    Parâmetro: Preciso tirar um cochilo. Meu Deus! Que joras são? Vou perder minha aula...
    return: 4
    """
    
    ret=str.count(texto,'...')
    exc=str.count(texto,'!')
    inter=str.count(texto,'?')
    pf=str.count(texto,'.')-3*ret
    
    return ret+exc+inter+pf