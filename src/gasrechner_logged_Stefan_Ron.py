import logging

logging.basicConfig(filename="gasrechner.log",
                    filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logging.info('Skript gestartet')

def gasrechner(gaspreis=12, grundgebuehr=15, abschlag=150, vorjahr=15000):
    try:
        endabrechnung = abschlag*12 - (gaspreis*vorjahr/100 + 12*grundgebuehr)
    except:
        logging.error("Falsche eingabe")
        print("Tut mir leid. Ich habe Ihre Eingabe nicht verstanden.")
    else:
        if endabrechnung > 0:
            logging.info(f"{endabrechnung} zurück")
            print(f"Sie erhalten {round(endabrechnung,2)} Euro zurück und könnten den Abschlag auf {round(abschlag-endabrechnung/12,2)} Euro senken!")
        elif endabrechnung < 0:
            logging.info(f"{endabrechnung} nachzahlen")
            print(f"Achtung! Sie müssen {round(endabrechnung,2)} Euro nachzahlen! Erhöhen Sie Ihren Abschlag auf {round(abschlag-endabrechnung/12,2)} Euro, um bei 0 rauszukommen!")
        else:
            logging.info("Alles Okay")
            print("Alles okay. Sie kommen genau bei 0 Euro raus.")

gasrechner()
