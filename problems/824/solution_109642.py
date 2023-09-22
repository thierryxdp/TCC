def uppCons(phrase):
    answer = ""
    for letter in phrase:
        if letter not in "aãeiouAEIOU":
            answer = answer + letter.upper()
        else:
            answer = answer + letter
    return answer