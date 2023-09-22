def retira_pontuacao(frase):
    """funcao que, dada uma frase, retorna essa frase sem qualquer caractere de pontuaçao. Todos esses caracteres serao substituidos por espaço
    str--->str"""
    frase=str.replace('...','!')
    frase=str.replace('-','!')
    frase=str.replace(',','!')
    frase=str.replace(':','!')
    frase=str.replace('?','!')
    frase=str.replace('.','!')
    return str(frase)