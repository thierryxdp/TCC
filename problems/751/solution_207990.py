# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# string -> int
def quant_palavras(frase):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
  def retira_pontuacao(frase):
    """retira a pontuação de uma dada frase"""
    frase=frase.replace('!','')
    frase=frase.replace(',','')
    frase=frase.replace(';','')
    frase=frase.replace('.','')
    return frase