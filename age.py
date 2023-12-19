import time
import sys                
az = input('age : ')
a = float(az
          )

if a >110:
    print("Impossible d'exister et tu as menti,ou alors tu es un revenant!")
    ae = input('Donne ton vrai age !!!!!!!!!!!! : ')
    aa = float(ae)
    if aa < 5:
        print('Bébé! Et menteur avec ça!!!')
    if aa >5 and aa < 25:
        print("C'est paaaaas bieeeen de mentiiiiiiir !!!!!(ton réprobateur)")
    if aa >24 and aa <111:
        print("Gros menteur")
    if aa >110 and aa <155:
        print("peut - être...")
        aae = input("est-tu un pépé ou une mémé (de l'EHPAD ou pas) ?(O/N)")
        if aae == "O" or aae == "o":
            aaaa = input("est-tu un pépé ou une mémé ?(P/N)")
            if aaaa == "P" or aaaa == "p":
                print("Gros pépé menteur")
                time.sleep(4)
                sys.exit
            if aaaa == "M" or aaaa == "m":
                print("Grose mémé menteuse")
                time.sleep(4)
                sys.exit 
        if aae == "111" or aae == aa or aae == a:
            print("Gros bébé ! Et gros menteur avec ça! Espèce de gros !")
            time.sleep(4)
            sys.exit
        if aae == "N" or aae == "n":
            time.sleep(0.5)
            print("FANTOME!!!!!!")
            time.sleep(0.5)
            print("AU SECOUUUUUUURS")
            time.sleep(0.5)
            print("J'hallucine!!!!!")
            print()
            time.sleep(0.4)
            print()
            print()
            time.sleep(0.4)
            print("                      ________")
            time.sleep(0.3)
            print("           _____     /        \\     _____")
            time.sleep(0.3)
            print("           \\    \\   /  .    .  \\   /    /")
            time.sleep(0.3)
            print("            \\    \\  |          |  /    /")
            time.sleep(0.3)
            print("             \\    \\ |          | /    / ")
            time.sleep(0.3)
            print("              \\    \\|          |/    /")  
            time.sleep(0.3)
            print("               \\    |          |    /")
            time.sleep(0.3)
            print("                \\   |          |   /")
            time.sleep(0.3)
            print("                 \\  |          |  /")
            time.sleep(0.3)
            print("                  \\ |          | /")
            time.sleep(0.3)
            print("                   \\|          |/")
            time.sleep(0.3)
            print("                    |          |")
            time.sleep(0.3)
            print("                    /           \\")
            time.sleep(0.3)
            print("                   /             \\")
            time.sleep(0.3)
            print("                  /               \\")
            time.sleep(0.3)
            print("                 /   __   __   __  \\")
            time.sleep(0.3)
            print("                /___/  \\_/  \\_/  \\__\\")
            time.sleep(4)
            time.sleep(4)
            sys.exit
        elif aae == float:
            print("T'as rien compris.")
            time.sleep(4)
            sys.exit

            
    if aa >150:
        time.sleep(0.5)
        print("FANTOME!!!!!!")
        time.sleep(0.5)
        print("AU SECOUUUUUUURS")
        time.sleep(0.5)
        print("J'hallucine!!!!!")
        print()
        time.sleep(0.4)
        print()
        print()
        time.sleep(0.4)
        print("                      ________")
        time.sleep(0.3)
        print("           _____     /        \\     _____")
        time.sleep(0.3)
        print("           \\    \\   /  .    .  \\   /    /")
        time.sleep(0.3)
        print("            \\    \\  |          |  /    /")
        time.sleep(0.3)
        print("             \\    \\ |          | /    / ")
        time.sleep(0.3)
        print("              \\    \\|          |/    /")  
        time.sleep(0.3)
        print("               \\    |          |    /")
        time.sleep(0.3)
        print("                \\   |          |   /")
        time.sleep(0.3)
        print("                 \\  |          |  /")
        time.sleep(0.3)
        print("                  \\ |          | /")
        time.sleep(0.3)
        print("                   \\|          |/")
        time.sleep(0.3)
        print("                    |          |")
        time.sleep(0.3)
        print("                    /           \\")
        time.sleep(0.3)
        print("                   /             \\")
        time.sleep(0.3)
        print("                  /               \\")
        time.sleep(0.3)
        print("                 /   __   __   __  \\")
        time.sleep(0.3)
        print("                /___/  \\_/  \\_/  \\__\\")
        time.sleep(4)

if a >0 and a <=2.5:
    print('bébé !')
if a >2.5 and a <=5:
    print('Grandis vite !')
if a >5 and a <=13:
    print('bien,tu est assez jeune')
if a >13 and a <=18:
    print('Passe bien ton brevet et ton bac !')
if a >18 and a <=30:
    print('Tu as l\'age qu\'il faut')
if a >30 and a <=110:
    print('Tu est trop vieux de %s années.' % (a - 30))