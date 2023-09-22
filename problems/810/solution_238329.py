#-------EXERCICIO 5-----------

def inverte(texto):
    '''Inverte a ordem das palavras e retira os pontos
       str -> str'''

    txtSemPonto = eliminapontos(texto)
    listaPalavras = str.split(txtSemPonto)
    
    return ' '.join(reversed(listaPalavras))