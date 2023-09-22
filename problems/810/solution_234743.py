def inverte(frase):
    '''função que recebe uma frase e retorna uma nova formada apartir
       da alteração de letras maiusculas para minusculas, além da retirada
       de vírgulas e pontuações
       [str-->str]'''
    
    if '...' in frase:
        frase = frase.replace('...',' ')
        
    if '.' in frase:
        frase = frase.replace('.',' ')
        
    if '?' in frase:
        frase = frase.replace('?',' ')
        
    if '!' in frase:
        frase = frase.replace('!',' ')

    if ':' in frase:
        frase = frase.replace(':',' ')
        
    if ';' in frase:
        frase = frase.replace(';',' ')

    if ',' in frase:
        frase = frase.replace(',',' ')

    if '-' in frase:
        frase = frase.replace('-',' ')

    if '—' in frase:
        frase = frase.replace('—',' ')

    return  str.join(' ',str.split(str.lower(frase))[-1::-1])