# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef freq_palavras(frase):
#VOCEEEEEE!!!!!!!!!!!!
def freq_palavras(frases):
    quantas_vezes={}
    separado=frases.split()
    for palavra in separado:
    	quantas_vezes.update({palavra:separado.count(palavra)})
    return quantas_vezes