def contar_frase(texto):
 """
 Função que dado um texto armazenado em uma string,
 retorna o numéro de frases que aparecem no texto.
 Paramêtro de Entrada: string
 Valor de saida: int
 """
  ponto_final       = str.count(texto,".")
  ponto_exclamacao  = str.count(texto,"!")
  ponto_interrogacao= str.count(texto,"?")

  return ponto_final+ponto_exclamacao+ponto_interrogacao