def retira_pontuação(frase):
   import string
   R = " "
   for c in frase:
       if c not in str.punctuation:
           R += c
    return R