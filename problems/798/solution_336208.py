def freq_palavras(iteravel,elem):
  '''recebe uma frase e retorna um dicionario com a repetição das palavras da frase
str-> dicionário'''
    qtd=0
    for valor in iteravel:
        if valor==elem:
            qtd+=1
    return qtd