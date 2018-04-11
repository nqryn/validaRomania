
CNP_GROUPS = [
	'gender',
	'birth_year',
	'birth_month',
	'birth_day',
	'county',
	'counter',
	'control_digit',
]
CNP_REGEX = r"""
	(?P<gender>[1-9])
	(?P<birth_year>\d{2})
	(?P<birth_month>\d{2})
	(?P<birth_day>\d{2})
	(?P<county>\d{2})
	(?P<counter>\d{3})
	(?P<control_digit>\d{1})
"""
CNP_KEY = [2, 7, 9, 1, 4, 6, 3, 5, 8, 2, 7, 9]

CNP_COUNTY_CODE_MIN = 1
CNP_COUNTY_CODE_MAX = 52

CNP_EXCEPTIONS = {
	# code: [message, detail]
	'regex': ['CNPul nu este valid.', 'CNPul nu are 13 cifre sau prima cifra nu este valida.']
	'birth_date': ['CNPul nu este valid.', 'Data nasterii nu este valida.']
	'county': ['CNPul posibil sa nu fie valid.', 'Codul judetului nu se afla printre cele oficiale, dar este posibil ca CNPul sa fie totusi valid.']
}