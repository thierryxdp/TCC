def conta_frases(txt):
    ''' Função que dado uma texto, retorna quantas 
    frases tem naquele trecho de texto
    ass: str --> int
    testes:'''    
    a =str.count(txt, '...')
    b =str.count(txt, '!')
    c =str.count(txt, '.')-(a*3)
    d =str.count(txt, '?')     
    return (a+b+c+d)