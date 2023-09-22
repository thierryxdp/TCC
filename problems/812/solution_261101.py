def retira_pontuacao(frase):
    
   caractere = - or , or : or ; or , or .
    
    if caractere in frase:
        return str.replace(frase, 'caractere', ' ')