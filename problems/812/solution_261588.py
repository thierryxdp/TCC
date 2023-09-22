def retira_pontuacao(texto):
    '''funcao que recebida uma frase como entrada retorna a mesma frase com as pontuacoes substituidas por espacos
       str->str'''
    stringvazia=''
    if '?' in texto:
        stringvazia= stringvazia+ str.replace(texto,'?',' ')
    if ',' in texto:
        stringvazia= stringvazia+ str.replace(texto,',','')
    if ':' in texto:
        stringvazia= stringvazia+ str.replace(texto,':','')
    if ';' in texto:
        stringvazia= stringvazia+ str.replace(texto,';','')
    if '.' in texto:
        stringvazia= stringvazia+ str.replace(texto,'.','')
    if '-' in texto:
        stringvazia= stringvazia+ str.replace(texto,'-','')
    if '!' in texto:
        stringvazia= stringvazia+ str.replace(texto,'!','')
    else: 
        texto
    
    return stringvazia