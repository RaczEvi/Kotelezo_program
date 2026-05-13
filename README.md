2. Magyar nyelvű Gutenberg könyvek feldolgozása

A program lekéri az internetről a magyar nyelvű könyvek adatait a Gutendex APi segítségével.
Megkeresi a könyvek címét, a szerzőket, a letöltések számát.
Ezeket elmenti egy CSV fájlba. A program végén lehet keresni is a könyvcímek között. 
A program létrehoz egy talalatok.csv nevű fájlt. Ebben vannak elmentve a lekért könyvek.


A program futtatása előtt telepíteni kell a requests modult.
pip install requests

A program futtatása:
python Kotelezo_program.py


Használt oldal: Gutendex API
https://gutendex.com/



Készítette:
Rácz Éva
