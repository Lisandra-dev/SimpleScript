# Préambule
Pour créer une nouvelle "custom commands", suivez le guide ici : https://learn.yagpdb.xyz/the-custom-command-interface
Il suffit de copier coller chaque code dans une nouvelle custom commands, en utilisant : 
- Trigger type : Commmand (cmd/prefix)
- Trigger : Le nom que vous souhaitez

La commande sera alors utilisable en utilisant le préfixe défini dans le serveur, suivi du nom de la commande; par exemple, si vous avez mis `hello` en trigger, vous devrez utiliser `-hello` pour lancer la commande.

> **Note** Par défaut, le préfixe est `-`. Vous pouvez aussi nommer les commandes comme vous le souhaitez.

# Inscrire son personnage
🗒️ -> [Fichier](./inscript_chara.yag)

> **Note** Par défaut le trigger utilisé est `-create`

Syntaxe : `-create <Force> <Endurance> <Agilité> <Constitution> <Education> <Intelligence> <Charisme> <Pouvoir> (nom du perso si DC ou PNJ) (@joueur)`

- Les arguments entre parentheses sont optionnels, et peuvent être utilisé indépendemment
- Seuls les modérateurs peuvent créer des personnages pour d'autres joueurs. 

Exemples:
    - `-create 10 10 10 10 10 10 10 10 @Joueur` : Permet de mettre des stats à un autre joueur que soit-même
    - `-create 10 10 10 10 10 10 10 10 Nom du perso`: Permet de mettre des stats à un PNJ/DC qui nous appartient
    - `-create 10 10 10 10 10 10 10 10 Nom du perso @Joueur`: Met des stats à un PNJ/DC d'un autre joueur

Cette commande est nécessaire pour utiliser les autres commandes de ce bot.

Au besoin, vous pouvez afficher l'aide de la commande avec `-create --help`

> **Note** Pour modifier les stats d'un personnage, il suffit de relancer la commande avec les nouvelles stats.

# Afficher les stats d'un personnage
🗒️ -> [Fichier](./show_chara.yag)

> **Note** Par défaut le trigger utilisé est `-get`

<u>Syntaxe :</u> `-get (nom du personnage) (@joueur)`
Les arguments entre parentheses sont optionnels, et peuvent être utilisé indépendemment

Exemples:
    - `-get` : Affiche les stats du personnage principal du joueur qui lance la commande
    - `-get @Joueur` : Permet d'afficher les stats d'un autre joueur que soit-même
    - `-get Nom du perso`: Permet d'afficher les stats d'un PNJ/DC qui nous appartient
    - `-get Nom du perso @Joueur`: Affiche les stats d'un PNJ/DC d'un autre joueur  

Au besoin, vous pouvez afficher l'aide de la commande avec `-get --help`

# Supprimer un personnage
🗒️ -> [Fichier](./del_chara.yag)

> **Note** Par défaut le trigger utilisé est `-del`

<u>Syntaxe :</u> `-del (nom du personnage) (@joueur)`
- Seuls les modérateurs peuvent supprimer les statistiques d'un autre joueur ;
- Les autres peuvent uniquement supprimer leur propre statistique ou celui de leur PNJ/DC.

> **warning** Il ne faut pas oublier de supprimer les statistiques des personnages supprimés ou des joueurs qui quittent !

## Pour supprimer automatiquement les statistiques d'un joueur qui quitte le serveur



Cette commande est à placer dans la partie : Notification & Feeds -> General -> User Leave Message