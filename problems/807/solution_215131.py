def conta_frases(texto):
    """Cálculo de uma função que tem por objetivo calcular o número de frases em um determinado texto.
    
       Parameters:
       texto: texto que será analisado e contado a quantidade de frases.
       
       Returns: 
       Retorna o número de frases do texto tendo que:
       str -> int  
    """
    tex = texto
    return str.count(tex,'.') + str.count(tex,'?') + str.count(tex,'!') - 2*str.count(tex,'...')