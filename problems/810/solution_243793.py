def retira_pontuacao (texto):
    """Retorna uma frase onde todos os caracteres de pontuação tenham sido 
    substituídos por espaço. str -> str"""
    texto1 = str.replace(texto, ',' , ' ' )
    texto2 = str.replace(texto1, texto[-1], ' ')
    texto3 = str.replace(texto2,'-', ' ')
    texto4 = str.replace(texto3,':', ' ')
    texto5 = str.replace(texto4,';', ' ')
    
    return texto5

def inverte (texto):
    """Retorna uma frase na ordem inversa, sem letras maiúsculas e sem a pontuação.
    str->str"""
    a = str.lower(retira_pontuacao(texto))
    b = str.split(a)
    list.sort(b)
    str.join(' ',b)
    
    return a