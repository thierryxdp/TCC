def conta_frases(texto):
    '''Função que conta o número de frases que aparece em um texto
    str -> str'''
    
    frases = texto.split('...')
    terminadores = ['!', '.', '?']
    
    while '' in frases:
      frases.remove('')
        
    quantidade = len(frases)
            
    return quantidade