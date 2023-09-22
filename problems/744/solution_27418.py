# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
    def hashtag():
        frase = input("insira seu texto: ")
        total = 0
        for i in frase:
            total = total + 1
        if (total % 2) == 0:
            x = (total/2)
            primeira_metade = frase[:int(x)]
            segunda_metade = frase[int(x):]
            resultado = "#" + primeira_metade + "#" + segunda metade + "#"
            return resultado
        else:   
            x = (total/2)+1
            y = (total/2)+1
            primeira_metade = frase[:int(x)]
            segunda_metade = frase[int(y):]
            resultado = "#" + primeira_metade + "#" + segunda metade + "#"
            return resultado