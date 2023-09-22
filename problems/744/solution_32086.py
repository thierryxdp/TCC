def hashtag(s):
    "Função que recebe uma string e insere uma hashtag no início, no meio e no final da palavra."""
    str; str
    s  =  "#"  +  s [: len ( s ) // 2 ] +  "#"  +  s [ len ( s ) // 2 :] +  "#"
    return  s