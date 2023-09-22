def conta_frases(texto):
    '''Dado um texto, a função deve retornar o número de 
    frases que aparecem no texto, e cada frase do texto
    terminan com as pontuações: '.', '!', '?' ou '...';
    str -> int'''
    frase_com_ponto=((str.count(texto,'.'))-((str.count(texto,'...'))*3))
    
    frase_com_exclamacao=(str.count(texto,'!'))
    
    frase_com_interrogacao=(str.count(texto,'?'))
    
    frase_com_reticencias=str.count(texto,'...')
    
    numero_de_frase=(frase_com_ponto+frase_com_exclamacao+frase_com_interrogacao+frase_com_reticencias)
    return (numero_de_frase)