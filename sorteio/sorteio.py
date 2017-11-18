import random# biblioteca python para sorteios
import csv# biblioteca python para ler arquivos csv com lista de convidados
import sys

with open('presentes.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    presentes = []
    for row in reader:
        presentes.append(row['email'])

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
    else:
        break
