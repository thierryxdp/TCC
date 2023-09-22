# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frases):
    '''Função rece uma string e retorna um dicionário em
    que cada palavra é uma chave contendo o número de 
    repetições dessa palavra
    str -> dic'''
    pala = str.split(frases)
    dic = {}
    for i in pala:
        dic[i]+=1
    return dic