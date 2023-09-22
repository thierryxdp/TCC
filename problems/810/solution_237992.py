def inverte(frase):
    """Recebe uma frase e retorna outra frase, a qual contém as mesmas
       palavras da frase original na ordem inversa, sem letras maiúsculas e sem a pontuação
       parâmetro de entrada:str
       parâmetro de saída:str"""
    frase=str.replace(frase,'--','')
    frase=str.replace(frase,',','')
    frase=str.replace(frase,':','')
    frase=str.replace(frase,';','')
    frase=str.replace(frase,'?','')
    frase=str.replace(frase,'!','')
    frase=str.replace(frase,'.','')
    lista=str.split(frase," ")
    invertida=lista[::-1]
    return str.lower(str.join(' ',invertida))