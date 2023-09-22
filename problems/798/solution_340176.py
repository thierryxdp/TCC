# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    """A função acima recebe uma string e retorna um dicionário, sendo
    cada palavra dessa string uma chave para o dicionário. A função
    tambem retorna a frequencia com que essa palavra aparece."""
    d={}
    ps = str.split(frases)
    for p in ps:
        d[p]= dict.get(d,p, 0) + 1
    return d