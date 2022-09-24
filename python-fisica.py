#..........importar bibliotecas e definir funçoes opcionais
import os
import time
def clear(): #..........Define a função para limpar o terminal (linux)
    os.system('clear')
def sleep(x): #.........Define a função para simplificar o sleep da biblioteca time
    time.sleep(x)
def voltar():
    input('\nvoltar ao menu [enter]--->')

#.............................subfunções:
def a_media(): #.............aceleração média
    clear()
    print("\nAceleração média\n")
    v_var = float(input("Variação da velocidade:\n--->"))
    inter_temp = float(input("Intervalo de tempo:\n--->"))
    a_media = v_var / inter_temp
    print(f'Aceleração média = {a_media}')
    voltar()

def v_funcao(): #...............Função horária da velocidade
    clear()
    print("\nFunção horária da velocidade\n")
    vo = float(input("Velocidade inicial:\n--->"))
    a = float(input("Aceleração\n--->"))
    t = float(input("Tempo\n--->"))
    v = vo + (a * t)
    print(f'Velocidade = {v}')
    voltar()
def v_funcao_vert():
    clear()
    print("\nFunção horária da velocidade no movimento vertical\n")
    vo = float(input("Velocidade inicial:\n--->"))
    t = float(input("Tempo\n--->"))
    v = vo + (9.8 * t)
    print(f'Velocidade = {v}')
    voltar()
def s_funcao_tempo_vert():
    clear()
    print("\nFunção horária da posição em função do tempo no movimento vertical")
    so = float(input("Altura inicial:\n--->"))
    vo = float(input("Velocidade inicial:\n--->"))
    t = float(input("Tempo\n--->"))
    a = 9.8
    s = so + (vo * t) + ((1/2)* a*(t**2))
    print(f'Altura = {s}')

def s_funcao_tempo():#..............Função horária da posição em função do tempo
    clear()
    print("\nFunção horária da posição em função do tempo")
    so = float(input("Posição inicial:\n--->"))
    vo = float(input("Velocidade inicial:\n--->"))
    t = float(input("Tempo\n--->"))
    a = float(input("Aceleração\n--->"))
    s = so + (vo * t) + ((1/2)* a*(t**2))
    print(f'Posição = {s}')
    voltar()

def torricelli(): #..........equação torricelli
    clear()
    print("\nTorricelli")
    vo = float(input("Velocidade inicial:\n--->"))
    a = float(input("Aceleração\n--->"))
    dist_perc = float(input("Distância percorrida:\n--->"))
    v = vo**2 + 2*a*dist_perc
    print(f'V² = {v}')
    voltar()
def torricelli_vert():
    clear()
    print("\nTorricelli no movimento vertical")
    vo = float(input("Velocidade inicial:\n--->"))
    dist_perc = float(input("Distância percorrida:\n--->"))
    a = 9.8
    v = vo**2 + 2*a*dist_perc
    print(f'V² = {v}')
#.......funções principais
def velocidade():
    clear()
    print("\nVelocidade média\n")
    dist_perc = float(input("Distância percorrida:\n--->"))
    inter_temp = float(input("Intervalo de tempo:\n--->"))
    vlcmedia = dist_perc/inter_temp #.......................fórmula velocidade média
    print(f"Velocidade média = {vlcmedia}")
    voltar()

def s_funcao():#.................função horaria do deslocamento MU
    clear()
    print("\nFunção horária do deslocamento\n")
    so = float(input("Posição inicial:\n--->"))
    v = float(input("Velocidade:\n--->"))
    inter_temp = float(input("Intervalo de tempo:\n--->"))
    s =   so + v * inter_temp#...............função horária do deslocamento
    print(f"S = {s}")
    simular = int(input("[1] para iniciar simulação\n"))
    if simular == 1:
        print("")
    else:
        voltar()

def unif_var():#....................uniformemente variado
    clear()
    print("\nMovimento uniformemente variado:\n")
    print("\n[1] Aceleração média")
    print("\n[2] Função horária da velocidade")
    print("\n[3] Função horária da posição em função do tempo")
    print("\n[4] Equação de Torricelli")
    unif_var_escolha = int(input('--->'))
    if unif_var_escolha == 1:
        sleep(1)
        a_media()
    elif unif_var_escolha == 2:
        sleep(1)
        v_funcao()
    elif unif_var_escolha == 3:
        sleep(1)
        s_funcao_tempo()
    elif unif_var_escolha == 4:
        sleep(1)
        torricelli()

def vert():
    clear()
    print("\nMovimento vertical:\n")
    print("\n[1] Função horária da velocidade no movimento vertical")
    print("\n[2] Função horária da posição em função do tempo no movimento vertical")
    print("\n[3] Equação de Torricelli no movimento vertical")
    unif_var_escolha = int(input('--->'))
    if unif_var_escolha == 1:
        sleep(1)
        v_funcao_vert()
    elif unif_var_escolha == 2:
        sleep(1)
        s_funcao_tempo_vert()
    elif unif_var_escolha == 3:
        sleep(1)
        torricelli_vert()
        
        

menuprincipal = 20
while menuprincipal != 0:
    clear()
    print("\nbem vindo")
    print("[0] Sair do script")
    print("\nCinemática: \n")
    print("\n[1] Velocidade média")
    print("\n[2] Movimento uniforme (função horária do deslocamento)")
    print("\n[3] Movimento uniformemente variado")
    print("\n[4] Movimento vertical")
    print("\n[5] Lançamento Oblíquo")
    menuprincipal = int(input('--->'))
    
    if menuprincipal == 1: #.........................velocidade media
        print(f'Você selecionou [{menuprincipal}]')
        sleep(1)
        velocidade()
    elif menuprincipal == 2: #......................função horaria do deslocamento
        print(f'Você selecionou [{menuprincipal}]')
        sleep(1)
        s_funcao()
    elif menuprincipal == 3: #........................movimento uniformemente variado
        print(f'Você selecionou [{menuprincipal}]')
        sleep(1)
        unif_var()
    elif menuprincipal == 4: #........................movimento vertical
        print(f'Você selecionou [{menuprincipal}]')
        sleep(1)
        vert()
    elif menuprincipal == 5:#.......................lançamento obliquo
        print(f'Você selecionou [{menuprincipal}]')
        sleep(1)
        #oblq()
    elif menuprincipal == 6:#.......................lançamento obliquo
        print(f'Você selecionou [{menuprincipal}]')
        simulacao()
    