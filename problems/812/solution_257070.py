def retira_pontuacao(frase):
    """Função que dada uma frase, substitui todos os caracteres de
       pontuação por espaço.
       
       Parameters:
       frase: Frase a ter sua pontuação substituida
       
       Returns:
       Retorna a frase sem a pontuação
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