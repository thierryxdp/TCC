def retira_pontuacao(frase):
    """Função que dada uma frase, substitui todos os caracteres de
       pontuação por espaço.     
       str -> str
       """
    x=str.replace(frase,('-'),'')
    y=str.replace(x,(','),'')
    z=str.replace(y,(':'),'')
    w=str.replace(z,(';'),'')
    r=str.replace(w,('.'),'')
    s=str.replace(r,('?'),'')
    a=str.replace(s,('!'),'')
    return a

def inverte(texto):
    """Função que dada uma frase, inverte sua ordem e retorna uma nova
       frase com as palavras invertidas.
       
       parameters: 
       texto: Frase a ser invertida
       
       Returns:
       Retorna uma nova frase com as palavras invertidas
       str -> str"""
    b=str.lower(retira_pontuacao(texto))
    c=str.split((b)
    d=c[::-]
    e=str.join('',c)
    return e