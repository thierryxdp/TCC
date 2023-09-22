def retira_pontuacao(frase):
    """funcao que, dada uma frase, retorna essa frase sem qualquer caractere de pontuaçao. Todos esses caracteres serao substituidos por espaço
    str--->str"""
    frase=str.replace(frase,'...','!')
    frase=str.replace(frase,'-','!')
    frase=str.replace(frase,',','!')
    frase=str.replace(frase,':','!')
    frase=str.replace(frase,'?','!')
    frase=str.replace(frase,'.','!')
    frase=str.split(frase,'!')
    del frase[-1]
    frase= str(frase[:])
    return frase