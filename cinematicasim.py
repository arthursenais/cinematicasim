#..........importar bibliotecas e definir funçoes opcionais
from termcolor import colored
print_red = lambda x: print(colored(x,'red'))
print_blue = lambda x: print(colored(x,'blue'))
print_yellow = lambda x: print(colored(x,'yellow'))
print_green = lambda x: print(colored(x,'green'))
input_teste = lambda x: input(colored(x,attrs=["bold"]))
import os
import time
from vpython import *
def clear(): #..........Define a função para limpar o terminal (linux)
    os.system('clear')
def sleep(x): #.........Define a função para simplificar o sleep da biblioteca time
    time.sleep(x)
def voltar():
    input_teste('\nvoltar ao menu [enter]--->')

#..........................................................subfunções:....................................
#aceleração média:
def a_media(): 
    clear()
    print("\nAceleração média\n")
    v_var = float(input_teste("Variação da velocidade:\n--->"))
    inter_temp = float(input_teste("Intervalo de tempo:\n--->"))
    a_media = v_var / inter_temp
    print(f'Aceleração média = {a_media}')
    voltar()
#Função horária da velocidade:
def v_funcao(): 
    clear()
    print("\nFunção horária da velocidade\n")
    vo = float(input_teste("Velocidade inicial:\n--->"))
    a = float(input_teste("Aceleração\n--->"))
    inter_temp = float(input_teste("Tempo\n--->"))
    v = vo + (a * inter_temp)
    print(f'V = {v}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_vfuncao(vo,a,inter_temp)
    else:
        return
    voltar()
#Função horária da posição em função do tempo
def s_funcao_tempo():
    clear()
    print("\nFunção horária da posição em função do tempo")
    so = float(input_teste("Posição inicial:\n--->"))
    vo = float(input_teste("Velocidade inicial:\n--->"))
    inter_temp = float(input_teste("Tempo\n--->"))
    a = float(input_teste("Aceleração\n--->"))
    s = so + (vo * inter_temp) + ((1/2)* a*(inter_temp**2))
    print(f'Posição = {s}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_sfuncaotempo(so,vo,inter_temp,a)
    else:
        return
    voltar()
#Função horária da posição em função da posição
def a_funcao_s():
    clear()
    print("\nFunção horária da aceleração em função da posição")
    s = float(input_teste("Posição final:\n--->"))
    so = float(input_teste("Posição inicial:\n-->"))
    vo = float(input_teste("Velocidade inicial:\n--->"))
    inter_temp = float(input_teste("Tempo\n--->"))
    a = (so + (vo * inter_temp) + ((1/2) * (inter_temp**2))) / s
    print(f'Aceleração= {a}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_afuncaoposicao(so,vo,inter_temp,s)
    else:
        return
    voltar()
#equação torricelli:
def torricelli_v():
    clear()
    print("\nTorricelli (v=vo² + 2as)")
    vo = float(input_teste("Velocidade inicial:\n--->"))
    a = float(input_teste("Aceleração\n--->"))
    dist_perc = float(input_teste("Distância percorrida:\n--->"))
    v = pow((vo**2) + 2*a*dist_perc,1/2)
    print(f'V² = {v}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_torricelliv(vo, a, dist_perc)
    else:
        return
    voltar()
#Torricelli para descobrir aceleração
def torricelli_a():
    clear()
    print("\nTorricelli ( a = (vo² + v²)  / (2s) )")
    vo = float(input_teste("Velocidade inicial:\n--->"))
    v = float(input_teste("Velocidade final\n--->"))
    dist_perc = float(input_teste("Distância percorrida:\n--->"))
    a = ((vo**2) + (v**2))  / (2 * dist_perc)
    print(f'V² = {a}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_torricellia(vo, v, dist_perc)
    else:
        return
    voltar()
#2ª lei de newton:
def newtonforca():
    clear()
    print("\n2ª Lei de Newton (força escalar resultante)\n")
    m = float(input_teste("Massa:\n--->"))
    a = float(input_teste("Aceleração escalar\n--->"))
    f = m*a
    print(f'F = {f}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacaonewton(m,a,f)
    else:
        return
    voltar()
def newtonaceleracao():
    clear()
    print("\n2ª Lei de Newton (Aceleração escalar)\n")
    m = float(input_teste("Massa:\n--->"))
    f = float(input_teste("Força\n--->"))
    a = f/m
    print(f'A = {a}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacaonewton(m,a,f)
    else:
        return
    voltar()
def newtonmassa():
    clear()
    print("\n2ª Lei de Newton (Massa)\n")
    a = float(input_teste("Aceleração escalar:\n--->"))
    f = float(input_teste("Força\n--->"))
    m = f/a
    print(f'm = {m}')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacaonewton(m,a,f)
    else:
        return
    voltar()
#Aceleração adquirida pelo sistema de dois blocos A e B:
def aceleracao_ab():
    clear()
    print("\nAceleração adquirida pelo sistema de dois blocos A e B\n")
    m_a = float(input_teste("Massa do bloco A:\n--->"))
    m_b = float(input_teste("Massa do bloco B:\n--->"))
    f_a = float(input_teste("Intensidade da força sobre o bloco A\n--->"))
    a = f_a / (m_a + m_b)
    print(f'a = {a}m/s²')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_ab(m_b,m_a,f_a,a)
    else:
        return
    voltar()
def forca_ab():
    clear()
    print("\nForça que o bloco A exerce sobre o bloco B\n")
    m_b = float(input_teste("Massa do bloco B:\n--->"))
    a = float(input_teste("Aceleração:\n--->"))
    f_ab = m_b * a
    print(f'Fab = {f_ab}N')
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_ab(m_b,a,f_ab)
    else:
        return
    voltar()
    
#.............................................funções principais:.........................................
#Velocidade média:
def velocidade():
    clear()
    print("\nVelocidade média\n")
    dist_perc = float(input_teste("Distância percorrida:\n--->"))
    inter_temp = float(input_teste("Intervalo de tempo:\n--->"))
    vlcmedia = dist_perc/inter_temp #.......................fórmula velocidade média
    print(f"Velocidade média = {vlcmedia}")
    voltar()
#Movimento uniformemente variado:
def unif_var():
    clear()
    print("\nMovimento uniformemente variado:\n")
    print("\n[1] Aceleração média")
    print("\n[2] Função horária da velocidade")
    print("\n[3] Função horária da aceleração em função da posiçao")
    print("\n[4] Função horária da posição em função do tempo")
    print("\n[5] Equação de Torricelli (descobrir velocidade)")
    print("\n[6] Equação de Torricelli (descobrir aceleração)")
    var_escolha = int(input_teste('--->'))
    if var_escolha == 1:
        sleep(0.5)
        a_media()
    elif var_escolha == 2:
        sleep(0.5)
        v_funcao()
    elif var_escolha == 3:
        sleep(0.5)
        a_funcao_s()
    elif var_escolha == 4:
        sleep(0.5)
        s_funcao_tempo()
    elif var_escolha == 5:
        sleep(0.5)
        torricelli_v()
    elif var_escolha == 6:
        sleep(0.5)
        torricelli_a()

    clear()
#função horaria do deslocamento:
def s_funcao():
    clear()
    print("\nFunção horária do deslocamento\n")
    so = float(input_teste("Posição inicial:\n--->"))
    v = float(input_teste("Velocidade:\n--->"))
    inter_temp = float(input_teste("Intervalo de tempo:\n--->"))
    s =   so + v * inter_temp#...............função horária do deslocamento
    print(f"S = {s}")
    simular = input_teste("[1] para iniciar simulação\n[Enter] para voltar\n--->")
    if simular == '1':
        simulacao_mru(so,v,inter_temp)
    else:
        return
    voltar()
#Leis de newton:
def leisnewton():
    clear()
    print("\nLeis de newton\n")
    print("\n[1] 2ª Lei de newton (força)")
    print("\n[2] 2ª Lei de newton (massa)")
    print("\n[3] 2ª Lei de newton (aceleração)")
    print("\n[4] 3ª Lei de newton (Aceleração adquirida pelo sistema de dois blocos A e B)")
    print("\n[5] 3ª Lei de newton (Intensidade da força que o bloco A exerce no bloco B)")
    newton_escolha = int(input_teste('--->'))
    if newton_escolha == 1:
        sleep(0.5)
        newtonforca()
    elif newton_escolha == 2:
        sleep(0.5)
        newtonmassa()
    elif newton_escolha == 3:
        sleep(0.5)
        newtonaceleracao()
    elif newton_escolha == 4:
        sleep(0.5)
        aceleracao_ab()
    elif newton_escolha == 5:
        sleep(0.5)
        forca_ab()
    clear()
#peso de um corpo:
def pesocorpo():
    clear()
    print("\nPeso de um corpo\n")
    m = float(input_teste("Massa:\n--->"))
    g = float(input_teste("Gravidade (padrão = 9.8m/s):\n--->"))
    p = m*g
    print(f'P = {p}N')
    voltar()
#lista de todoas as formulas etc:
def todos():
    clear()
    print("\nTodas as equações e fórmulas utilizadas no script:\n")
    print_yellow("[1] Velocidade média: Vm = d/t")
    print_yellow("[2] Aceleração média: Am = v/t")
    print_yellow("[3] Função horária do deslocamento: S = So + v * t")
    print_yellow("[4] Função horária da velocidade: V = Vo + (a*t)")
    print_yellow("[5] Função horária da aceleração em função da posiçao: A = (So + (Vo * t) + ((1/2) * (t^2))) / S")
    print_yellow("[6] Função horária da posição em função do tempo: S = So + (Vo * t) + ((1/2)* a*(t^2))")
    print_yellow("[7] Equação de Torricelli (descobrir velocidade): V = raiz((Vo^2) + 2*a*d)")
    print_yellow("[8] Equação de Torricelli (descobrir aceleração): a = ((Vo^2) + (V^2))  / (2 * d)\n")
    print_green("[9] Peso de um corpo: P = m*g")
    print_green("[10] 2ª Lei de newton (força): F = m*A")
    print_green("[11] 2ª Lei de newton (massa): m = F/A")
    print_green("[12] 2ª Lei de newton (aceleração): A = F/m")
    print_green("[13] 3ª Lei de newton (aceleração adquirida por dois blocos A B): A = Fa / (Ma + Mb)")
    print_green("[14] 3ª Lei de newton (Força que o bloco A exerce sobre bloco B): Fab = Mb * A")
    print("[15] ...")
    todos_escolha = int(input_teste('--->'))
    if todos_escolha == 1:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        vlcmedia()
    elif todos_escolha == 2:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        a_media()
    elif todos_escolha == 3:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        s_funcao()
    elif todos_escolha == 4:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        v_funcao()
    elif todos_escolha == 5:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        a_funcao_s()
    elif todos_escolha == 6:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        s_funcao_tempo()
    elif todos_escolha == 7:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        torricelli_v()
    elif todos_escolha == 8:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        torricelli_a()
    elif todos_escolha == 9:
        print_blue(f'Você selecionou [{pesocorpo}]')
        sleep(0.5)
        pesocorpo()
    elif todos_escolha == 10:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        newtonforca()
    elif todos_escolha == 11:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        newtonmassa()
    elif todos_escolha == 12:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        newtonaceleracao()
    elif todos_escolha == 13:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        aceleracao_ab()
    elif todos_escolha == 14:
        print_blue(f'Você selecionou [{todos_escolha}]')
        sleep(0.5)
        forca_ab()
    clear()
#......................................simulações movimento retilineo:...............................
def simulacao_mru(so,v,inter_temp):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Movimento Retilineo Uniforme</b>")
    scene.append_to_caption(f'\tInformações:\n\tVelocidade: {v}\n\tPosição inicial: {so}\n\tIntervalo de tempo: {inter_temp}')
    scene.align = 'left'
    
    obj = sphere(pos=vector(so,0,0),velocidade=vector(v,0,0),color=color.red,make_trail=True,trail_color=color.white)
    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    
    #trail = curve(color=color.white)
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.6)
    dt=0.01
    t=0
    textotempo = label(text=f'{t}',color=color.white,opacity=1,background=color.black,box=False)
    while t <= inter_temp:
        rate(100)
        #objeto:
        obj.pos.x = obj.pos.x + obj.velocidade.x * dt
        #labels:
        texto.pos.x = obj.pos.x #label informando posição
        texto.text = f'S = {obj.pos.x}' #texto da label
        textovelocidade.text = f'V = {obj.velocidade.x}'
        textovelocidade.pos = obj.pos
        textovelocidade.pos.x = obj.pos.x + 2 
        textovelocidade.pos.y = obj.pos.y + 1

        textotempo.text = f'{t:.0f}s'
        #flecha:
        flecha.pos=obj.pos #Flecha do objeto
        flecha.pos.x=obj.pos.x + 0.7
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #cenario camera:
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'S = {obj.pos.x} ')

def simulacao_vfuncao(vo,a,inter_temp):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Função horária da velocidade</b>")
    scene.append_to_caption(f'\tInformações:\n\tVelocidade inicial: {vo}\n\tAceleração: {a}\n\tTempo: {inter_temp}')
    scene.align = 'left'
    
    obj = sphere(pos=vector(0,0,0),velocidade=vector(vo,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while t < inter_temp:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * dt)
        obj.pos = obj.pos + (obj.velocidade * dt) #movimento do objeto
        #labels:

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'V = {obj.velocidade.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.x = obj.pos.x + 0.7
        flecha.pos.y=obj.pos.y-0.5
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.x = obj.pos.x + 0.7
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'v = {obj.velocidade.x} ')

def simulacao_sfuncaotempo(so,vo,inter_temp,a):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Função horária da posição em função do tempo</b>")
    scene.append_to_caption(f'\tInformações:\n\tPosição inicial: {so}\n\tVelocidade inicial: {vo}\n\tAceleração: {a}\n\tTempo: {inter_temp}\n\t')
    scene.align = 'left'
    
    obj = sphere(pos=vector(so,0,0),velocidade=vector(vo,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while t < inter_temp:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * dt)
        obj.pos = obj.pos + (obj.velocidade * dt) #movimento do objeto
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'S = {obj.pos.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'V = {obj.velocidade.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.x = obj.pos.x + 0.7
        flecha.pos.y=obj.pos.y-0.5
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.x = obj.pos.x + 0.7
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'v = {obj.velocidade.x} ')

def simulacao_afuncaoposicao(so,vo,inter_temp,s):
    a = (so + (vo * inter_temp) + ((1/2) * (inter_temp**2))) / s
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Função horária da posição em função da posição</b>")
    scene.append_to_caption(f'\tInformações:\n\tPosição inicial: {so}\n\tVelocidade inicial: {vo}\n\tPosição final: {s}\n\tTempo: {inter_temp}\n\t')
    scene.align = 'left'
    
    obj = sphere(pos=vector(so,0,0),velocidade=vector(vo,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while obj.pos.x <= s:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * dt)
        obj.pos = obj.pos + (obj.velocidade * dt) #movimento do objeto
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'S = {obj.pos.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'V = {obj.velocidade.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.x = obj.pos.x + 0.7
        flecha.pos.y=obj.pos.y-0.5
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.x = obj.pos.x + 0.7
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'a = {obj.aceleracao.x} ')

def simulacao_torricelliv(vo,a,dist_perc):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Torricelli</b>")
    scene.append_to_caption(f'\tInformações:\n\tVelocidade inicial: {vo}\n\tAceleração: {a}\n\tDistância: {dist_perc}\n\t')
    scene.align = 'left'
    
    obj = sphere(pos=vector(0,0,0),velocidade=vector(vo,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while obj.pos.x <= dist_perc:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * dt)
        obj.pos = obj.pos + (obj.velocidade * dt) #movimento do objeto
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'S = {obj.pos.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'V = {obj.velocidade.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.x = obj.pos.x + 0.7
        flecha.pos.y=obj.pos.y-0.5
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.x = obj.pos.x + 0.7
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'v = {obj.velocidade.x} ')

def simulacao_torricellia(vo,v,dist_perc):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>Torricelli</b>")
    scene.append_to_caption(f'\tInformações:\n\tVelocidade inicial: {vo}\n\tVelocidade final: {v}\n\tDistância: {dist_perc}\n\t')
    scene.align = 'left'
    a = ((vo**2) + (v**2))  / (2 * dist_perc)
    obj = sphere(pos=vector(0,0,0),velocidade=vector(vo,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while obj.velocidade.x < v:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * dt)
        obj.pos = obj.pos + (obj.velocidade * dt) #movimento do objeto
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'S = {obj.pos.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'V = {obj.velocidade.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.x = obj.pos.x + 0.7
        flecha.pos.y=obj.pos.y-0.5
        flecha.axis=obj.velocidade*0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.x = obj.pos.x + 0.7
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
        
    sleep(0.5)
    print(f'v = {obj.velocidade.x} ')

def simulacaonewton(m,a,f):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>2ª Lei de Newton</b>")
    scene.append_to_caption(f'\tInformações:\n\tMassa: {m}\n\tAceleração: {a}\n')
    scene.align = 'left'
    obj = box(pos=vector(0,0,0),velocidade=vector(0,0,0),massa=vector(m,0,0),forca=vector(0,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    
    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while obj.forca.x <= f:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * t)
        obj.forca.x = obj.massa.x * (obj.aceleracao.x * t)
        obj.pos = obj.pos + (obj.forca * dt) #movimento do objeto
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'M = {obj.massa.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'F = {obj.forca.x}' 
        #flecha:
        flecha.pos=obj.pos
        flecha.pos.y=obj.pos.y-0.5
        flecha.pos.x=obj.pos.x+0.5
        flecha.axis=obj.forca * 0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.pos.x=obj.pos.x + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt

def simulacao_ab(m_b,m_a,f_a,a):
    #cena:
    scene.background = color.hsv_to_rgb(vector(0.1,0.1,0.2))
    scene.autoscale = False
    scene.width = 1080
    scene.height = 600
    scene.append_to_title("<b>2ª Lei de Newton</b>")
    scene.append_to_caption(f'\tInformações:\n\tBloco A:\n\tMassa: {m_a}\n\tAceleração: {m_a}\n\tForça aplicada: {f_a}\n\tBloco B:\n\tMassa: {m_b}')
    scene.align = 'left'
    obj = box(size=vector(m_a,m_a,m_a),pos=vector(0,0,0),velocidade=vector(0,0,0),massa=vector(m_a,0,0),forca=vector(0,0,0),aceleracao=vector(a,0,0),color=color.red,make_trail=True,trail_color=color.white)
    objb = box(pos=vector(obj.size.x,0,0),velocidade=vector(0,0,0),massa=vector(m_b,0,0),forca=vector(0,0,0),aceleracao=vector(a,0,0),color=color.blue)

    flecha = arrow(pos=obj.pos,axis=obj.velocidade,color=color.blue,round=True,shaftwidth=0.2)
    flechaaceleracao = arrow(pos=obj.pos,axis=obj.aceleracao,color=color.yellow,round=True,shaftwidth=0.2)

    texto = label(pos=vector(obj.pos.x,obj.pos.y - 3,0),text=f'S = {obj.pos.x}',color=color.white,opacity=0,box=False)
    textob = label(pos=vector(objb.pos.x,objb.pos.y - 3,0),text=f'S = {objb.pos.x}',color=color.white,opacity=0,box=False)
    textoaceleracao = label(pos=flechaaceleracao.pos,text=f'a = {a}²',color=color.white,opacity=0,box=False)
    textovelocidade = label(text=f'V ={obj.velocidade.x}',color=color.white,opacity=0,box=False)
    dt=0.01
    t=0
    
    while obj.forca.x <= f_a:
        rate(100)
        obj.velocidade = obj.velocidade + (obj.aceleracao * t)
        obj.forca.x = obj.massa.x * (obj.aceleracao.x * t)
        obj.pos = obj.pos + (obj.forca * dt) #movimento do objeto

        obj

        if obj.pos.x >= objb.pos.x:
            obj.forca.x = obj.forca.x - objb.massa.x
        #labels:
        texto.pos.x = obj.pos.x # posição da label informando
        texto.text = f'M = {obj.massa.x}' #texto da label

        textoaceleracao.pos.x = flechaaceleracao.pos.x + 5
        textoaceleracao.pos.y = flechaaceleracao.pos.y + 1
        textoaceleracao.text = f'a = {obj.aceleracao.x}²'

        textovelocidade.pos = textoaceleracao.pos
        textovelocidade.pos.y = textoaceleracao.pos.y - 3
        textovelocidade.text = f'F = {obj.forca.x}' 
        #flecha:
        flecha.pos=objb.pos
        flecha.pos.y=objb.pos.y-0.5
        flecha.pos.x=objb.pos.x+0.5
        flecha.axis=objb.forca * 0.5 #Para onde a flecha aponta
        #flecha da aceleração:
        flechaaceleracao.pos=obj.pos
        flechaaceleracao.pos.y=obj.pos.y + 0.5
        flechaaceleracao.pos.x=obj.pos.x + 0.5
        flechaaceleracao.axis=obj.aceleracao*0.5
        scene.camera.follow(obj) #cenario
        t=t+dt
menuprincipal = 20
while menuprincipal != 0:
    clear()
    print(colored("\nbem vindo",attrs=["underline"]))
    print_red("[0] Sair do script")
    print_red("[9] Listar todas as fórmulas utilizadas")
    print_yellow("\nCinemática: \n")
    print_yellow("\n[1] Velocidade média")
    print_yellow("\n[2] Movimento uniforme (função horária do deslocamento)")
    print_yellow("\n[3] Movimento uniformemente variado")
    print_green("\nDinâmica:")
    print_green("\n[4] Peso de um corpo")
    print_green("\n[5] 2ª e 3ª lei de newton")
    menuprincipal = int(input_teste('--->'))
    
    if menuprincipal == 1: #.........................velocidade media
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        velocidade()
    elif menuprincipal == 2: #......................função horaria do deslocamento
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        s_funcao()
    elif menuprincipal == 3: #........................movimento uniformemente variado
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        unif_var()
    elif menuprincipal == 4:#.......................lançamento obliquo
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        pesocorpo()
    elif menuprincipal == 5: #........................leis newton
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        leisnewton()
    elif menuprincipal == 9: #........................leis newton
        print_blue(f'Você selecionou [{menuprincipal}]')
        sleep(0.5)
        todos()
    rate(100)