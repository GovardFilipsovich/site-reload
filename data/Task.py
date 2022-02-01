import json

class Task:
	_counter = 0
	def __init__(self, dict_ = None):
		if (dict_ is None):
			self.type = 1
			self.info = None
			self.decide = None
		else:
			self.type = dict_["type"]
			self.info = dict_["info"]
			self.decide = dict_["decide"]


	def asdict(self):
		return {"type": self.type, "info": self.info, "decide": self.decide}