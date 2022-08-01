import random
import sys
import argparse


# C'est probablement le code le plus dégueulasse que j'ai jamais écrit, mais il y avait trop de duplication pour m'empêcher de faire des fonctions.

# J'ai choisi de les nommer en fonction des lettres utilisées, mais il est possible que j'ai fait quelque fails de typo, donc je te laisse vérifier.

# Pour appeler la commande : python gothiqueGenerator.py -n <nombre de mot à générer>


def random_TV(liste_T, voyelle):
    return random.choice(liste_T) + random.choice(voyelle)


def random_CSV(consonne, liste_S, voyelle):
    return random.choice(consonne) + random.choice(liste_S) + random.choice(voyelle)


def random_CSVS(consonne, liste_S, voyelle):
    return random.choice(consonne) + random.choice(liste_S) + random.choice(voyelle) + random.choice(liste_S)


def random_CSVC(consonne, voyelle, liste_S):
    return random_CSV(consonne, liste_S, voyelle) + random.choice(consonne)


def random_CV(consonne, voyelle):
    return random.choice(consonne) + random.choice(voyelle)


def random_CVC(consonne, voyelle):
    return random_CV(consonne, voyelle) + random.choice(consonne)


def random_CVSC(consonne, voyelle, liste_S):
    return random_CV(consonne, voyelle) + random.choice(liste_S) + random.choice(consonne)


def random_voy(voyelle):
    return random.choice(voyelle)


def random_VC(consonne, voyelle):
    return random_voy(voyelle) + random.choice(consonne)


def bs1_generator(consonne, voyelle, liste_S, liste_T):
    BS1 = random.randint(1, 54)
    if BS1 <= 3:
        return random_TV(liste_T, voyelle)
    elif BS1 <= 5:
        return random_CV(consonne, voyelle)
    elif BS1 <= 7:
        return random_CSVS(consonne, liste_S, voyelle)
    elif BS1 < 16:
        return random_CV(consonne, voyelle)
    elif BS1 < 40:
        return random_CV(consonne, voyelle)
    elif BS1 < 47:
        return random_CVSC(consonne, voyelle, liste_S)
    elif BS1 < 49:
        return random_voy(voyelle)
    else:
        return random_VC(consonne, voyelle)


def bs2_generator(consonne, voyelle, liste_S):
    BS2 = random.randint(1, 43)
    if BS2 <= 2:
        return random_CSV(consonne, liste_S, voyelle)
    elif BS2 <= 4:
        return random_CSVC(consonne, voyelle, liste_S)
    elif BS2 < 13:
        return random_CV(consonne, voyelle)
    elif BS2 < 37:
        return random_CVC(consonne, voyelle)
    else:
        return random_CVSC(consonne, voyelle, liste_S)


def bs3_generator(consonne, voyelle, liste_S, liste_W):
    BS3 = random.randint(1, 46)
    if BS3 == 1:
        return random.choice(consonne) + random.choice(consonne)
    elif BS3 <= 3:
        return random_CSV(consonne, liste_S, voyelle)
    elif BS3 <= 5:
        return random_CSVC(consonne, voyelle, liste_S)
    elif BS3 < 14:
        return random_CV(consonne, voyelle)
    elif BS3 < 38:
        return random_CVC(consonne, voyelle)
    elif BS3 < 45:
        return random_CVSC(consonne, voyelle, liste_S)
    else:
        return random_CV(consonne, voyelle) + random.choice(liste_W)


if __name__ == "__main__":
    consonne = [i for j in ['b' * 4, 'l' * 4, 's' * 8, 'n' * 11, 'd' * 6, 't' * 7, 'k' * 6, 'm' * 5, 'g' * 3, 'r' * 8, 'f' * 1,
                'y' * 4, 'th' * 2, 'p' * 5, 'z' * 10, 'h' * 2, 'w' * 5, 'ź' * 2, 'ś' * 7] for i in j]
    voyelle = [i for j in ['a' * 8, 'o' * 7, 'u' * 2, 'e' * 4, 'i' * 4]
               for i in j]

    liste_S = [i for j in ['l' * 4, 'r' * 7] for i in j]
    liste_W = ['w', 'y']
    liste_T = ['st']
    parser = argparse.ArgumentParser(description="Génère des noms fictifs aléatoires",
                                     formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", "--nombre", type=int,
                        default=100, help="Nombre de noms à générer")
    args = parser.parse_args()
    p = 0
    result = ''
    while p < args.nombre:
        NBS = random.randint(1, 3)
        if NBS == 1:
            result += bs2_generator(consonne, voyelle, liste_S)
        elif NBS == 2:
            S1 = bs1_generator(consonne, voyelle, liste_S, liste_T)
            S3 = bs3_generator(consonne, voyelle, liste_S, liste_W)
            result += S1 + S3
        else:
            S1 = bs1_generator(consonne, voyelle, liste_S, liste_T)
            S2 = bs2_generator(consonne, voyelle, liste_S)
            S3 = bs3_generator(consonne, voyelle, liste_S, liste_W)
            result += S1 + S2 + S3
        p += 1
        result = result + '\n'
    print(result)
    sys.exit(0)
