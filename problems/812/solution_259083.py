def retira_pontuacao(frase):
    frase= frase.split('.')
    frase1=' '.join(frase)
    frase2= frase1.split('!')
    frase3=' '.join(frase2)
    frase4= frase3.split('?')
    frase5= ' '.join(frase4)
    frase6= frase5.split(',')
    frase7= ' '.join(frase6)
   
    
    
    
   
    return frase7
'''a partir de uma frase, retorna a mesma sem nenhuma pontuação, str->str'''