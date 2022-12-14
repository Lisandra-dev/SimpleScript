# Préambule
Pour créer une nouvelle "custom commands", suivez le guide ici : https://learn.yagpdb.xyz/the-custom-command-interface  
Il suffit de copier coller chaque code dans une nouvelle custom commands, en utilisant :   
- Trigger type : Commmand (cmd/prefix)  
- Trigger : Le nom que vous souhaitez  

La commande sera alors utilisable en utilisant le préfixe défini dans le serveur, suivi du nom de la commande; par exemple, si vous avez mis `hello` en trigger, vous devrez utiliser `-hello` pour lancer la commande.    

> **Note**  
> Par défaut, le préfixe est `-`. Vous pouvez aussi nommer les commandes comme vous le souhaitez.  

# Inscrire son personnage
🗒️ -> [Fichier](./inscript_chara.yag)

> **Note**  
> Par défaut le trigger utilisé est `-create`  

Syntaxe : `-create <Force> <Endurance> <Agilité> <Constitution> <Education> <Intelligence> <Charisme> <Pouvoir> (nom du perso si DC ou PNJ) (@joueur)`  

- Les arguments entre parentheses sont optionnels, et peuvent être utilisé indépendemment  
- Seuls les modérateurs peuvent créer des personnages pour d'autres joueurs.   

Exemples:  
- `-create 10 10 10 10 10 10 10 10 @Joueur` : Permet de mettre des stats à un autre joueur que soit-même    
- `-create 10 10 10 10 10 10 10 10 Nom du perso`: Permet de mettre des stats à un PNJ/DC qui nous appartient    
- `-create 10 10 10 10 10 10 10 10 Nom du perso @Joueur`: Met des stats à un PNJ/DC d'un autre joueur   

Cette commande est nécessaire pour utiliser les autres commandes de ce bot.  

Au besoin, vous pouvez afficher l'aide de la commande avec `-create --help`  

> **Note**  
> Pour modifier les stats d'un personnage, il suffit de relancer la commande avec les nouvelles stats.  

# Afficher les stats d'un personnage
🗒️ -> [Fichier](./show_chara.yag)  

> **Note**  
> Par défaut le trigger utilisé est `-get`  

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

> **Note**  
> Par défaut le trigger utilisé est `-del`  

<u>Syntaxe :</u> `-del (nom du personnage) (@joueur)`  
- Seuls les modérateurs peuvent supprimer les statistiques d'un autre joueur ;  
- Les autres peuvent uniquement supprimer leur propre statistique ou celui de leur PNJ/DC.  
- L'option `--all` permet de supprimer tous les personnages d'un joueur. Les modérateurs peuvent supprimer pour un autre joueurs.  

> **Warning**  
> Il ne faut pas oublier de supprimer les statistiques des personnages supprimés ou des joueurs qui quittent !  

Il est aussi possible de supprimer tous les personnages associés à un jour à l'aide de l'option `--all` :  
- `-del --all` : Supprime tous les personnages du joueur qui lance la commande  
- `-del --all @Joueur` : Supprime tous les personnages d'un autre joueur que soit-même (utilisable par les modérateurs uniquement)  

## Pour supprimer automatiquement les statistiques d'un joueur qui quitte le serveur

🗒️ -> [Fichier](./automatic_delete.yag)  

Cette commande est à placer dans la partie : Notification & Feeds -> General -> User Leave Message  

Si un joueur quitte, le bot supprimera automatiquement ses statistiques et ceux de ses PNJ.  

# Roll des dés

🗒️ -> [Fichier](./roll.yag)  

Le vrai intérêt de toutes ses fonctions : pouvoir lancer des dés sans avoir à sortir de Discord et se rappeler de ses statistiques !  

Il y a **beaucoup** d'option possible, mais je vais vous montrer les plus courantes, et les plus simples ;).  

> **Note**  
> Par défaut le trigger utilisé est `-roll`  

La commande a plusieurs syntaxes mais chaque arguments peut être utilisé dans le désordre **sauf pour la statistique qui doit être en premier**.  
Cette statistique peut être une partie du mot, par exemple : `-roll fo` pour la force.  

Ainsi :   
- Pour lancer un dé simple, sur une statistique, il suffit de faire `-roll <statistique>`  
- Pour lancé un dés sur une statistique avec un commentaire : `-roll <statistique> <commentaire>` ou `-roll <statistique> #<commentaire>`  
  
Mais, il est aussi possible de changer le seuil de succès, avec le préfix `>` ou `<` devant la valeur :  
- `-roll <statistique> >10` : Lance un dé sur la statistique, et réussi si le résultat est supérieur à 10  
- `-roll <statistique> <10 #commentaire` : La même chose, mais avec un commentaire  

De même, vous pouvez ajouter des bonus et des malus, avec `-` et `+` devant la valeur :  
- `-roll <statistique> +5` : Lance un dé sur la statistique, et ajoute 5 au résultat  
- `-roll <statistique> -5 #commentaire` : Lance un dé avec un malus et un commentaire  

Enfin, dans le cas où votre dé concerne un PNJ ou un DC, il faut préciser le nom du personnage avec le caractère `&` devant le nom :   
- `-roll <statistique> &<nom du personnage>` : Lance un dé sur la statistique du personnage  
- `-roll <statistique> &<nom du personnage> #commentaire` : Lance un dé sur la statistique du personnage avec un commentaire  

Et toutes ses options sont cumulables, par exemple :`-roll <statistique> &<nom du personnage> +<bonus> ><seuil> #commentaire` : Lance un dé sur la statistique du personnage avec un commentaire et un bonus tout en changeant le seuil de succès  

On notera qu'il n'est pas possible de "combiner" l'option `+` (bonus) et `-` (malus) dans la même commande : vous devez calculer le bonus (ou malus) final.  

> **Note**  
> Au besoin, vous pouvez afficher l'aide de la commande avec `-roll --help`  



