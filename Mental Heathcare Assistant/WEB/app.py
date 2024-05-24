from twilio.rest import Client
TWILIO_ACCOUNT_SID = 'ACc9dd9b4c7f228a3ecd388f16*********'
TWILIO_AUTH_TOKEN = '31f9233df1d23b9f6d68f**********'
TWILIO_PHONE_NUMBER = '+1254*******'
YOUR_PHONE_NUMBER = '+9160064*****'
from flask import Flask, render_template,request


app = Flask(__name__)
@app.route('/')
def questionnaire():
    return render_template('questionnaire.html')
@app.route('/submit', methods=['POST'])
def submit():
    # Process the form data and calculate the total_score
    total_score=0
    form_data=request.form
    for question_number in range(1, 10):
        question_key = f'q{question_number}'
        if question_key in form_data:
            score = int(form_data[question_key])
            total_score += score
    
    #Check if total_score is 20 or higher
    if total_score >= 20:
        send_sms(total_score)
    
    return render_template('submit.html', total_score=total_score)
@app.route('/result')
def result():
    score = request.args.get('score')
    return render_template('result.html', score=score)
def send_sms(score):
    TWILIO_ACCOUNT_SID = 'ACc9dd9b4c7f228a3**********'
    TWILIO_AUTH_TOKEN = '31f9233df1d23b9f6************'
    TWILIO_PHONE_NUMBER = '+1254*******'
    YOUR_PHONE_NUMBER = '+916006*******'
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = f"High PHQ score alert! Total score: {score}"
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=YOUR_PHONE_NUMBER
    )
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
