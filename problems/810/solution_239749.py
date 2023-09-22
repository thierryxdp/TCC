def inverte(frase):
    '''Função que dada uma frase como entrada retorne a mesma
    frase, estando em ordem inversa, sem letras maiúsculas e 
    sem pontuação.'''
    frase = str.replace(frase,".","")
    frase = str.replace(frase,"!","")
    frase = str.replace(frase,"?","")
    frase = str.replace(frase,";","")
    frase = str.replace(frase,"-","")
    frase = str.replcae(frase,":","")
    frase = str.replace(frase,",","")
    nova_frase = str.lower(frase,"")
    nova_frase = str.split(frase)
    return nova_frase