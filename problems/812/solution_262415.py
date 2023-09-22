def retira_pont(frase):
    '''Função que troca todas as pontuações por espaço;
    str -> str'''
    
    frase = str.replace(frase,'-', )
    frase = str.replace(frase,',', )
    frase = str.replace(frase,';', )
    frase = str.replace(frase,'.', )
    frase = str.replace(frase,'!', )
    frase = str.replace(frase,'?', )
    
    return frase