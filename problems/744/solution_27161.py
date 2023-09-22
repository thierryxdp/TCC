# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
# str-> str
def hashtag(s)
    x=len(s)//2#corta a quantidade de caracteres da string no meio
#retorna no inicio uma hashtag e segue a string até um caractere antes do meio
#depois adciona uma hashtag no meio da string e
#segue a string do meio até o final dela e adciona outra hashtag no final
    return  '#'+(s[0:x])+'#'+(s[x:len(s)])+'#'