def build_xml_element(tag,content,**atribute)->str:
    lista_atribute = []
    for cheie,val in atribute.items():
        nume=cheie
        lista_atribute.append(f"{nume}={val}")
    string_atribute=""
    if lista_atribute:
        string_atribute=" "+ " ".join(lista_atribute)
    rezultat = f"<{tag}{string_atribute}>{content}</{tag}>"
    return rezultat

xml_element = build_xml_element(
        "a",
        "Hello there",
        href="http://python.org",
        _class="my-link",
        id="someid"
    )
print(xml_element)