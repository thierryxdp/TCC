def retira_pontuacao(frase):
    """Função que, dada uma frase, retona a mesma, porém sem caracteres de pontuação.
    string -> string."""
    
    lista = frase.split()
    
    for i in range(len(lista)):
        if '!' in lista[i]:
            str.replace(lista, '!', ' ')
    
    return lista