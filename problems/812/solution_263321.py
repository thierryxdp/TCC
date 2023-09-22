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