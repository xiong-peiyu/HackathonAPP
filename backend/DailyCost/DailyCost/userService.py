# all the imports
from OCRHelper import OCRHelper

USER_ID_LENGTH = 21
class UserService():
	def __init__(self, DB):
		self.DB = DB
		self.OCRHelper = OCRHelper()

	def profilePage(self, profileData):

		return True

	def receiptPage(self, receiptData):
		receiptText = OCRHelper.getText(receiptData["image"])
		result_dict = {"text": receiptText}
		return result_dict

	



