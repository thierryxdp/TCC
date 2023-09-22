def retira_pontuacao(frase):
    """Funcao que substitui a pontuacao da frase
    por espaços vazios.
    str -> str"""
    

    lista = frase.split('?')
    frase1 = " ".join(lista)
    
    lista2 = frase1.split('.')
    frase2 = " ".join(lista2)

    lista3 = frase2.split('!')
    frase3 = " ".join(lista3)

    lista4 = frase3.split(",")
    frase4 = " ".join(lista4)

    lista5= frase4.split(':')    
    frase5 = " ".join(lista5)

    lista6 = frase5.split(';')
    frase6 = " ".join(lista6)
    
    lista_final = frase6.split("-")
    frase_final = " ".join(lista_final)

    return frase_final