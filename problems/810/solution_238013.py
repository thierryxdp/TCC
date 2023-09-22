def retira_pontuacao(frase):
    """Função que dada uma frase, substitui todos os caracteres de 
       pontuação por espaço.
       
       Parameters: 
       frase: Frase a ter sua pontuação substituída
       
       Returns:
       Retorna a frase sem a pontuação
       str -> str
       """
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(frase,"."," "),","," "),";"," "),":"," "),"_"," "),"!"," "),"?"," "),"-"," ")
def inverte(frase):
    """Função que dada uma frase, inverta a ordem das palavras e retorne
       outra frase com as palavras invertidas, sem letra maiuscula e sem
       pontuação
       
       Parameters:
       frase: Frase que terá sua ordem invertida
       
       returns:
       Retorna uma nova frase, sem letra maiuscula e pontuação e de forma
       invertida
       str -> str
       """
    b = str.lower(retira_pontuacao(frase))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return d