def verificare(s):
    caractere=["\r","\t","\n","\a","\b","\f","\v"]
    for c in s:
        if c in caractere:
            return True
    return False

if verificare("NU am \t caractere speciale\n"):
    print("Am")
else: print("N-am")