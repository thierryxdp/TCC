def inverte(frase):
    """Função que dada uma frase retorna uma outra frase que contenha
    as mesmas palavras da frase de entrada porém em ordem inversa, sem
    letras maiúsculas e sem pontuação.
    tipo de entrada: str
    tipo de saída; str"""
    
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, ":"," ")
    frase = str.replace(frase, "."," ")
    
    nova_frase = str.lower(frase)
    
    lista = str.split(nova_frase, ' ')
    
    nova_lista = list.reverse(lista)
    
    return str.join(' ', nova_lista)