def uppCons(frase):
    """Função que dada uma frase de entrada retorna a frase com
    todas as consoantes maiúsculas e os outros caracteres como
    estavam na frase original ;str->str"""
    i=0
    while i<len(frase):
        i=i+1	
        if frase[i] not in 'AEIOUaeiou! ,.?ãâÃÂ':
            str.upper(frase[i])
        else:
            return frase