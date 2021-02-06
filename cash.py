#!/usr/bin/python
import time
import random
global dificultad,cafe,cantidad,desicion,dinero,producto,vc,mvc,vl,mvl,s,y
global dificultad,vc,vl,vo,va,vp,vi,vv,vA,vm
dinero=100
dificultad = 0
producto = " "
desicion = 0
cafe = 1000
vm=0 #valor maximo usado para escalar el grafico
altura=0 #alto del grafico
ancho=0 #ancho del graifco
a=1 #valor que uso para trabajar lo aleatorio
maximo=100 #valor maximo para cambiar lo aleatorio aumentarlo aumenta la dificultad
mvc=200 #valor maximo variable en % para cafe
mvl=200 #valor maximo variable en % para limonada
mvo=1000 #valor maximo variable en % para oregano
mva=2000 #valor maximo variable en % para azucar
mvp=4000 #valor maximo variable en % para piedra
mvi=2500 #valor maximo variable en % para insulina
mvv=500 #valor maximo variable en % para vino
vc=1 #valor inicial del cafe
vl=1 #valor inicial limonada
vo=1 #valor inicial oregano
va=1 #valor inicial azucar
vp=1 #valor inicial piedra
vi=1 #valor inicial insulina
vv=1 #valor inicial vino
vA=4000000 #valor almas
cantidad = 0    #se usa para medir cantidad a comprar o vender
tiempo = 0
cafeina_recolectada = 0
acido_citrico_recolectado = 0
var=0#lo uso para mitigar UnboundLocalError: local variable 'cafe' referenced before assignment
dinero2 = 100#se usa para mitigar bugs al autoreferenciar la variable
s=[["$","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","7"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","6","9"," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," ","2"," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","2"," "," "," "," ","8","0","0"," "," "," ","0","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," ","2"," "," "," ","8","0"," ","0"," ","0"," ","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","m"," "," "," "," ","8","0"," "," ","0"," "," ","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," "," "," "," "," ","8","0"," "," "," "," "," ","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","7"," "," "," "," "," "," "," ","8","0"," "," "," "," "," ","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","6","9"," "," "," "," "," "," ","8","0"," "," "," "," "," ","0","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," ","2"," "," "," "," "," ","8"," ","0"," "," "," ","0"," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","2"," "," "," "," ","8"," "," ","0"," ","0"," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," ","2"," "," "," ","8"," "," "," ","0"," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","m"," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","7"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","6","9"," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," ","2"," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","2"," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," ","2"," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","m"," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","7"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" ","6","9"," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," ","2"," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","2"," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," "," ","2"," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","m"," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"],
   [" "," "," "," ","i"," "," "," "," ","8"," "," "," "," "," ","i"," ","8"," "," "," "," "," "," "," ","8"," "," "," "," "," ","7"," "," ","8"," "," "," "," "," ","7"]
   ]
i=0
x=0
y=0

int(dinero)
int(cafe)
int(cantidad)
int(var)
def mercado():
    global cafe,cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    #a=random.randint(1,maximo)
    #b = b*(a/100)#devuelve un porcentaje

    a=random.randint(30,mvc)
    vc = vc*(a/100)
    #print "%.2f" % vc
    #round(vc, 2)
    if vc < 1:
        vc=vc+1
    
    a=random.randint(1,mvl)
    vl = vl*(a/100)
    if vl < 1:
        vl=vl+1
    
#a=1#valor que uso para trabajar lo aleatorio
#maximo=100#valor maximo para cambiar lo aleatorio aumentarlo aumenta la dificultad
#mvc=100#valor maximo variable en % para cafe
#mvl=200#valor maximo variable en % para limonada
#mvo=1000#valor maximo variable en % para oregano
#mva=2000#valor maximo variable en % para azucar
#mvp=4000#valor maximo variable en % para piedra
#mvi=2500#valor maximo variable en % para insulina
#mvv=500#valor maximo variable en % para vino
#vc=1#valor inicial del cafe
#vl=1#valor inicial limonada
#vo=1#valor inicial oregano
#va=1#valor inicial azucar
#vp=1#valor inicial piedra
#vi=1#valor inicial insulina
#vv=1#valor inicial vino
def transaccion(valor):
    global cafe,cantidad,desicion,dinero,producto,vc
    if desicion == 2:#venta
        cantidad = int(input("cantidad: "))
        dinero = dinero+(cantidad*valor)
        producto = producto-cantidad
        desicion = 0

    if desicion == 1:#compra
        cantidad = int(input("cantidad: "))
        desicion = 0
        if (dinero-(cantidad*valor)>0):
            producto=producto+cantidad
            dinero = dinero-(cantidad*valor)
        else:
            print("no tienes suficientes fondos")
   
    
def productos():
    global cafe,cantidad,desicion,dinero,producto,vc
    print("elije un producto")
    print("C cafe")
    print("L limonada")
    print("O oregano")
    print("A azucar")
    print("P piedra")
    print("I insulina")
    print("V vino")
    print("@ alma")
    producto = str(input())
    if producto == "c":
        producto = cafe
        transaccion(vc)#vc = valor cafe
        cafe = producto
    
#$ valor de dinero
#C cafe
#L limonada
#O oregano
#A azucar
#P piedra
#I insulina
#V vino
#@ almas


def decidir():
    global cafe,cantidad,desicion,dinero,producto,vc,mvc,vl,mvl
    print('valor de cafe: ','%.2f' % vc,'limonada: ','%.2f' % vl)#print '%.2f' % vc esto redondea el valor
    print('elije: 1 = comprar, 2 = vender,3 = no hacer nada')
    print('cafe restante = ',cafe,'dinero = ',dinero)
    desicion = int(input())
    if desicion == 3:#nada
        print("sigamos")
        
    else:
        productos()


    print("procesando transaccion")
    print(desicion)  
def clase():
    print ("elije un personaje")
    print ("0 bagabundo")#cafe
    print ("1 pasante")#cafe
    print ("2 godinez")#cafe, impuestos
    print ("3 supervisor")# cafe, impuestos, empleados
    print ("4 empresario")#cafe, limonada, impuestos, empleados,
    print ("5 politico")#cafe, impuestos + y -,empleados, corrupcion(lavado)
    print ("6 banquero")#crea creditos y genera ganancias cafe, impuestos, corrupcion
    print ("7 traficante")#cafe, impuestos, oregano, azucar, piedra, insulina
    print ("8 mafioso")#cafe, impuestos, oregano, azucar, sal, insulina, empleados, corrupcion
    print ("9 clerigo")#cafe, pero solo genera vino, impuestos,
    print ("10 la parca")#acceso total productos, almas, impuestos,
    print ("11 el diablo mismo")#acesso total productos, almas, empleados,impuestos
    
def dificultades():
    global dificultad
    print ("elije dificultad")
    dificultad = int(input())
    comparar()
    
def comparar():
    global dificultad,vc,vl,vo,va,vp,vi,vv,vA
    if dificultad == 1:
        print(" ")
    if dificultad == 2:
        print(" ")
    if dificultad == 3:
        print(" ")
def comparar2():
    
    global dificultad,vc,vl,vo,va,vp,vi,vv,vA,vm
    if vc>vm:
        vm=vc
    if vl>vm:
        vm=vl
    if vo>vm:
        vm=vo
    if va>vm:
        vm=va
    if vp>vm:
        vm=vp
    if vi>vm:
        vm=vi
    if vv>vm:
        vm=vv
    int(vm)
    alto=29/vm
    int(alto)
    print("vm = ",vm)
    
def screen():#screen
    #global s,y
    print(s[0][0])
    #s=[
   
    for y in range(0, 29, 1):
             print(s[y][0],s[y][1],s[y][2],s[y][3],s[y][4],s[y][5],s[y][6],s[y][7],s[y][8],s[y][9],s[y][10],s[y][11],s[y][12],s[y][13],s[y][14],s[y][15],s[y][16],s[y][17],s[y][18],s[y][19],s[y][20],s[y][21],s[y][22],s[y][23],s[y][24],s[y][25],s[y][26],s[y][27],s[y][28],s[y][29],s[y][30],s[y][31],s[y][32],s[y][33],s[y][34],s[y][35],s[y][36],s[y][37],s[y][38])


dificultades()
while cafe>0:
    #screen()
    comparar2()
    tiempo = tiempo+1#puntuacion en dias
    cafe=cafe-1
    
    
    
    decidir()
    mercado()
    

    #time.sleep(1.5)
    
       
    if cafe == 0:
        print("GAME OVER")
        print("resultados:")
        #print("dificultad jugada: ",dificultad1)#poner en dificultad 1 el string correspondiente
        print("dias: ",tiempo)
        print("cafeina recolectada: ",cafeina_recolectada)
        print("acido citrico recolectado: ",acido_citrico_recolectado)
        print("almas encaminadas: ")
        print("almas recolectadas: ")
        print("almas consumidas: ")
        
        
    
def screen_test():
    for y in range(0, 29, 1):
             print (s[y][0],s[y][1],s[y][2],s[y][3],s[y][4],s[y][5],s[y][6],s[y][7],s[y][8],s[y][9],s[y][10],s[y][11],s[y][12],s[y][13],s[y][14],s[y][15],s[y][16],s[y][17],s[y][18],s[y][19],s[y][20],s[y][21],s[y][22],s[y][23],s[y][24],s[y][25],s[y][26],s[y][27],s[y][28],s[y][29],s[y][30],s[y][31],s[y][32],s[y][33],s[y][34],s[y][35],s[y][36],s[y][37],s[y][38])
    

  
    


def catastrofes():
    #pandemias
    #golpes de estado
    #pago de impuestos
    #asaltos
    #enfermedades
    #sindrome de abstencion
    #catastrofes naturales terremotos inundaciones incendios meteoritos
    #
 print ("s")
def info_mecanicas():
    print("sobre quien quieres saber sus mecanicas?")          

 

def pasante():
     print("descripcion")
     pasante_info = ("pasante, debil y pobreton, no recibe pago por su trabajo como asistente a teimpo parcial, no tiene que pagar impuestos a no ser que reciba sospechosas ganancias de nose donde, su vida es simple y aburrida necesita consumir 1 taza de cafe al dia o morira ")
     print(pasante_info)

  
def bagabundo():
    print("descripcion")
    bagabundo_info =("bla")


def get_shortened_integer(number_to_shorten):
    """ Takes integer and returns a formatted string """
    trailing_zeros = floor(log10(abs(number_to_shorten)))
    if trailing_zeros < 3:
        # Ignore everything below 1000
        return trailing_zeros
    elif 3 <= trailing_zeros <= 5:
        # Truncate thousands, e.g. 1.3k
        return str(round(number_to_shorten/(10**3), 1)) + 'k'
    elif 6 <= trailing_zeros <= 8:
        # Truncate millions like 3.2M
        return str(round(number_to_shorten/(10**6), 1)) + 'M'
    else:
        raise ValueError('Values larger or equal to a billion not supported')
#>>> get_shortened_integer(2300)
#2.3k # <-- str

#>>> get_shortened_integer(1300000)
#1.3M # <-- str


    
