# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str

def hashtag(s):
    '''insere '#' no início, meio e fim da string 's' '''
    
    string= 's';
    metade= math.floor(string.length/2);
    resultado= '#' + (string.substr(0,metade)+'#'+string.substr(metade) + "#';
    return  resultado