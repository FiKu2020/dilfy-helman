def generowanie_klucz_publicznego(podst_wartosc,klucz_prywatny_osoby,modulo):
    klucz_publiczny_danej_osoby = (podst_wartosc ** klucz_prywatny_osoby) % modulo
    return klucz_publiczny_danej_osoby
def temp():
    pass

modulo = 19
podst_wartosc = 6
