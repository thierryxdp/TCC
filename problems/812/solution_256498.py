def retira_pontuacao(f): 
    '''Função que substitui os caracteres de pontuação ('.','-',',',':',';','!','?','...')
    por espaços. Entrada: str. Saída: str.'''
    f=str.replace(f,'...','')
    f=str.replace(f,'?','')
    f=str.replace(f,'.','')
    f=str.replace(f,'-',' ')
    f=str.replace(f,',','')
    f=str.replace(f,';','')
    f=str.replace(f,':','')
    f=str.replace(f,'!','')
    return f