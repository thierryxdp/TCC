# A função recebe uma palavra em português e retorna esta mesma palavra traduzida para a língua
# do P, quando após cada vogal da palavra original é inserida a sequência de letras 'p' mais a
# vogal original. Na resposta a palavra deverá estar com todas as letras minúsculas
# string-->string
#
def lingua_p(palavra):
    palavra_p=''
    for letra in palavra:
        if letra in 'AEIOUÁÀÃÉÍÓÔÕUÚaeiouáàãéíóôõuú':
            palavra_p=palavra_p+letra+'p'
        palavra_p=palavra_p+letra
    str.lower(palavra_p)
    return palavra_p