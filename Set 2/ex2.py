from Intro.main import prim

def lista_nr_prime(lista)->list:
    lista_prime=[]
    for numar in lista:
        if prim(numar):
            lista_prime.append(numar)
    return lista_prime

lista2=[20,21,22,23,31,44,51]
print(lista_nr_prime(lista2))
