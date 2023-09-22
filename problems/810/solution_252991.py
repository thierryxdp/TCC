def retira_pontuacao(texto):
    ''' 
    Função recebe um texto e remove caracteres especiais que estão em uma lista pre-definida
    '''
    # usando replace () para remover caracteres especiais
    caracteres_interesse = "@_!'^#$%^&*()<>?/\|}{:;[]~,...-"
    #texto = limpa_acentuacao(texto)
    for i in caracteres_interesse:
        texto = texto.replace(i, ' ')
        texto = texto.lower()
    return texto

def inverte(frase):
    '''
    Funçao que dada uma frase retorne uma outra frase contendo
    as mesmas palavras da frase de entrada na ordem inversa.
    '''
    frase = retira_pontuacao(frase)
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase