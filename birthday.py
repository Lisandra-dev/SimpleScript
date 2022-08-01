import argparse
import datetime
import random
import sys

def birthday(year=None, age=None, mode="numeric"):
    """
    Génère une date d'anniversaire aléatoirement.
    Parameters
    ----------
    year : int
        L'année à utiliser.
    age : int
        L'âge à utiliser (en années).
    mode : str
        Le mode de génération, numerique ou full.
    Returns
    -------
    str:
        The birthday.
    """
    if year and age:
        year = year - age
    elif age:
        year = datetime.datetime.now().year - age
    month_nb = random.randint(1, 12)
    if year and month_nb == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        day_nb = random.randint(1, 29)
    elif month_nb in [1, 3, 5, 7, 8, 10, 12]:
        day_nb = random.randint(1, 31)
    elif month_nb in [4, 6, 9, 11]:
        day_nb = random.randint(1, 30)
    else:
        day_nb = random.randint(1, 28)
    month_name = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Aout', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    day_name = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
    if mode == "full":
        if year:
            day_convert = day_name[datetime.datetime(year, month_nb, day_nb).isoweekday()-1]
        else:
            day_convert=day_name[random.randint(0, 6)]
        if day_nb == 1:
            day_convert = day_convert + "er"
        day_final = f"{day_convert} {day_nb} {month_name[month_nb]}"
    else:
        if month_nb < 10:
            month_nb = f"0{month_nb}"
        day_final = f"{day_nb}/{month_nb}"
    if year and mode == "full":
        day_final = f"{day_final} {year}"
    elif year:
        day_final = f"{day_final}/{year}"
    return day_final

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Génère une date d'anniversaire aléatoire.")
    parser.add_argument("-y", "--year", type=int, help="L'année à utiliser.")
    parser.add_argument("-a", "--age", type=int, help="L'âge, si on veut générer une année. (Par défaut, l'année actuelle sera utilisée.)")
    parser.add_argument("-m", "--mode", type=str, choices=["numeric", "full"], default="numeric", help="Le mode d'affichage de la date. Full: Affiche avec le jour de la semaine, le nom du mois et l'année. Numeric: Affiche uniquement le jour et le mois (en nombre).")
    args = parser.parse_args()
    print("La date d'anniversaire est le", birthday(year=args.year, age=args.age, mode=args.mode))
    sys.exit(0)