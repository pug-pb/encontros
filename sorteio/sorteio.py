import random #biblioteca python para sorteios
#import webbrowser #biblioteca python para abrir navegadores
import sys

presentes = [
    "junio.webmaster@gmail.com",
]

while True:
    print('S para sorteio, P para parar')
    if sys.version_info.major == 3:
        opt = input()
    else:
        opt = raw_input()
    if opt in ['S', 's']:
        ganhador = random.sample(presentes, 1)
        presentes.remove(ganhador[0])
        print(ganhador[0])
        #webbrowser.open(ganhador[0])
    else:
        break
