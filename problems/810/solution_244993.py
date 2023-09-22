def retira_pontuacao(frase):
    """Dado uma frase troca sua pontuação por espaços vazios. str -> str """
    f1 = frase.replace('-', ' ').replace('—', ' ').replace(',', ' ').replace(':', ' ').replace(';', ' ').replace('.', ' ').replace('!',' ').replace('?', ' ')
 
   
    return f1

def inverte(frase):
    """ Dada uma frase, tirar sua pontuação e a inverte. str -> str"""
    
    
    separar = retira_pontuacao(frase).lower().split()
    inverter = (separar[::-1])
                        
    return ' '.join(inverter)