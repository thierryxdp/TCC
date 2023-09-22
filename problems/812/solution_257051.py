def retira_pontuacao(frase):
    """Função que dada uma frase, substitui todos os caracteres de
       pontuação por espaço.
       
       Parameters:
       frase: Frase a ter sua pontuação substituida
       
       Returns:
       Retorna a frase sem a pontuação
       str -> str"""
    pontuacao = ['-',',',':',';','...','?','!']
    if pontuacao in frase:
        return str.replace(frase, pontuaçao,'')