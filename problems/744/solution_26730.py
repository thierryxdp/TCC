# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s):
    ''' iremos primerio dividir a string e adicionar a '#' nos intervalos
    o primeiro intervalo será do começo ao meio adicionando mais um '#', 
    e depois o último intervalo do meio ao final e adicionando mais um '#' '''
    meio = (len (s))//2
    return '#' + s[:meio]+'#'+s[meio:]+ '#'