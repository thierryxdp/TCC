def hashtag(s):
     """Função que insere o caractere # no início, meio e no final de uma string.
    str -> str"""
     meio = len(s)//2
   return '#' + s[:meio] + '#' + s[meio:] + '#'