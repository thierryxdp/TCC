def inverte(f):
    '''Dada uma frase, retorna outra frase com as mesmas palavras na ordem inversa, sem letras maiúsculas e sem pontuação.
assinatura: string --> string'''
    n=str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(f,'-',' '),':',' '),'?',' '),'!',' '),',',' '),'.',' ')
    s=str.lower(str.replace(str.replace(str.replace(n,'  ',' '),'  ',' '),'  ',' '))
    x=str.split(s,' ')
    a=str.join(' ',x[::-1])
    return a