def hashtag(s):
    '''recebe uma string e retorna a mesma, só que agora com o caractere '#", 
    inserido em seu início, meio e fim;
    str-> str'''
    
    if len(s)%2 == 0:
       y = int(len(s)/2)
       return '#'+s[:y]+'#'+s[y:]+'#'
    
    else:
        x = int(len(s)//2)
        return '#'+s[:x]+'#'+s[x:]+'#'