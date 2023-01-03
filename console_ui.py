from biudzetas import Biudzetas

biudzetas = Biudzetas()

while True:
    ivedimas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - ataskaita\n4 - balansas\n0 - išeiti\n"))
    if ivedimas == 1:
        suma = float(input("Įveskite sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamu_irasa(suma, siuntejas, info)
    if ivedimas == 2:
        suma = float(input("Įveskite sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įsigyta prekė ar paslauga: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
    if ivedimas == 3:
        biudzetas.gauti_ataskaita()
    if ivedimas == 4:
        print("Balansas:", biudzetas.gauti_balansa())
    if ivedimas == 0:
        print("Viso gero")
        break
