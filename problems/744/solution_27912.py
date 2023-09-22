def hashtag(s):
    '''Retorna uma string com o caractere "#" insirido no início, no meio e no final dela;
    str -> str'''
    string = "#"+str(s)+"#"
    meio = len(s)//2
    return string[:meio]+"#"+string[meio:]