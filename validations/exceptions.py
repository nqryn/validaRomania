from .constants import CNP_EXCEPTIONS

class CnpError(Exception):

	def __init__(self, message, detail, code):
		super().__init__(code, message=None, detail=None)
		self.code = code
		self.message = message or CNP_EXCEPTIONS[self.code][0]
		self.detail = detail or CNP_EXCEPTIONS[self.code][1]
		

class CnpWarning(Warning):

	def __init__(self, message, detail, code):
		super().__init__(code, message=None, detail=None)
		self.code = code
		self.message = message or CNP_EXCEPTIONS[self.code][0]
		self.detail = detail or CNP_EXCEPTIONS[self.code][1]