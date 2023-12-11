def negyedik():
    lista = []
    befajl = open("fajlok/karivers.txt", "r", encoding="utf-8")
    tartalom = befajl.read()
    befajl.close()

    kiFajl = open("fajlok/karivers2.txt", "w", encoding="utf-8")
    kiFajl.write(tartalom)
    kiFajl.write("\n\nTiszta öröm tüze átég\na szemeken, a harangjáték\nszól, éjféli üzenet:\nKis Jézuska született!”")
    kiFajl.close()

    print("A másolás végbement")


