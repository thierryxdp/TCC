def hashtag(s):
    '''Recebe uma string e insere "#" no início, meio e fim da mesma. str -> str.'''
    return "#"+s[:int(len(s)/2)]+"#"+s[int(len(s)/2):]+"#"