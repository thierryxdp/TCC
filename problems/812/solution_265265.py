def retira_pontuacao(frase):
     '.' in frase
     frase = str.replace(frase,'.','')
     '-' in frase
     frase = str.replace(frase,'-','')
     ',' in frase
     frase = str.replace(frase,',','')
     ':' in frase
     frase = str.replace(frase,':','')
     ';' in frase
     frase = str.replace(frase,';','')
     return frase