from google.cloud import language
from google.cloud.language import enums

from google.cloud import vision


# Instantiates a client
clientOCR = vision.ImageAnnotatorClient()

# Instantiates a client
clientNL = language.LanguageServiceClient()

entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION','EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')

with open(r"C:/Users/yuant/Desktop/Print_Payment_Receipt.JPG", "rb") as f:
		image = f.read()

image = vision.types.Image(content = image)
response = clientOCR.document_text_detection(image=image)
document = response.full_text_annotation
text = document.text
tokens = text.split("\n")

location = ''
for token in tokens:
	doc = language.types.Document(content=token,type=language.enums.Document.Type.PLAIN_TEXT,)
	try:
		response = clientNL.analyze_entities(document=doc,encoding_type="UTF32")
		print('token:'+token)
		for entity in response.entities:
			print('='*20)
			print('       name: {0}'.format(entity.name))
			print('       type: {0}'.format(entity_type[entity.type]))

			if (entity_type[entity.type] == 'LOCATION'):
				location = location + " " + token
	except Exception as e:
		print(e)

print('location:'+location)