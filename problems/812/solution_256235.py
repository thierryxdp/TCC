def retira_pontuação(frase):
   R = " "
   for c in frase:
       if c not in str.punctuation:
           R += c
    return R