def EsPalindromo(palidromo = "arpra"):
    palidromo = palidromo.lower()
    longitud = len(palidromo)
    copy = ""
    for i in range(int(longitud)):
        copy = copy+palidromo[-i-1]

    if copy == palidromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")

EsPalindromo("MurcIcrum")