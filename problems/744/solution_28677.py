# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    tamanho = int((len(s))/2)
    antes = s[0:tamanho]
    dps = s[tamanho:]
    return "#"+antes+"#"+dps+"#"