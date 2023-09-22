# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def freq_palavras(frase):
    
    Lista1=[]
    i=0
    for palavra in frase:
        Lista1.append(frase.split())
        a = Lista1.count(palavra)
    return {Lista1[i]: a}