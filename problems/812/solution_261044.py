def retira_pontuacao(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase sem esses caracteres de pontuacao, substituindo-os por espaço
    str -> str'''
    frase=str.replace(frase,'-',' # ')
    frase=str.replace(frase,',',' # ')
    frase=str.replace(frase,':',' # ')
    frase=str.replace(frase,';',' # ')
    frase=str.replace(frase,'.',' # ')
    frase=str.replace(frase,'?',' # ')
    frase=str.replace(frase,'!',' # ')
    return str.strip(frase, ' # ')