def retira_pontuacao (frase):
    """Função que irá remover a pontução de uma frase
    str -> str"""
    
     pontos = ['!', '?', '#', '$', '@', '%', '&', '*', ',', '.', '-']
     
     trocar in pontos:
         
        frase = frase.replace(trocar, '')
     
    return frase