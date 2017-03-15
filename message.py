import os,sys
from flask import Flask,request

app = Flask(_name_)

@app.route('/', methods=['GET'])
def verify():
	# Webhook verfication
	if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge");
      if not request.args.get("hub.verify_token") == "hello":
      	 return "Verification token mismatch",403
      return request.args["hub.challenge"],200
     return "Hello vibs",200


 if __name__=="__main":
    app.run(debug = True, port = 80)      	
		
