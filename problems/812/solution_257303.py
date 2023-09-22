def retira_pontuação(f):
    '''Função que tendo uma frase como entrada retorna a mesma sem os 
    caracteres de pontuação
    str -> str'''
    n= str.replace(f,'.','')
    n= str.replace(f,',','')
    n= str.replace(f,';','')
    n= str.replace(f,'!','')
    n= str.replace(f,'?','')
    n= str.replace(f,':','')
    n= str.replace(f,'-','')
    n= str.replace(f,'...','')
    return n