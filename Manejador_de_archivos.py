
texto1 = open('Curiosidades de las Jirafas.txt', encoding="utf-8")
texto2 = open('Beneficio de la fruta.txt', encoding="utf-8")
texto3 = open('El principe Feliz.txt', encoding="utf-8")
texto4 = open('Que le pasa a la gallina.txt', encoding="utf-8")
texto5 = open('Desayuno_de_laura.txt', encoding="utf-8")
texto6 = open('Tristian queria ser Pirata.txt',  encoding="utf-8")
texto7 = open('El sol y la luna.txt', encoding="utf-8")
texto8 = open('Curiosidades del ornitorrinco.txt', encoding="utf-8")

#convierte el archivo txt a una cadena con toda la lectura
def lector_de_archivos(textoIn):
    lect = ''
    for i in textoIn:
        lect += i.lower()
    textoIn.close()
    return lect

lect1 = lector_de_archivos(texto1)
lect2 = lector_de_archivos(texto2)
lect3 = lector_de_archivos(texto3)
lect4 = lector_de_archivos(texto4)
lect5 = lector_de_archivos(texto5)
lect6 = lector_de_archivos(texto6)
lect7 = lector_de_archivos(texto7)
lect8 = lector_de_archivos(texto8)

"""def comparador_lecturas(lectura):
        p_iguales = []
        palabras_correctas = 0
        palabras = ''
        archivoLector = open('textoLector.txt', 'r')
        for i in archivoLector:
            palabras += i.lower()
        palabras = palabras.split()
        lectura = lectura.split()
        for j in palabras:
            for y in lectura:
                if y == j:
                    p_iguales.append(y)
        print(f'palabras iguales {p_iguales}')
        print(f'Leiste una cantidad de {len(p_iguales)} palabras correctas')
"""

