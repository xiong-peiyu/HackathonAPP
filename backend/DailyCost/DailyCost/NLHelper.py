# all the import
import json
import os
import io
import setting
import requests
import base64
# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
client = language.LanguageServiceClient()

class NLHelper():
	def __init__(self):
		self.this = 1

	# return dictionary result
	def getText(receiptImage):
		#content = setting.OCR_REQ_DATA
		#content["requests"][0]["image"].update({"content":receiptImage})
		#response = requests.post(url = setting.OCR_URL, data = json.dumps(content))
		image = types.Image(content = base64.decodebytes(receiptImage.encode('utf-8')))
		response = client.document_text_detection(image=image)
		document = response.full_text_annotation
		print("document")
		print(document)

		for page in document.pages:
			for block in page.blocks:
				block_words = []
				for paragraph in block.paragraphs:
					block_words.extend(paragraph.words)

				block_symbols = []
				for word in block_words:
					block_symbols.extend(word.symbols)
					print(word.symbols)

				block_text = ''
				for symbol in block_symbols:
					block_text = block_text + symbol.text

			
		return document.text

	def write2DB(self):
		# write to DB function
		result_dict = None;
		try:
			conn = self.DB.connect()
			cursor = conn.cursor()
			cursor.callproc('spAddItem', (self.userID, self.title, self.category, self.description, "Null"))
			result = cursor.fetchall()
			self.itemID = result[0][0]
			conn.commit()
			result_dict =  {"result":"true"}
			result_dict.update({"itemID":self.itemID})

		except Exception as e:
			print("ERROR: Item: write2DB():"+str(e))
			result_dict = {"result":"false"}

		return result_dict

	def updateItem(self):
		result_dict = None
		self.userID = self.itemInfo['userID']
		self.title = self.itemInfo['itemName']
		self.description = self.itemInfo['itemDescription']
		self.picture = self.itemInfo['picture']
		self.category = self.itemInfo['itemCategory']
		result_dict = self.write2DB()
		if(self.itemID):
			save = self.saveImage()
			if not save:
				result_dict.update({"result":"false"})
		return result_dict

	def deleteItem(self):
		result_dict = {"result":"false"}
		if("itemID" in self.itemInfo):
			try:
				conn = self.DB.connect()
				cursor = conn.cursor()
				cursor.callproc('spDeleteItem', (self.itemInfo["itemID"],))
				result = cursor.fetchall()
				conn.commit()
				if len(result):
					raise Exception(result)
				deleteImage(self.itemInfo["itemID"])	
				result_dict =  {"result":"true"}

			except Exception as e:
				print("ERROR: Item: deleteItem():"+str(e))
			
		return result_dict

	def saveImage(self):
		filePath = os.path.join(PIC_DIRECTORY,"image/"+self.itemID+".txt")
		result = True
		try:
			imageFile =open(filePath,"w")
			imageFile.write(self.picture)
			imageFile.close()
		except Exception as e:
			print("ERROR: Item: saveImage():"+str(e))
			result = False

		return result
