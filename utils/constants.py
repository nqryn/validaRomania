
CNP_REGEX = r"""
	(?P<gender>[1-9])
	(?P<birth_year>\d{2})
	(?P<birth_month>\d{2})
	(?P<birth_day>\d{2})
	(?P<county>\d{2})
	(?P<counter>\d{3})
	(?P<control_digit>\d{1})
"""
CNP_KEY = 279146358279