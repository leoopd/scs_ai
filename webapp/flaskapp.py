from flask import Flask, request, render_template
import openai
import os

# Key will only need to be exposed once and can (and has to!) be deleted after that.
# openai.api_key=''

app = Flask(__name__)

# Will process the webapp with the model and settings specified.
@app.route('/', methods=['GET', 'POST'])
def scs_ai():
    if request.method == 'POST':
        user_input = request.form['user_input']
        output = f'You entered {user_input}'

        # response = openai.Completion.create(
        #     engine='scs-faq-domains-2023-04-13-09-28-43',
        #     prompt=user_input,
        #     temperature=0,
        #     max_tokens=1000,
        #     n=1,
        #     stop=[" ###"]
        # )

        # output = response.choices[0].text.strip()

        return render_template('ai_template.html', output=output)
    else:
        return render_template('ai_template.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
