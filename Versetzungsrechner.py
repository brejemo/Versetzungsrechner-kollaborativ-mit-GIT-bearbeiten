def frage_nach_prozenten(lernfeld):
    while True:
        antwort = input("Nennen Sie den Prozentwert im Lernfeld " + lernfeld)
        if antwort.isdigit() and 0 <= int(antwort) <= 100:
            return int(antwort)
        else:
            print("Die Antwort muss zwischen 0 und 100 liegen und eine ganze Zahl sein!")


def bestimme_note(prozent):
    note = 6
    # bestimme hier abhängig vom eingegeben Prozentwert die Note
    return note


def bestimme_summe_der_note(note, lf1, lf2, lf3, lf5, deutsch, politik, sport):
    anzahl_note = 0
    # hier die Anzahl einer bestimmten Note bestimmen
    return anzahl_note


def pruefe_nicht_bestanden(anzahl_6, anzahl_5, anzahl_4, anzahl_3, anzahl_2, anzahl_1):
    nicht_bestanden = False
    # bestimme hier abhängig von der Anzahl der Noten, ob das Probehalbjahr nicht bestanden wurde
    return nicht_bestanden


def pruefe_bestanden_mit_ausgleich(anzahl_6, anzahl_5, anzahl_4, anzahl_3, anzahl_2, anzahl_1):
    bestanden_mit_ausgleich = False
    # bestimme hier abhängig von der Anzahl der Noten, ob das Probehalbjahr mit Ausgleich bestanden wurde
    return bestanden_mit_ausgleich


def pruefe_bestanden(anzahl_6, anzahl_5, anzahl_4, anzahl_3, anzahl_2, anzahl_1):
    bestanden = False
    # bestimme hier abhängig von der Anzahl der Noten, ob das Probehalbjahr bestanden wurde
    return bestanden


def bestimme_situation(bestanden, bestanden_mit_ausgleich, nicht_bestanden):
    situation = ""
    # hier abhängig von den parametern klären,
    # ob das Probehalbjahr bestanden wurde oder
    # mit Ausgleich bestanden wurde
    # oder nicht bestanden wurde
    return situation


def antworte(situation):
    antwort = "Aufgrund des Notenbildes ist das Probehalbjahr " + situation
    print(antwort)


def main():
    # In der main bitte die obigen Funktionen verwenden.
    # Hier bitte erst nach den Noten in allen Lernfeldern und Fächern fragen mit der Funktion frage_nach_note()
    # LF1, LF", LF3, LF5, dDeutsch, Politik, Sport
    #
    # Dann die Summe der sechsen, fünfen, vieren, dreien, zweien, und einsen in den LFS und Fächern bestimmen.
    # Anschließend mit den Funktionen überprüfen, ob das Probejahr nicht bestanden wurde,
    # mit Ausgleich bestanden wurde oder bestanden wurde und den entsprechdenen variablen zuweisen
    # bestanden = pruefe_bestanden(hier eure variablen für summen angeben)
    # bestanden mit ausgleich

    antworte("betanden")  # "bestanden" bitte durch eine Variable zur Situation ersetzen

main()
