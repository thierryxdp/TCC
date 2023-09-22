def lingua_p(palavra):
    str.lower(palavra)
    palavra=str.replace(palavra,'a','pa')
    palavra=str.replace(palavra,'e','pe')
    palavra=str.replace(palavra,'i','pi')
    palavra=str.replace(palavra,'o','po')
    palavra=str.replace(palavra,'u','pu')
    return palavra