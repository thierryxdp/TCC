def retira_pontuacao (texto):
    ''' função que ao receber um texto altera todos os elementos de pontuação,
       (...—!:;,?.), os substituindo por espaços vazios
       [str-->str]'''
    
    if '...' in texto:
        texto = texto.replace('...',' ')
        
    if '.' in texto:
        texto = texto.replace('.',' ')
        
    if '?' in texto:
        texto = texto.replace('?',' ')
        
    if '!' in texto:
        texto = texto.replace('!',' ')

    if ':' in texto:
        texto = texto.replace(':',' ')
        
    if ';' in texto:
        texto = texto.replace(';',' ')

    if ',' in texto:
        texto = texto.replace(',',' ')

    if '—' in texto:
        texto = texto.replace('—',' ') 
      
    if '-' in texto:
        texto = texto.replace('-',' ')
        
    return texto