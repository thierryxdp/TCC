def inverte(frase):
    """ Dada uma frase, tirar sua pontuação e a inverte. str -> str"""
    
    
    
    f1 = frase.lower().replace('-', '').replace('—', '').replace(',', '').replace(':', '').replace(';', '').replace('.', '').replace('!','').replace('?', '')
    separar = f1.split()
    inverter = (separar[::-1])
                        
    return ' '.join(inverter)