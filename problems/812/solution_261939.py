def retira_pontuacao(frase):
    '''função que recebe uma frase e retorna uma frase onde todos os caracteres de pontuação foram substituídos por espaço.
    entrada: string 
    saída: string'''
    
    if ('!' in frase):
        s=str.replace(frase,'!',' ')
    if ('.' in frase): 
        s= s + str.replace(frase,'.',' ')
    if (',' in frase):
        s= s + str.replace(frase, ',', ' ')   
    if ('?' in frase): 
        s=s + str.replace(frase,'?',' ')
    if ('...' in frase): 
        s=s + str.replace(frase,'...',' ')
    if ('-' in frase): 
        s= s+str.replace(frase,'-',' ')
    if (';' in frase): 
        s= s+str.replace(frase,';',' ')
    if (':' in frase):
        s= s+str.replace(frase,':',' ')
        return s