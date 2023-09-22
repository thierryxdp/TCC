def inverte(frase):
    """função que recebe uma frase e retorna outra frase com
       as mesmas palavras na ordem inversa, sem letra maiuscula
       e sem pontuação.
       str -> str"""
    
    frase_trav = frase.replace('-',' ')
    frase_virg = frase_trav.replace (',',' ')
    frase_2pont = frase_virg.replace(':',' ')
    frase_pont_virg = frase_2pont.replace(';',' ')
    frase_exclama = frase_pont_virg.replace('!',' ')
    frase_interroga = frase_exclama.replace('?',' ')
    frase_pont_final = frase_interroga.replace('.',' ')
    
    palavras = str.split(frase_pont_final)
    palavras_invertidas = palavras[::-1]
    
    return str.lower(' '.join(palavras_invertidas))