def retira_pontuacao(frase):
    frase= frase.split('.')
    frase1= frase.split('!')
    frase2= frase1.split(',')
    frase3= frase2.split(':')
    frase4= frase3.split('')
    
    
    
   
    return ' '.join(frase4)