import speech_recognition as sr
import Grabador_voz

tiempo = Grabador_voz.duracion

def fn_speech_recognition():
    audio = 'grabacion.wav'
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        info_audio = r.record(source)
        texto = r.recognize_google(info_audio, language='es-MX')
        texto = texto.lower()
        print("Lo que dijiste fue: {}".format(texto))

    archivoLector = open("textoLector.txt", "w")
    archivoLector.write(texto)
    archivoLector.close()
    print('Se genero tu archivo de salida!')

def word_counter():
    palabras = ''
    archivoLector = open('textoLector.txt', 'r')
    for i in archivoLector:
        palabras +=i
    palabras = palabras.split()
    print(f'Leiste la cantidad de {len(palabras)} palabras en {tiempo}s! ')

fn_speech_recognition()
word_counter()

