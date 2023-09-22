def inverte(frase):
    '''Função que dada uma frase, retorna a mesma frase
    na ordem inversa, sem letras maiúsculas, e sem a 
    pontuação.
    str -> str'''
    
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"-"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")
    frase = str.replace(frase,","," ")
    frase = str.replace(frase,":"," ")
    frase = str.replace(frase,"."," ")
    
    nova_frase = str.lower(frase)
    
    lista = str.split(nova_frase, ' ')
    
    nova_lista = lista[::-1]
    
    return str.join(" ", nova_lista)