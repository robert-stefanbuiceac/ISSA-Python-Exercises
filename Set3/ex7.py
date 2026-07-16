FUNCTII_GLOBALE={
    "print_all": lambda *a, **k: print(a, k),
    "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
    "print_only_args": lambda *a, **k: print(a),
    "print_only_kwargs": lambda *a, **k: print(k)
}

def apply_function(nume_functie,*args,**kwargs):
    if nume_functie in FUNCTII_GLOBALE:
        return FUNCTII_GLOBALE[nume_functie](*args,**kwargs)
    else:
        return None

apply_function("print_args_commas", 1, 2, 3, x="test", y=True)
apply_function("print_only_args", 1, 2, 3)
apply_function("print_only_kwargs", 1, 2, 3)
