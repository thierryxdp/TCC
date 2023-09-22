def substitui_pontuação(texto):
    '''Esta função recebe um texto, retira a pontuação, substituindo
por espaços.
str --> str'''
    mod = str.replace(texto,'.',' ')
    mod = str.replace(mod,'...',' ')
    mod = str.replace(mod,'!',' ')
    mod = str.replace(mod,'?',' ')
    mod = str.replace(mod,',',' ')
    mod = str.replace(mod,'-',' ')
    mod = str.replace(mod,';',' ')
    mod = str.replace(mod,':',' ')
    return mod

def inverte(frase):
    '''Esta função recebe um texto, chama uma função para retirar a pontuação
e substituir por espaços, inverte a ordem das palavras e as põe em caixa baixa.'''
    mod = substitui_pontuação(frase)
    mod = str.split(mod)
    list.reverse(mod)
    mod = str.join(' ',mod)
    return str.lower(mod)