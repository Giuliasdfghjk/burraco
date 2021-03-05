


def burraco():
    #impostare valore punti
    punti_totali= 0
    bur_pulito = 200
    but_sporco = 100
    pinella = 20
    jolly = 30
    asso = 15
    k_otto = 10
    sette_tre = 5
    #inizio calcolo punti
    a = input("Sei il giocatore che ha effettuato la chiusura? \n Sì   No  \n")
    if a == "Sì" or a == "sì" or a == "si" or a == "Si":
        punti_totali += 100
    else:
        pass
    b= input("Inserisci il numero di BURRACO PULITI: \n")
    punti_totali += int(b) * int(bur_pulito)
    c = input("Inserisci il numero di BURRACO SPORCHI: \n")
    punti_totali += int(c) * int(but_sporco)
    d = input("Inserisci il numero di PINELLE: \n")
    punti_totali += int(d) * int(pinella)
    e = input("Inserisci il numero di JOLLY: \n")
    punti_totali += int(e) * int(jolly)
    f = input("Inserisci il numero di ASSI: \n")
    punti_totali += int(f) * int(asso)
    g = input("Inserisci il numero di carte comprese fra K (13) e 8: \n")
    punti_totali += int(g) * int(k_otto)
    h = input("Inserisci il numero di carte comprese fra 7 e 3: \n")
    punti_totali += int(h) * int(sette_tre)

    print("Punti totali:", punti_totali)
burraco()
