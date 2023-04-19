#Um den Log nicht zu überschreiben muss man filemode auf 'a' stellen, um append statt overwrite zu machen

import logging

logging.basicConfig(filename='addieren.log', filemode='a', format='%(asctime)s - %(message)s',
                    level=logging.INFO)

logging.info("Skript gestartet")
a = input("Bitte erste Zahl eingeben:   ")
b = input("Bitte zweite Zahl eingeben:  ")

try:
    a = int(a)
    b = int(b)
    print(f"Ihre Zahlen waren: {a} und {b}")
    print(f"Das Ergebnis der Addition lautet {a + b}")
except ValueError as e:
    print("Sie haben keine zwei validen Zahlen eingegeben!")
    logging.error(f"Mindestens eine Eingabe war vom falschen Datentyp.")
else:
    logging.info(f"Addieren hat geklappt. Ergebnis: {a+b}")
