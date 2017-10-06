# validari-Romania
---

 Acest repo conține validări pentru diverse componente specific românești ( CNP, numere de telefon, IBAN, numere de înmatriculare auto, ș.a.m.d. )
 
  Proiectul este scris în limbajul Python și poate fi folosit atât ca librărie (integrat în alt proiect), cât și ca un proiect de sine stătător ce poate fi expus public pe un server printr-o interfață de tip REST API. 


## Cerințe preliminare
---

* Python >= 3.0

 
 Fiecare componentă este detaliată în modulul corespunzător, după cum urmează: 
 

### CNP (Cod Numeric Personal)

**CNP** -  Codul Numeric Personal constituie numărul de ordine atribuit de Evidența Populației unui individ la naștere. 

Formatul unui CNP este `|S| |AA| |LL| |ZZ| |JJ| |ZZZ| |C|`,  unde fiecare variabilă reprezintă :

 * `S` -- Sexul persoanei (masculin/feminin) :
     *   1/2-cetățeni români născuți între 1 ian 1900 și 31 dec 1999 
     *   3/4-cetățeni români născuți între 1 ian 1800 și 31 dec 1899 
     *   5/6-cetățeni români născuți între 1 ian 2000 și 31 dec 2099 
     *   7/8-rezidenți 
     *   9-persoanele cu cetățenie străină 
 * `AA` --  ultimele două cifre din anul nașterii (e.g. 91 pentru cineva născut în 1991) 
 * `LL` --  luna nașterii (e.g. 06 pentru cineva născut în luna iunie) 
 * `ZZ` --  ziua nașterii (e.g. 19 pentru cineva născut data de 19)
 * `JJ` --  codul județului (e.g. 12 pentru cineva din județul Cluj); județele sunt numerotate în ordine alfabetică, cu unele excepții, și au valori între 01 (Alba) și 52 (Giurgiu) 
 * `NNN` --  numărul de ordine atribuit persoanei la naștere per județ și per zi
 * `C` -- cifra de control
 
