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
    lf1_note = bestimme_note(frage_nach_prozenten("LF1"))
    lf2_note = bestimme_note(frage_nach_prozenten("LF2"))
    lf3_note = bestimme_note(frage_nach_prozenten("LF3"))
    lf5_note = bestimme_note(frage_nach_prozenten("LF5"))
    deutsch_note = bestimme_note(frage_nach_prozenten("Deutsch"))
    politik_note = bestimme_note(frage_nach_prozenten("Politik"))
    sport_note = bestimme_note(frage_nach_prozenten("Sport"))

    summe_6 = bestimme_summe_der_note(6, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)
    summe_5 = bestimme_summe_der_note(5, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)
    summe_4 = bestimme_summe_der_note(4, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)
    summe_3 = bestimme_summe_der_note(3, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)
    summe_2 = bestimme_summe_der_note(2, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)
    summe_1 = bestimme_summe_der_note(1, lf1_note, lf2_note, lf3_note, lf5_note, deutsch_note, politik_note, sport_note)

    bestanden = pruefe_bestanden(summe_6, summe_5, summe_4, summe_3, summe_2, summe_1)
    bestanden_mit_ausgleich = pruefe_bestanden_mit_ausgleich(summe_6, summe_5, summe_4, summe_3, summe_2, summe_1)
    nicht_bestanden = pruefe_nicht_bestanden(summe_6, summe_5, summe_4, summe_3, summe_2, summe_1)

    situation = bestimme_situation(bestanden, bestanden_mit_ausgleich, nicht_bestanden)
    antworte(situation)


main()
