male(shantilal).
male(govind).
male(arun).
male(arvind).
male(sharad).
male(soham).
male(aditya).

female(kusum).
female(ganga).
female(sushma).
female(urmila).
female(sakshi).
female(sonal).

father(shantilal,arun).
father(shantilal,arvind).
father(shantilal,sushma).
father(govind,urmila).
father(govind,sharad).
father(arun,aditya).
father(arvind,sonal).
father(sharad,soham).

mother(kusum,arun).
mother(kusum,sushma).
mother(kusum,arvind).
mother(ganga,urmila).
mother(ganga,sharad).
mother(urmila,sonal).
mother(sushma,sakshi).

parent(X,Y):- father(X,Y);mother(X,Y).
sibling(X,Y):- parent(Z,X),parent(Z,Y),X\=Y.
brother(X,Y):- sibling(X,Y),male(Y).
sister(X,Y):- sibling(X,Y),female(Y).
cousin(X,Y):- parent(Z,X),parent(W,Y),sibling(Z,W).
uncle(X,Y):- parent(Z,Y),brother(X,Z).
aunt(X,Y):- parent(Z,Y),sister(X,Z).
grandfather(X,Y):- father(X,Z),parent(Z,Y).
grandmother(X,Y):- mother(X,Z),parent(Z,Y).