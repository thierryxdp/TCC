# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    """Dado como entrada a string "s", retorna a ela mesma
    com o símbolo # no início, meio e fim, por exemplo, se a entrada for mnp,
    a saída seria #m#np#, agora, se fosse por exemplo mnpq, a saída seria
    #mn#pq#; str -> str """
    s="#" + s[:len(s)//2]+"#"+ s[len(s)//2:]+"#"
    return s