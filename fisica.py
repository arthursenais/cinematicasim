from vpython import *
so = float(input("Posição inicial: "))
vo = float(input("Velocidade: "))
tempo = float(input("Intervalo de tempo: "))

obj = sphere(pos=vector(so,0,0),velocity=vector(vo,0,0))
chao = box(pos=vector(0,-10,0),color=color.green,size=vector(1,5,0.5))

dt=0.01
t=0

while t < tempo:
    rate(100)
    obj.pos.x = obj.pos.x + obj.velocity.x * dt
    t=t+dt
sleep(1)
print(f'S = {obj.pos.x} ')
    