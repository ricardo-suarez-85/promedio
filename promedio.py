print ("Hola me llamo Nataly , yo voy a revisar tus calificaciónes\n")
nombre = input("escribe tu nombre\n")
mate = float(input(nombre+" ¿cual es tu calificació e matematicas?\n"))
espanol = float(input(nombre+" ¿cuál es tu calificación en español?\n"))
historia = float(input(nombre+" ¿cual es tu calificación en historia?\n"))
compu = float(input(nombre+" ¿cual es tu calificación en computacion\n"))

promedio = mate+espanol+historia+compu
resultado = promedio/4

if(resultado>=6):{
    print(f"felicidades {nombre} aprobaste con {round(resultado,1)}")
}
else:{
    print(f"lo siento {nombre} reprobaste con  { round(resultado,1)}")
}
