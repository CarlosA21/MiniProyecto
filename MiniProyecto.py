import random
players = []
cartas = ["As",1,2,3,4,5,6,7,8,9,10,"J","K","Q"]
j = 10
k = 10
q = 10
p1a = 0
def game():
    print ("Bienvenido a 21 Blackjack")
    numJugadores = input("Cuantos jugadores participaran?")
    if (numJugadores == 1):
        print("Debe haber al menos un jugador en la mesa")
        numJugadores = input("Cuantos jugadores participaran?")
    else:
        for nombre in range(0, numJugadores):
            print("Introduzca nombre del jugador:")
            nombre = raw_input()
            players.append(nombre)
        print("EL JUEGO VA A EMPEZAR")
        p = len(players)
        cartasmesa1 = random.choice(cartas)
        cartasmesa2 = random.choice(cartas)

        print ('{},Cartas del Croupier,{},{}'.format(cartasmesa1))
        #INICIO ASIGNACION CARTAS
        if (p == 2):
            cartasp11 = random.choice(cartas)
            cartasp12 = random.choice(cartas)
            cartasp21 = random.choice(cartas)
            cartasp22 = random.choice(cartas)
            print "------------------"
            print (players[0], "Tus cartas son" , cartasp11,cartasp12)
            print (players[1], "Tus cartas son" , cartasp21,cartasp22)
            print "------------------"
        elif (p == 3):
            cartasp11 = random.choice(cartas)
            cartasp12 = random.choice(cartas)
            cartasp21 = random.choice(cartas)
            cartasp22 = random.choice(cartas)
            cartasp31 = random.choice(cartas)
            cartasp32 = random.choice(cartas)
            print (players[0], "Tus cartas son" , cartasp11,cartasp12)
            print (players[1], "Tus cartas son" , cartasp21,cartasp22)
            print (players[2], "Tus cartas son" , cartasp31,cartasp32)
        elif (p == 4):
            cartasp11 = random.choice(cartas)
            cartasp12 = random.choice(cartas)
            cartasp21 = random.choice(cartas)
            cartasp22 = random.choice(cartas)
            cartasp31 = random.choice(cartas)
            cartasp32 = random.choice(cartas)
            cartasp41 = random.choice(cartas)
            cartasp42 = random.choice(cartas)
            print (players[0], "Tus cartas son", cartasp11, cartasp12)
            print (players[1], "Tus cartas son", cartasp21, cartasp22)
            print (players[2], "Tus cartas son", cartasp31, cartasp32)
            print (players[3], "Tus cartas son", cartasp41, cartasp42)
        elif (p == 5):
            cartasp11 = random.choice(cartas)
            cartasp12 = random.choice(cartas)
            cartasp21 = random.choice(cartas)
            cartasp22 = random.choice(cartas)
            cartasp31 = random.choice(cartas)
            cartasp32 = random.choice(cartas)
            cartasp41 = random.choice(cartas)
            cartasp42 = random.choice(cartas)
            cartasp51 = random.choice(cartas)
            cartasp52 = random.choice(cartas)
            print (players[0], "Tus cartas son", cartasp11, cartasp12)
            print (players[1], "Tus cartas son", cartasp21, cartasp22)
            print (players[2], "Tus cartas son", cartasp31, cartasp32)
            print (players[3], "Tus cartas son", cartasp41, cartasp42)
            print (players[4], "Tus cartas son", cartasp51, cartasp52)
        #FIN ASIGNACION CARTAS


        #INICIO APUESTAS
        if (p == 2):
            print "---------------"
            print('{},QUE Cantidad Apostaras {},{}'.format(players[0],"?"))
            p1a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[1],"?"))
            p2a = raw_input()
            print "---------------"
        elif (p == 3):
            print "---------------"
            print('{},QUE Cantidad Apostaras {},{}'.format(players[0], "?"))
            p1a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[1], "?"))
            p2a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[2], "?"))
            p3a = raw_input()
            print "---------------"
        elif (p == 4):
            print "---------------"
            print('{},QUE Cantidad Apostaras {},{}'.format(players[0], "?"))
            p1a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[1], "?"))
            p2a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[2], "?"))
            p3a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[3], "?"))
            p4a = raw_input()
            print "---------------"
        elif (p == 5):
            print "---------------"
            print('{},QUE Cantidad Apostaras {},{}'.format(players[0], "?"))
            p1a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[1], "?"))
            p2a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[2], "?"))
            p3a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[3], "?"))
            p4a = raw_input()
            print('{},Que Cantidad Apostaras {},{}'.format(players[4], "?"))
            p5a = raw_input()
            print "---------------"
        #FIN APUESTAS


        #INICIO TURNOS

        #TURNOS 2 JUGADORES
        if (p == 2):
            print "------------"
            print('{}Turno de{},{}'.format(players[0]))
            print('{}Que deseas hacer{},{}'.format(players[0]))
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p1 = input("")
            #player1
            if (p1 == 1):
                print(players[0], "Se ha plantado")
            elif (p1 == 2):
                print ("Funcion no disponible")
            elif (p1 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p1 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p1 == 5):
                cartasp13 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp11,cartasp12,cartasp13)
            print("Turno de:", players[1])
            print(players[1], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p2 = input("")
            if (p2 == 1):
                print(players[0], "Se ha plantado")
            elif (p2 == 2):
                print ("Funcion no disponible")
            elif (p2 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p2 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p2 == 5):
                cartasp23 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp21, cartasp22, cartasp23)

        #TURNOS 3 JUGADORES
        if (p == 3):
            #TURNO PLAYER 1
            print("Turno de:", players[0])
            print(players[0], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p1 = input("")

            if (p1 == 1):
                print(players[0], "Se ha plantado")
            elif (p1 == 2):
                print ("Funcion no disponible")
            elif (p1 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p1 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p1 == 5):
                cartasp13 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp11, cartasp12, cartasp13)


             #TURNO PLAYER 2
            print("Turno de:", players[1])
            print(players[1], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p2 = input("")
            if (p2 == 1):
                print(players[0], "Se ha plantado")
            elif (p2 == 2):
                print ("Funcion no disponible")
            elif (p2 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p2 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p2 == 5):
                cartasp23 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp21, cartasp22, cartasp23)



            #TURNO PLAYER 3
            print("Turno de:", players[2])
            print(players[2], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p3 = input("")
            if (p3 == 1):
                print(players[2], "Se ha plantado")
            elif (p3 == 2):
                print ("Funcion no disponible")
            elif (p3 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p3 == 4):
                print(players[2], "SE HA RENDIDO")
            elif (p3 == 5):
                cartasp33 = random.choice(players)
                print(players[2], "Nuevas Cartas:", cartasp31, cartasp32, cartasp33)


        #TURNOS 4 JUGADORES
        if (p == 4):
                # TURNO PLAYER 1
                print("Turno de:", players[0])
                print(players[0], "Que Deseas hacer?")
                print ("1. Plantarte")
                print("2. Separar")
                print("3. Doblar")
                print("4. Rendirse")
                print("5. Pedir")
                p1 = input("")

                if (p1 == 1):
                    print(players[0], "Se ha plantado")
                elif (p1 == 2):
                    print ("Funcion no disponible")
                elif (p1 == 3):
                    print ("Apuesta Inicial:", p1a)
                    dob = p1a * 2
                    print ("Apuesta Doblada: ", dob)
                elif (p1 == 4):
                    print(players[0], "SE HA RENDIDO")
                elif (p1 == 5):
                    cartasp13 = random.choice(players)
                    print(players[0], "Nuevas Cartas:", cartasp11, cartasp12, cartasp13)

                # TURNO PLAYER 2
                print("Turno de:", players[1])
                print(players[1], "Que Deseas hacer?")
                print ("1. Plantarte")
                print("2. Separar")
                print("3. Doblar")
                print("4. Rendirse")
                print("5. Pedir")
                p2 = input("")
                if (p2 == 1):
                    print(players[0], "Se ha plantado")
                elif (p2 == 2):
                    print ("Funcion no disponible")
                elif (p2 == 3):
                    print ("Apuesta Inicial:", p1a)
                    dob = p1a * 2
                    print ("Apuesta Doblada: ", dob)
                elif (p2 == 4):
                    print(players[0], "SE HA RENDIDO")
                elif (p2 == 5):
                    cartasp23 = random.choice(players)
                    print(players[0], "Nuevas Cartas:", cartasp21, cartasp22, cartasp23)

                # TURNO PLAYER 3
                print("Turno de:", players[2])
                print(players[2], "Que Deseas hacer?")
                print ("1. Plantarte")
                print("2. Separar")
                print("3. Doblar")
                print("4. Rendirse")
                print("5. Pedir")
                p3 = input("")
                if (p3 == 1):
                    print(players[2], "Se ha plantado")
                elif (p3 == 2):
                    print ("Funcion no disponible")
                elif (p3 == 3):
                    print ("Apuesta Inicial:", p1a)
                    dob = p1a * 2
                    print ("Apuesta Doblada: ", dob)
                elif (p3 == 4):
                    print(players[2], "SE HA RENDIDO")
                elif (p3 == 5):
                    cartasp33 = random.choice(players)
                    print(players[2], "Nuevas Cartas:", cartasp31, cartasp32, cartasp33)

                #TURNO P4
                print("Turno de:", players[3])
                print(players[3], "Que Deseas hacer?")
                print ("1. Plantarte")
                print("2. Separar")
                print("3. Doblar")
                print("4. Rendirse")
                print("5. Pedir")
                p4 = input("")
                if (p4 == 1):
                    print(players[3], "Se ha plantado")
                elif (p4 == 2):
                    print ("Funcion no disponible")
                elif (p4 == 3):
                    print ("Apuesta Inicial:", p1a)
                    dob = p1a * 2
                    print ("Apuesta Doblada: ", dob)
                elif (p4 == 4):
                    print(players[3], "SE HA RENDIDO")
                elif (p4 == 5):
                    cartasp43 = random.choice(players)
                    print(players[3], "Nuevas Cartas:", cartasp41, cartasp42, cartasp43)



        #TURNO 5 JUGADORES
        if (p == 5):
            # TURNO PLAYER 1
            print("Turno de:", players[0])
            print(players[0], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p1 = input("")

            if (p1 == 1):
                print(players[0], "Se ha plantado")
            elif (p1 == 2):
                print ("Funcion no disponible")
            elif (p1 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p1 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p1 == 5):
                cartasp13 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp11, cartasp12, cartasp13)

            # TURNO PLAYER 2
            print("Turno de:", players[1])
            print(players[1], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p2 = input("")
            if (p2 == 1):
                print(players[0], "Se ha plantado")
            elif (p2 == 2):
                print ("Funcion no disponible")
            elif (p2 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p2 == 4):
                print(players[0], "SE HA RENDIDO")
            elif (p2 == 5):
                cartasp23 = random.choice(players)
                print(players[0], "Nuevas Cartas:", cartasp21, cartasp22, cartasp23)

            # TURNO PLAYER 3
            print("Turno de:", players[2])
            print(players[2], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p3 = input("")
            if (p3 == 1):
                print(players[2], "Se ha plantado")
            elif (p3 == 2):
                print ("Funcion no disponible")
            elif (p3 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p3 == 4):
                print(players[2], "SE HA RENDIDO")
            elif (p3 == 5):
                cartasp33 = random.choice(players)
                print(players[2], "Nuevas Cartas:", cartasp31, cartasp32, cartasp33)

            # TURNO P4
            print("Turno de:", players[3])
            print(players[3], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p4 = input("")
            if (p4 == 1):
                print(players[3], "Se ha plantado")
            elif (p4 == 2):
                print ("Funcion no disponible")
            elif (p4 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p4 == 4):
                print(players[3], "SE HA RENDIDO")
            elif (p4 == 5):
                cartasp43 = random.choice(players)
                print(players[3], "Nuevas Cartas:", cartasp41, cartasp42, cartasp43)
            # TURNO P5

            print("Turno de:", players[4])
            print(players[4], "Que Deseas hacer?")
            print ("1. Plantarte")
            print("2. Separar")
            print("3. Doblar")
            print("4. Rendirse")
            print("5. Pedir")
            p4 = input("")
            if (p4 == 1):
                print(players[4], "Se ha plantado")
            elif (p4 == 2):
                print ("Funcion no disponible")
            elif (p4 == 3):
                print ("Apuesta Inicial:", p1a)
                dob = p1a * 2
                print ("Apuesta Doblada: ", dob)
            elif (p4 == 4):
                print(players[4], "SE HA RENDIDO")
            elif (p4 == 5):
                cartasp53 = random.choice(players)
                print(players[4], "Nuevas Cartas:", cartasp51, cartasp52, cartasp53)

        print("LA CASA MUESTRA SU SEGUNDA CARTA", cartasmesa2)
        casa = len(players)
        #LETRAS P1
        if (cartasp11 == "J"):
            cartasp11 = 10;
        elif (cartasp11 == "K"):
            cartasp11 = 10
        elif(cartasp11 == "Q"):
            cartasp11 = 10
        if (cartasp12 == "J"):
            cartasp12 = 10;
        elif (cartasp12 == "K"):
            cartasp12 = 10
        elif (cartasp12 == "Q"):
            cartasp12 = 10

         #LETRAS P2
        elif (cartasp21 == "J"):
            cartasp21 = 10;
        elif (cartasp21 == "K"):
            cartasp21 = 10
        elif(cartasp21 == "Q"):
            cartasp21 = 10
        elif (cartasp22 == "J"):
            cartasp22 = 10;
        elif (cartasp22 == "K"):
            cartasp22 = 10
        elif (cartasp22 == "Q"):
            cartasp22 = 10

        #LETRAS P3
        elif (cartasp31 == "J"):
            cartasp31 = 10;
        elif (cartasp31 == "K"):
            cartasp31 = 10
        elif(cartasp31 == "Q"):
            cartasp31 = 10
        elif (cartasp32 == "J"):
            cartasp32 = 10;
        elif (cartasp32 == "K"):
            cartasp32 = 10
        elif (cartasp32 == "Q"):
            cartasp32 = 10
         #LETRAS P4
        elif (cartasp41 == "J"):
            cartasp41 = 10;
        elif (cartasp41 == "K"):
            cartasp41 = 10
        elif (cartasp41 == "Q"):
            cartasp41 = 10
        elif (cartasp42 == "J"):
            cartasp42 = 10;
        elif (cartasp42 == "K"):
            cartasp42 = 10
        elif (cartasp42 == "Q"):
            cartasp42 = 10

         #LETRAS P5
        elif (cartasp51 == "J"):
            cartasp41 = 10;
        elif (cartasp51 == "K"):
            cartasp41 = 10
        elif (cartasp51 == "Q"):
            cartasp41 = 10
        elif (cartasp52 == "J"):
            cartasp52 = 10;
        elif (cartasp52 == "K"):
            cartasp52 = 10
        elif (cartasp52 == "Q"):
            cartasp52 = 10
        if (cartasp11 + cartasp12 > cartasmesa1+cartasmesa2):
            print(players[0],"BLACKJACK, HAZ GANADO LA RONDA Y LA SUMA DE ", p1a )
        elif (cartasp11 + cartasp12 < cartasmesa1+cartasmesa2):
            print(players[0],"LO SENTIMOS, HAZ PERDIDO LA RONDA")
        if (cartasp21 + cartasp22 > cartasmesa1+cartasmesa2):
            print(players[1],"BLACKJACK, HAZ GANADO LA RONDA Y LA SUMA DE ", p2a)
        elif (cartasp22 + cartasp22 < cartasmesa1+cartasmesa2):
            print(players[1],"LO SENTIMOS, HAZ PERDIDO LA RONDA")
        if (cartasp31 + cartasp32 > cartasmesa1+cartasmesa2):
            print(players[2],"BLACKJACK, HAZ GANADO LA RONDA Y LA SUMA DE ", p3a)
        elif (cartasp31 + cartasp32 < cartasmesa1+cartasmesa2):
            print(players[2],"LO SENTIMOS, HAZ PERDIDO LA RONDA")
        if (cartasp41 + cartasp42 > cartasmesa1+cartasmesa2):
            print(players[3],"BLACKJACK, HAZ GANADO LA RONDA Y LA SUMA DE ", p4a)
        elif (cartasp41 + cartasp42 < cartasmesa1+cartasmesa2):
            print(players[3],"LO SENTIMOS, HAZ PERDIDO LA RONDA")
        if (cartasp51 + cartasp52 > cartasmesa1+cartasmesa2):
            print(players[4],"BLACKJACK, HAZ GANADO LA RONDA Y LA SUMA DE ", p5a)
        elif (cartasp51 + cartasp52 < cartasmesa1+cartasmesa2):
            print(players[4],"LO SENTIMOS, HAZ PERDIDO LA RONDA")
        if (cartasp11 + cartasp12 == cartasmesa1+cartasmesa2):
            print(players[0], "USTED Y LA CASA HAN QUEDADO EMPATE")
        if (cartasp21 + cartasp22 == cartasmesa1+cartasmesa2):
            print(players[0], "USTED Y LA CASA HAN QUEDADO EMPATE")
        if (cartasp31 + cartasp32 == cartasmesa1+cartasmesa2):
            print(players[0], "USTED Y LA CASA HAN QUEDADO EMPATE")
        if (cartasp41 + cartasp52 == cartasmesa1+cartasmesa2):
            print(players[0], "USTED Y LA CASA HAN QUEDADO EMPATE")
        if (cartasp51 + cartasp52 == cartasmesa1+cartasmesa2):
            print(players[0], "USTED Y LA CASA HAN QUEDADO EMPATE")
game()



