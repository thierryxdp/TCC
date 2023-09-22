def inverte(frase):
    """Recebe uma frase e retorna uma outra frase, a qual contém as mesmas palavras
       da frase original; mas na ordem inversa, sem letras maiúsculas e sem a pontuação
       parâmetros de entrada:str
       parâmetros de saída:str"""
    frase=str.replace(frase,'--',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'-',' ')
    lista=str.split(frase,'')
    invertida=lista[::-1]
    return str.lower(str.join(' ',invertida))