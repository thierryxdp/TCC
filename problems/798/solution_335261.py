# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
 def freq_palavras(frases):
        liston = frases.split()
        dicioboy = {}
        for palavra in liston:
            chabe = liston.count(palavra)
            dicioboy[palavra] = chabe
        return dicioboy