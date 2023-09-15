from tkinter import *
import Manejador_de_archivos

lect1 = Manejador_de_archivos.lect1
lect2 = Manejador_de_archivos.lect2
lect3 = Manejador_de_archivos.lect3
lect4 = Manejador_de_archivos.lect4
lect5 = Manejador_de_archivos.lect5
lect6 = Manejador_de_archivos.lect6
lect7 = Manejador_de_archivos.lect7
lect8 = Manejador_de_archivos.lect8


#interfaz para mostrarle el cuento al lector
#lectN es el parametro donde se reciben las lecturas, ej: lect1,lect2,etc
def interfaz_lecturas(lectN):
    lectura = Tk()
    lectura.title("\tlectura elegida")
    lectura.config(bg="antique white")
    lbl = Label(lectura, text=lectN, font=("Baskerville Old Face", 14), justify = CENTER, anchor =CENTER)
    lbl.grid(column=10, row=10)
    lectura.mainloop()

"""def menu_grabacion():
    print('1.Iniciar grabacion \n 2. Salir al menu principal\n')
    opcion = int(input('Selecciona una opcion: '))

    while True:
        match opcion:
            case 1:
                fn_speech_recognition()
                word_counter()
            case 2:
                print('Regresando al menu principal')
            case _:
                print('Error: Opcion no valida!')"""

def menu():

    while True:
        print("""
    ----------------------------------------------------------
    |                                                        |
    | S I S T E M A   D E   A P O Y O   D E   L E C T U R A  |
    |                         v.1.0                          |
    |                                                        |
    ----------------------------------------------------------
    
          LECTURAS
           1. Curiosidades de las Jirafas
           2. Beneficio de la fruta
           3. El principe feliz
           4. ¿Qué le pasa a la gallina?
           5. Desayuno de Laura
           6. Tristian queria ser pirata
           7. El sol y la luna
           8. Curiosidades del ornitorrinco
           9.  Salir
          """ )
        opcion = int(input('Selecciona la lectura que desees: '))
        match opcion:
            case 1:

                interfaz_lecturas(lect1)

            case 2:

                interfaz_lecturas(lect2)

            case 3:

                interfaz_lecturas(lect3)

            case 4:

                interfaz_lecturas(lect4)

            case 5:

                interfaz_lecturas(lect5)

            case 6:

                interfaz_lecturas(lect6)

            case 7:

                interfaz_lecturas(lect7)

            case 8 :

                interfaz_lecturas(lect8)
            case 9:
                print('Saliendo...')
                break
            case _:
                print('Error: Opcion no valida!')

if __name__ == "__main__":
    menu()
