
def nr_cuv(s):
    separatori=[",",";","?","!","."]
    for c in separatori:
        s=s.replace(c," ")
    return len(s.split())
if __name__=='__main__':
    s="Exercitiu, ; pentru ?test nr! .cuvinte"
    print("Numarul de cuvinte din <<",s,">> este ",nr_cuv(s))