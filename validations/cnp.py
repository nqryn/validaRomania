# CNP -  Codul Numeric Personal constituie numărul de ordine atribuit de Evidența Populației unui individ la naștere. 

# Formatul unui CNP este `|S| |AA| |LL| |ZZ| |JJ| |ZZZ| |C|`,  unde fiecare variabilă reprezintă :

# `S` -- Sexul persoanei (masculin/feminin) :
#       1/2-cetățeni români născuți între 1 ian 1900 și 31 dec 1999 
#       3/4-cetățeni români născuți între 1 ian 1800 și 31 dec 1899 
#       5/6-cetățeni români născuți între 1 ian 2000 și 31 dec 2099 
#       7/8-rezidenți 
#       9-persoanele cu cetățenie străină 
# `AA` --  ultimele două cifre din anul nașterii (e.g. 91 pentru cineva născut în 1991) 
# `LL` --  luna nașterii (e.g. 06 pentru cineva născut în luna iunie) 
# `ZZ` --  ziua nașterii (e.g. 19 pentru cineva născut data de 19)
# `JJ` --  codul județului (e.g. 12 pentru cineva din județul Cluj); județele sunt numerotate în ordine alfabetică, cu unele excepții, și au valori între 01 (Alba) și 52 (Giurgiu) 
# `NNN` --  numărul de ordine atribuit persoanei la naștere per județ și per zi
# `C` -- cifra de control

import re
from datetime import date

from .constants import CNP_REGEX, CNP_KEY, CNP_GROUPS, CNP_COUNTY_CODE_MIN, CNP_COUNTY_CODE_MAX
from .exceptions import CnpError, CnpWarning

# mapeaza codurile pentru sexul persoanei cu primele 2 cifre ale secolului corespunzator
gender_to_century = {
	1: 19,
	2: 19,
	3: 18,
	4: 18,
	5: 20,
	6: 20,
	# pentru valorile 7/8 si 9 nu exista foarte multe explicatii, asa ca verificam orice secol
	7: 20,
	8: 20,
	9: 20
}

def validate_cnp(cnp):
	pattern = re.compile(CNP_REGEX, re.X)
	match = pattern.match(str(cnp))

	if match:
		gender, birth_year, birth_month, birth_day, county, counter, control_digit = (int(match.group(x)) for x in CNP_GROUPS)
		# Verificare data nasterii
		try:
			birth_date = date(gender_to_century[gender_to_century]*100+birth_year, birth_month, birth_day)
		except ValueError:
			raise CnpError('birth_date')

		# Verificare cod judet; daca acesta nu este intre `Alba` si `Giurgiu`, se emite doar un avertisment, deoarece este posibil sa se foloseasca alte coduri pt rezidenti
		if not CNP_COUNTY_CODE_MIN <= county <= CNP_COUNTY_CODE_MAX:
			raise CnpWarning('county')

	else:
		raise CnpError('regex')

