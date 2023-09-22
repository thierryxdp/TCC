def hashtag (s):
        '''que receba uma string e insira o caractere ”#” no in ́ıcio, no meio
e no final dela
:str, str -> str '''
        return '#' + str (s[0:(len(s)//2)]) + '#' + s[(len(s)//2):] + '#'