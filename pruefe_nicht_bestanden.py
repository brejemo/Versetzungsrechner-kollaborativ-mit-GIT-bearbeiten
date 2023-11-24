anzahl_1 = int(input("Nennen sie die Anzahl der Note 1: "))
anzahl_2 = int(input("Nennen sie die Anzahl der Note 2: "))
anzahl_3 = int(input("Nennen sie die Anzahl der Note 3: "))
anzahl_4 = int(input("Nennen sie die Anzahl der Note 4: "))
anzahl_5 = int(input("Nennen sie die Anzahl der Note 5: "))
anzahl_6 = int(input("Nennen sie die Anzahl der Note 6: "))

# bestimme, ob das probejahr nicht bestanden ist
# nciht bestanden ist das probejahr, wenn
# es eine 6 und keine 2 oder 1 gibt
# wenn es zwei 5 und keine 3 oder 2 oder 1 gibt
# wenn es 6 und 5 gibt
# wenn es zweimal oder merh 6 gibt
# wenn es dreimal 5 gibt

nicht_bestanden = False

# gib in der Konsole aus, ob nicht bestanden wurde