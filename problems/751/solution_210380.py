def conta_palavras(frase):
  """dado como parametro uma frase, a função retora o numero de palavras na frase
    str->int"""
  lista_palavras = frase.split(' ')
  qtd_itens = len(lista_palavras)

  if lista_palavras[0] == '':
    qtd_itens -= 1
  if lista_palavras[-1] == '':
    qtd_itens -= 1

  return qtd_itens

print(conta_palavras('testando a funcao conta palavras'))
print(conta_palavras('testando a funcao conta palavras '))
print(conta_palavras(' testando a funcao conta palavras '))