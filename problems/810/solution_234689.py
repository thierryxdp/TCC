def inverte(frase):
    '''Função que dada uma frase(frase) retorna uma nova frase, na ordem inversa da original, sem letras maiúsculas e sem pontuação.
    parâmetro de entrada: str
    valor de retorno: str'''
    frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'...',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    frase=str.lower(frase)
    frase=str.split(frase)
    return str.join(' ',frase[::-1])