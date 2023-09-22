def retira_pontuacao(frase): 
    '''função que recebe uma frase e retorna uma outra com os caracteres
    de pontuação substituídos por espaço. 
    entrada:string 
    saída: string'''
    
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase, '.' ,' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase, ';' ,' ')
    
    return frase

def inverte(frase1):
    '''função que recebe uma frase e retorna a mesma frase, mas com as 
    palavras em ordem inversa, sem letra maiúscula e sem pontuação.
    entrada:string
    saída: string'''
    
    frase=retira_pontuacao(frase) 
    frase=str.lower(frase)
    L1=str.split(frase)
    list.reverse(L1)
    return str.join(' ',L1)