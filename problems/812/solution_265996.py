def retira_pontuacao(frase):
    """Essa Função dada uma frase, ela retorna a frase sem caracteres de pontuacao;
    Recebe uma fras;
    Retorna a frase sem caracteres de pontuacao.
    string -> string"""
    f = str.split(frase,'-')
    frase = str.join(f,' ')
    f = str.split(frase,',')
    frase = str.join(f,' ')
    f = str.split(frase,':')
    frase = str.join(f,' ')
    f = str.split(frase,'.')
    frase = str.join(f,' ')
    f = str.split(frase,';')
    frase = str.join(f,' ')
    return f