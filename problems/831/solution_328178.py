def lingua_p(p):
    ''' Função que converte palavras em português p em palavras da lingua do P.'''
    d=list(p)
    f=''
    j=0
    for i in d:
        f=f+i
        if ( (i=='a') or (i=='á') or (i=='â') or (i=='e') or (i=='é') or (i=='è') or (i=='ê') or (i=='i') or (i=='í') or  (i=='ì') or (i=='o') or (i=='u') or (i=='ú')):
            f=f+'p'+i
     
    return f