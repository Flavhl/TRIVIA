#ESTA TRIVIA ES PARA SABER QUE TAN BUEN CATOLICO ERES#
#CREANDO LAS VARIABLES DE COLOR#
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW ='\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#CICLO DEL JUEGO Y FINAL
iniciar_trivia = True
intentos = 0
while iniciar_trivia == True:
  intentos += 1
  puntaje = 0
  nombre= input(BLUE+"Bienvenido a esta trivia \n¿Cual es tu nombre? \n"+RESET)
  print(BLUE+"Hola"+RESET, nombre,BLUE +"vamos a poner a prueba que tanto sabes de religion con algunas preguntas. Estas son las reglas:\n"+RESET)
  print(GREEN+"Por cada respuesta correcta + 5","\nPor cada pregunta incorrecta / 1","\nSi escoges una alterntiva parecia + 3","\nSi escoges una alterntiva descabellada - 5"+RESET)
  print(BLUE+"\nTe deseo mucha suerte"+RESET,nombre,BLUE+"!"+RESET)
  print(YELLOW+"............................................"+RESET)
  print("Intento numero:",intentos)
  #IMPORTAR LIBRERIA#
  import random
  #TEMPORALIDAD#
  import time
  #CODIGO PARA PUNTAJES Y SUERTE ALEATORIA#
  puntaje = random.randint(0, 20)
  time.sleep(3)
  print("Comenzaras con",puntaje,"puntos")
  print(YELLOW+"............................................."+RESET)
  for numero_carga in range(5,0,-1):
    print(numero_carga)
    time.sleep(1)
  #COMENZAMOS CON LA PREGUNTA 1#
  pregunta1= print(GREEN+"1.¿Cual es la abreviatura de Antes de Cristo?\n"+RESET)
  a= print("a) a.c.")
  b= print("b) A.c.")
  c= print("c) AC.")
  d= print("d) a.C.")
  respuesta1= input("\nRespuesta:").lower()
  while respuesta1 not in ("a","b","c","d","f"):
    respuesta1=input(MAGENTA+"\nDebes responder a, b, c o d. Ingrese nuevamente tu respuesta\n"+RESET)
  if respuesta1 =="f":
    puntaje = random.randint(10, 100)
    print(YELLOW+"\nBienvenido a mi mensaje secreto"+RESET)
    print(YELLOW+"Tuviste suerte",nombre,"!"+RESET)
    time.sleep(3)
    print(YELLOW+"Te has ganado","+",puntaje,"puntos!\n"+RESET)
  elif respuesta1 == "a":
    puntaje = puntaje / 1
    print(RED+"Incorrecto"+RESET,nombre,",","mejor suerte para la proxima")
    print(YELLOW+"Acumulas",puntaje,"puntos!\n"+RESET) 
  elif respuesta1 == "b":
    puntaje = puntaje + 3
    print(RED+"Incorrecto"+RESET,nombre,",","estuviste cerca")
    print(YELLOW+"Acumulas",puntaje,"puntos!\n"+RESET) 
  elif respuesta1 == "c":
    puntaje = puntaje - 5
    print(RED+"Incorrecto"+RESET,nombre,",","es en serio!")
    print(YELLOW+"Acumulas",puntaje,"puntos!\n"+RESET) 
  else:
    puntaje = puntaje * 5
    print(CYAN+"!Correcto"+RESET,nombre,"!")
    print(YELLOW+"Estuvo facil. Tienes",puntaje,"puntos\n"+RESET)
  #COMENZAMOS CON LA PREGUNTA2#
  time.sleep(5)  
  pregunta2= print(GREEN+"2.¿Cual es el nombre del Papa Francisco?\n"+RESET)
  a= print("a) Mariano Jose Bergoglio")
  b= print("b) Mario Jonas Benedicto")
  c= print("c) Jorge Mario Bergoglio")
  d= print("d) Mario Mariano Benedicto")
  respuesta2= input("\nRespuesta:").lower()
  while respuesta2 not in ("a","b","c","d"):
    respuesta2=input(MAGENTA+"\nDebes responder a, b, c o d. Ingrese nuevamente tu respuesta\n"+RESET)
  if respuesta2 == "a":
    puntaje = puntaje + 3
    print(RED+"Incorrecto"+RESET,nombre,",","estuviste cerca")
    print(YELLOW+"Acumulas",puntaje,"puntos"+RESET)
  elif respuesta2 == "b":
    puntaje = - 5
    print(RED+"Incorrecto"+RESET,nombre,",","Benedicto fue el anterior Papa")
    print(YELLOW+"Acumulas",puntaje,"puntos"+RESET)
  elif respuesta2 == "d":
    puntaje = puntaje / 1
    print(RED+"Incorrecto"+RESET,nombre,",","El Santo Padre no esta orgulloso de ti\n")
    print(YELLOW+"Acumulas",puntaje,"puntos"+ RESET)
  else:
    puntaje = puntaje * 5
    print(CYAN+"!Correcto"+RESET,nombre,"!")
    print(YELLOW+"Acumulas",puntaje,"puntos\n"+RESET)
  #COMENZAMOS CON LA PREGUNTA3#
  time.sleep(5)  
  pregunta3= print(GREEN+"3.¿Que dia de la semana resucito Jesus?\n"+RESET)
  a= print("a) Domingo")
  b= print("b) Lunes")
  c= print("c) Jueves Santo")
  d= print("d) Miercoles")
  respuesta3= input("\nRespuesta:").lower()
  while respuesta3 not in ("a","b","c","d"):
    respuesta3=input(MAGENTA+"\nDebes responder a, b, c o d. Ingrese nuevamente tu respuesta\n"+RESET)
  if respuesta3 == "b":
    puntaje = puntaje + 3
    print(RED+"Incorrecto"+RESET,nombre,",","por eso odiamos los lunes")
    print(YELLOW+"Acumulas",puntaje,"puntos\n"+RESET)
  elif respuesta3 == "c":
    puntaje = puntaje / 1
    print(RED+"Incorrecto"+RESET,nombre,",","te confundiste con Semana Santa")
    print(YELLOW+"Acumulas",puntaje,"puntos\n"+RESET)
  elif respuesta3 == "d":
    puntaje = puntaje - 3
    print(RED+"Incorrecto"+RESET,nombre,",","eso estuvo raro")
    print(YELLOW+"Acumulas",puntaje,"puntos\n"+RESET)
  else:
    puntaje = puntaje * 5
    print(CYAN+"!Correcto"+RESET,nombre,"!")
    print(YELLOW+"Acumulas",puntaje,"puntos\n"+RESET)
  print(YELLOW+"..........................FIN......................"+RESET)
  #RULETA DE PUNTAJES#
  time.sleep(4)
  print(GREEN+"\nEsperaaaaaaa!"+RESET)
  time.sleep(3)
  print(GREEN+"\nAun no hemos terminado"+RESET,nombre,".",GREEN+"Vamos a jugar a la ruleta!\n"+RESET)
  time.sleep(2)
  for ruleta in range(3,0,-1):
    puntos = random.randint(0, 20)
    print(ruleta)
    time.sleep(2)
  print(YELLOW+"\nObtuviste:"+RESET,puntos)
  print(YELLOW+"\nLo sumaremos a tu nuevo puntaje\n"+RESET)  
  puntaje_nuevo = puntaje + puntos
  time.sleep(2)
  print(BLUE+"Gracias por participar en esta Trivia",nombre,",","en esta oportunidad tuviste",puntaje_nuevo,"puntos!"+RESET)
  time.sleep(4)
  print(YELLOW+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  time.sleep(4)
  repetir_trivia = input(BLUE+"\nIngresa si para repetir, o cualquier tecla para finalizar:"+RESET).lower()
  time.sleep(2)  
if repetir_trivia != "si":
  print(GREEN+"\nEspero",nombre,"Que lo hayas pasado bien, hasta pronto"+RESET)
  iniciar_trivia = False
      