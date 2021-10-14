from flask import Flask,render_template,request
import placement as p

app=Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/submit",methods=["POST"])
def submit():
    #HTML->.py
    if request.method=="POST":
        age=(request.form["age"])
        gender=p.gender_encoder.transform([(request.form["gender"]).lower()])
        stream=p.stream_encoder.transform([(request.form["stream"]).lower()])
        intern=(request.form["intern"])
        cgpa=(request.form["cgpa"])
        hostel=(request.form["hostel"]).lower()
        if hostel=="yes":
            hostel=1

        else:
            hostel=0

        backlog=(request.form["backlog"])

        test=[[age,gender,stream,intern,cgpa,hostel,backlog]]
        res=p.svc_classifier.predict(p.sc_x.transform(test))

        print(res)

        if res[0]==1:
            str="You have high chance to place in a company"

        elif res[0]==0:
            str="You have less chance to place in a company"

    #.py->HTML
    return render_template("submit.html",result=str)

if __name__=="__main__":
    app.run(debug=True)