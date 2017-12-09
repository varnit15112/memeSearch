from pymongo import MongoClient
import json
from flask import Flask,render_template
app = Flask(__name__)

client = MongoClient()


@app.route("/")
def main():
    return render_template('index.html')

@app.route("/query/<inp>")
def query(inp):
	#print (inp)

	inp = inp.split(" ")

	print (inp)

	db = client.test
	allImg = db.precogD.find()
	allPred = db.precogDPred.find()
	allText = db.precogDText.find()

	finalList=[]

	for i in range(75):

		keywords=set()

		try:
			#print i
			#print allText[1]
			prediction = allPred[i]["outputs"][0]["data"]["concepts"]
			#print prediction
			for word in prediction:
				if word["value"]>0.5:
					keywords.add(word["name"])
		except Exception as e: 
			print(e)

		written = allText[i]["text"]
		written = written.split(" ")

		for word2 in written:
			keywords.add(word2)

		#print keywords

		imgsrc = allImg[i]["image_versions2"]["candidates"][0]["url"]
		#print imgsrc

		matchCount=0

		for searchWord in inp:
			if searchWord in keywords:
				matchCount+=1

		#print matchCount

		if matchCount>0:
			finalList.append(imgsrc)


	#l1="https://scontent-sit4-1.cdninstagram.com/t51.2885-15/e35/23824981_247354545796728_2002710866071388160_n.jpg?ig_cache_key=MTY1NTI0MDk0OTcyNTY3MDUzMA%3D%3D.2"
	#l2="https://scontent-sit4-1.cdninstagram.com/t51.2885-15/e35/23823820_497674517268973_3034856125083156480_n.jpg?ig_cache_key=MTY1NTI2NzI4MTg5Mzg1MTM1MA%3D%3D.2"

	#li = [l1,l2]
	finalString=""

	for i in finalList:
		finalString+=i+","


	return render_template('result.html',value=finalString)
	#return inp

if __name__ == "__main__":
    app.run(host= '0.0.0.0',port=5010)