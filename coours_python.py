#!/usr/bin/cours.py

x=1
y=1
z=1
def f():
  def g():
    z=3
    print(x,y,z)

  y=2
  print(x,y,z)

  g()

print(x,y,z)
f()
print(x,y,z)

#Comment fzire un module


#on crée un ficher mon_module.py et on ecrit

import mon_module
print(mon_module.mafonction)
# ceci va mpermettre d'eviter les colisions 
#duas aux noms similaires d'un code ecrit 
#par quelqu'un d'autre

#on peut ecrire aussi

from mon_module import ma_fonction