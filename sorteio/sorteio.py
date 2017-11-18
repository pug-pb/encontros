import random# biblioteca python para sorteios
import csv# biblioteca python para ler arquivos csv com lista de convidados
import sys

with open('participantes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    participantes = []
    for row in reader:
        participantes.append(row['e-mail'])

while True:
    print('S para sorteio, P para parar')
    if sys.version_info.major == 3:
        opt = input()
    else:
        opt = raw_input()
    if opt in ['S', 's']:
        ganhador = random.sample(participantes, 1)
        participantes.remove(ganhador[0])
        print(ganhador[0])
    else:
        break
