def inverte_frase(frase : str)->str:
    """Dada uma frase retorna outra frase contendo as
    mesmas palavras da frase fornecida, mas na ordem inversa.."""
    
    frase_limpa = str.replace(str.replace(str.replace
    (str.replace(str.replace(str.replace
    (str.replace(frase,'.',' '),',',' '),';',' ')
                 ,':',' '),'-',' '),'?',' '),'!',' ')
    
    frase_invertida = list.reverse(str.split(frase_limpa))
    
    return str.join(" ",frase_invertida)