def retira_pontuacao(frase):
    '''funcao que recebe uma frase e retorna essa mesma frase sem esses caracteres de pontuacao, substituindo-os por espaço
    str -> str'''
    frase=str.replace(frase,'-',' pontuacao')
    frase=str.replace(frase,',',' pontuacao')
    frase=str.replace(frase,':',' pontuacao')
    frase=str.replace(frase,';',' pontuacao')
    frase=str.replace(frase,'.',' pontuacao')
    frase=str.replace(frase,'?',' pontuacao')
    frase=str.replace(frase,'!',' pontuacao')
    return frase.strip('pontuacao')