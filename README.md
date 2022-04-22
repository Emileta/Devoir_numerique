# PHY-1007 - Computational Homework
A small tool to visualize energy flux, electric field and magnetic field in arbitrary electrical circuits.

## Circuit obligatoires

On retrouve dans les quatres fichier python des circuits [a](examples/circuit_a.py), [b](examples/circuit_b.py) et [c](examples/circuit_c.py) dans le dossier [examples](examples).
![(a)](Images/flux_a.png)
![(b)](Images/flux_b.png)![(c)](Images/flux_c.png)

Remarquons que dans les trois circuits, le flux de l'énergie va toujours de la source de tension à la résistance. En effet ceci s'explique par le fait que l'énergie se trouve dans les champs. On voit que même lorsque la position de la source par rapport à la résistance, le comportement du flux énergétique est le même. On retrouve toute les autres figure des différentes simulation effectuées par le code dans le dossier [Images](Images).

## Circuit original

Commençons par regarder le circuit que nous avons fait dans un [simulateur](https://www.falstad.com/circuit/circuitjs.html?ctz=CQAgjCAMB0l3BWcMBMcUHYMGZIA4UA2ATmIxAUgpABZsKBTAWjDACgB3cFPEQmqmB58aUTt179aeKlMhsATtNmiaM8ISqC4i5RqoJhKAVGTyuawZpApj+sUtuiw1pzYwpTYHVzeZP2IS8-g4ggcEeYUFhhl46SuHunnSeIdryAOa02KmRNGpJppkURiaGwQiEReKJ2LFudZ7mNnaNLaIIGFXyjnadVW78WmZsAG7tIoLCQ0W06bMwCGxZifm8q3KhtbGrBenLEzODkVpsQA):


![simulation](Images/circuit_falstad.png)

Ce circuit correspond à un diviseur de tension où tois charges de 100 Ω sont placés à différents points du circuit. Chacune d'entre elle dissipe une partie de l'énergie mais aussi une partie du courant puisque elles sont toutes connectées à la mise à la terre. Regardons de plus près le flux énergétique de ce [circuit](examples/circuit_d.py):

![](Images/flux_d.png)

Nous pouvons bien voir que le flux énergétique se déplace en diagonale directement dans la direction des différentes résistance malgré le fait que les fils du circuits suivent un parcours indirect. On peut toutefois voir certaines discontinuités dans le champ du flux énergétiques qui pourraient être expliquées par la présences de mises à la terres ainsi que de plusieurs charges alignées par rapport à la source de courant. Pour vérifier cette hypothèse, nous avons placé dans le circuit [(a)](examples/circuit_a.py) deux autres résistance en série poour former le circuit [concept](examples/circuit_concept.py) et nous obtenons le flux énergétique suivant:

![](Images/flux_concept.png)

En comparant avec le flux énergétique du circuit [(a)](Images/flux_a) à celui ci-dessus, on remarque que le graphique est beaucoup moins beau; la représentation de ce dernier comporte plusieurs discontinuité tel qu'observé dans notre circuit diviseur de tension.
