# Añadir el código necesario para crear una variable que guarde la velocidad del asteroide.
# Escribe una expresión de prueba para calcular si necesita una advertencia.
# Agregue las instrucciones que se ejecutarán si la expresión de prueba es true o false
from re import S


asteroid1 = 49
if asteroid1 > 25:
    print("Si fuera tu, gritaria porque un asteroide viene a la tierra a una velocidad de " + str(asteroid1), "km/s")  # To print two sentences without the line break is necessary a comma
else:
    print('Se feliz, porque te salvaste')


# Agrega el código para crear una variable para un asteroide que viaja a 19 km/s
# Escribe varias expresiones de prueba para determinar si puedes ver el rayo de luz desde la tierra
# Agrega las instrucciones que se ejecutarán si las expresiones de prueba son True o False

asteroid2 = 19
if asteroid2 >= 20:
    # Change the funtion on IF from just > to >=
    print("Hey quieres ver un rayo de luz? mira el cielo")
# elif asteroid2 == 20:
#    print("Hey quieres ver un rayo de luz? mira el cielo")
else:
    print("Alguien dijo asteorides?")


# Agrega el código para crear nuevas variables para la velocidad y el tamaño del asteroide
# Para probar el código, prueba con varias velocidades y tamaños
# Escribe varias expresiones de prueba o combinaciones de expresiones de prueba para determinar qué mensaje se debe enviar a Tierra.

velocityAsteroid = 25
SizeAsteroid = 40
if velocityAsteroid > 25 and SizeAsteroid > 25:
    print('Si fuera tu, gritaria porque un asteroide viene a la tierra') #Can be nesting more conditionals

elif velocityAsteroid >= 20:
    print('Hey quieres ver un rayo de luz? mira el cielo')
elif SizeAsteroid < 25:
    print('Alguien dijo asteorides?')

else:
    print('Alguien dijo asteorides?')