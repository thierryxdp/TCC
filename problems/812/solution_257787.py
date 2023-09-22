def retira_pontuacao(frase):
    '''função que dada uma frase no formato string retira todos os caracteres de pontuação e 
    retorna a frase com espaços no lugar dos caracteres
    str->str'''
    if ('.!?-,:;-')in frase:
    frasenova=str.replace(frase,'')
    return frasenova