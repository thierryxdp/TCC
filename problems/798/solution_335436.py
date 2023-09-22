# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    """Função que recebe uma frase e retorna um dicionário no qual cada palavra
    da frase é uma chave cujo valor correspondente é o número de ocorrências
    dela na string introduzida
    string->dict"""
    palavras=str.split(frase)
    dici={}
    for palavra in palavras:
        n_ocorrencias=list.count(palavras,palavra)
        dici[palavra]=n_ocorrencias
    return dici