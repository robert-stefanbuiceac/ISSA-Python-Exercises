

def dictionar(s:str)->dict:
    frecvente={}
    for c in s:
        frecvente[c]=frecvente.get(c,0)+1
    return frecvente


print(dictionar('Ana are mere'))