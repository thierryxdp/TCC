# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """a partir da string, a função corta ela no meio e retorna o valor dela adcionando "#" no inicio, no fim e no meio"""
    tamanho = int((len(s))/2)
    antes = s[0:tamanho]
    dps = s[tamanho:]
    return "#"+antes+"#"+dps+"#"