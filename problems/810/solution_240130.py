def inverte_frase(frase : str)->str:
    """Dada uma frase retorna outra frase contendo as
    mesmas palavras da frase fornecida, mas na ordem inversa."""

    frase_min = str.lower(frase)
    
    frase_limpa = str.replace(str.replace(str.replace
    (str.replace(str.replace(str.replace
    (str.replace(frase_min,'.',' '),',',' '),';',' ')
                 ,':',' '),'-',' '),'?',' '),'!',' ')
    
    lista = (str.split(frase_limpa))
    lista_invertida = lista[-1:(-len(lista)-1):-1]
    
    return str.join(" ",lista_invertida)