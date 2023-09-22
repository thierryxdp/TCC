def inverte (x):
    '''Função que pega uma frase e retorna a frase com as mesmas 
    palavras porém com a ordem inversa, sem letra maiuscula e
    sem a pontuação.
    string->string'''
    x = str.replace (x, '-',' ')
    x = str.replace (x, ',','')
    x = str.replace (x, ':','')
    x = str.replace (x, ';','')
    x = str.replace (x, '.','')
    x = str.replace (x, '?','')
    x = str.replace (x, '!','')
    x = str.replace (x, '...','')
    x = str.split (x) [-1::-1]
    x = str.join (' ',x)
    return str.lower (x)