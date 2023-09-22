def retira_pontuacao(frase):
    """função que retira a pontuação de uma frase, substituindo por espaços"""
    if str.find(frase,'.')!=-1 and str.find(frase,',')==-1 and str.find(frase,'!')==-1 and str.find(frase,'?')==-1:
        return str.replace(frase,('.',' '))
        
    elif str.find(frase,'.')==-1 and str.find(frase,',')==-1 and str.find(frase,'!')!=-1 and str.find(frase,'?')==-1:
        return str.replace(frase,('!',' '))
    
    elif str.find(frase,'.')!=-1 and str.find(frase,',')!=-1 and str.find(frase,'!')==-1 and str.find(frase,'?')==-1:
        a=str.replace(frase,('.',' '))
        b=str.replace(a,(',',' '))
        return b
    
    elif str.find(frase,'.')==-1 and str.find(frase,',')!=-1 and str.find(frase,'!')==-1 and str.find(frase,'?')!=-1:
        c=str.replace(frase,(',',' '))
        d=str.replace(c,;('?',' '))
        return d
    
    def inverte(frase):
        """função que dada uma frase retorna uma outra frase contendo as mesmas palavras,
        mas na ordem inversa, sem maiúsculas e sem pontuação"""
        sempontos=retira_pontuacao(frase)
        minuscula=str.lower(sempontos)
        separada=str.split(minuscula,' ')
        palavras=separada[::-1]
        final=str.join(',',palavras)
        return final