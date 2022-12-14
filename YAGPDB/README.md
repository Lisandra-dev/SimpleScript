# Préambule
Pour créer une nouvelle "custom commands", suivez le guide ici : https://learn.yagpdb.xyz/the-custom-command-interface
Il suffit de copier coller chaque code dans une nouvelle custom commands, en utilisant : 
- Trigger type : Commmand (cmd/prefix)
- Trigger : Le nom que vous souhaitez

La commande sera alors utilisable en utilisant le préfixe défini dans le serveur, suivi du nom de la commande; par exemple, si vous avez mis `hello` en trigger, vous devrez utiliser `-hello` pour lancer la commande.

# Inscrire son personnage
🗒️ -> [Fichier](./inscript_chara.yag)

Syntaxe : -create <Force> <Endurance> <Agilité> <Constitution> <Education> <Intelligence> <Charisme> <Pouvoir> (nom du perso si DC ou PNJ) (@joueur)

- Les arguments entre parentheses sont optionnels, et peuvent être utilisé indépendemment
- Seuls les modérateurs peuvent créer des personnages pour d'autres joueurs. 

Exemples:
    - `-create 10 10 10 10 10 10 10 10 @Joueur` : Permet de mettre des stats à un autre joueur que soit-même
    - `-create 10 10 10 10 10 10 10 10 Nom du perso`: Permet de mettre des stats à un PNJ/DC qui nous appartient
    - `-create 10 10 10 10 10 10 10 10 Nom du perso @Joueur`: Met des stats à un PNJ/DC d'un autre joueur

Cette commande est nécessaire pour utiliser les autres commandes de ce bot.

# Afficher les stats d'un personnage
🗒️ -> [Fichier](./show_chara.yag)