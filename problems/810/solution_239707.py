def inverte(frase):
    '''Função que dada uma frase como entrada retorne a mesma
    frase, estando em ordem inversa, sem letras maiúsculas e 
    sem pontuação.'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,',',' ')
    nova_frase = str.lower(frase)
    lista = str.split(nova_frase,' ')
    nova_frase = lista[::-1]
    return str.join(' ',nova_lista)