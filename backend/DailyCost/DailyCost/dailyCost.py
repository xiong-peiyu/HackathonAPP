
from flask import Flask, request, jsonify, make_response
from flaskext.mysql import MySQL
from userService import UserService

import json
import setting


mysql = MySQL()
app = Flask(__name__)
app.config.from_object(setting)

mysql.init_app(app)
userService = UserService(mysql)

# profile view
# update profile info in db
@app.route('/profile', methods=['POST'])
def profile():
	profileData = request.get_json(silent=True)
	print(profileData)
	#TODO: user service!
	result_dict = {"result":"true"}
	result_dict.update({"from":"profile"})

	return jsonify(result_dict)

# receipt view
# get receipt picture to OCR
# return receipt information
@app.route('/receipt', methods=['POST'])
def receipt():
	receipt = request.get_json(silent=True)
	result_dict = userService.receiptPage(receipt)
	result_dict.update({"from":"receipt"})

	return jsonify(result_dict)

# statement view
# return statement information
@app.route('/statement', methods=['GET'])
def statement():
	receipt = request.get_json(silent=True)
	result_dict = {"message":"statement"}
	result_dict.update({"from":"statement"})

	return jsonify(result_dict)


if __name__ == '__main__':
	app.run(host = setting.HOST,port = setting.PORT)

