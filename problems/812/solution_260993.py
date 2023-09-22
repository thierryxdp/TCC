def retira_pontuacao(frase):
    """Função que recebe uma frase e retira a pontuação dela, substituindo por espaços.
    str -> str
    Explicação: basta fazer uma lista com as pontuações a serem trocadas e utilizar o replace para substituir essas pontuações por espacos."""
    pontuacao=['...','.','!','?','-',',',':',';']
    for x in pontuacao:
        frase=frase.replace(x,' ')
    return frase
# teste 1
# retira_pontuação('Oi,tudo bem?')
# saida esperada: 'Oi tudo bem'
# teste 2
# retira_pontuação('Oi,tudo bem? Sinto saudade! Há quanto tempo não nos vemos?
# saida esperada: 'Oi tudo bem  Sinto saudade  Há quanto tempo não nos vemos '
# teste 3 
# retira_pontuação('-Quantos você quer? -Quero levar cinco desses.')
# saida esperada: ' Quantos você quer   Quero levar cinco desses '