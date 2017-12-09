from InstagramAPI import InstagramAPI
from clarifai.rest import ClarifaiApp
import json
import urllib
from pymongo import MongoClient
from PIL import Image
from pytesseract import image_to_string


#conect to database
client = MongoClient()
db = client.test

user,pwd = '', ''

InstagramAPI = InstagramAPI(user,pwd)
InstagramAPI.login()

#get about 85 most recent posts about the searched hashtags
InstagramAPI.tagFeed("memes")

media_id = InstagramAPI.LastJson #last response JSON
allCatList = media_id["items"]

app = ClarifaiApp(api_key='')
model1 = app.models.get("general-v1.3")

inum=1
for i in allCatList:
	if "image_versions2" in i:
		imgsrc = i["image_versions2"]["candidates"][0]["url"]
		genPred = model1.predict_by_url(url=imgsrc)
		print imgsrc
		saveDir = "final/" + str(inum) + ".jpg"
		#urllib.urlretrieve(imgsrc, saveDir)
		#db.precogD.insert(i)
		#db.precogDPred.insert(genPred)
		allText = image_to_string(Image.open(saveDir))
		#db.precogDText.insert({"text" : allText})

	inum+=1



