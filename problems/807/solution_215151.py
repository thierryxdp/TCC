def conta_frases (texto):
    
    """Função que, dado um texto, conte o número de frases que aparecem neste texto. 
    Cada frase do texto é terminada com um ponto final, ponto de exclamação, interrogação ou reticências.
    
    Exemplo:
    
    Parâmetro: Preciso tirar um cochilo. Meu Deus! Que joras são? Vou perder minha aula...
    return: 4
    """
    
  if '.' in (texto):
        return str.count(texto,'.')
    
  if '!' in (texto):
        return str.count(texto,'!')
    
  if '?' in (texto):
        return str.count(texto,'?')
  
if '...' in (texto):
        return str.count(texto,'...')