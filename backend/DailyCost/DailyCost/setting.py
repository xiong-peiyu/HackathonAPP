# Server Setting

HOST = '128.189.242.161'
PORT = 8000
SECRET_KEY='development key'
USERNAME='admin'
PASSWORD='default'

# Database setting
MYSQL_DATABASE_USER = 'BarterAdmin'
MYSQL_DATABASE_PASSWORD = 'BarterAdmin'
MYSQL_DATABASE_DB = 'ItemListDB'
MYSQL_DATABASE_HOST = 'itemlistdb.c2bvhggvmrav.ca-central-1.rds.amazonaws.com'
MYSQL_CONNECTION_PORT = '3306'

OCR_API_KEY = 'AIzaSyB3zpuY3AWSl65AmKZemrv-sNj9csxcMHY'
OCR_URL = "https://vision.googleapis.com/v1/images:annotate?key="+OCR_API_KEY
OCR_REQ_DATA = {
				"requests":[
						{
						"image":{
							"content":"TBA"
						},
						"features":[
						{
						"type":"DOCUMENT_TEXT_DETECTION"
						}
						]
						}
					]
				}