def uppCons(phrase):
    answer = ""
    for letter in phrase:
        if letter not in "aeiouAÃEIOU":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer