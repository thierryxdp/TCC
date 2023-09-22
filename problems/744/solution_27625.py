"Recebe uma string e retorna com o simbolo # no inicio,meio e fim da string"
"string"
" str-> str"
def hashtag(str):
    return"#" + str[:int(len(str)/2)] + "#" + str[int(len(str)/2):] + "#"