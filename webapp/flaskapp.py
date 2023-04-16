from flask import Flask, request, render_template
import openai
import os

# Key will only need to be exposed once and can (and has to!) be deleted after that.
openai.api_key = os.environ["OPENAI_API_KEY"]

app = Flask(__name__)

# Will process the webapp with the model and settings specified.
@app.route('/', methods=['GET', 'POST'])
def scs_ai():
    if request.method == 'POST':
        user_input = 'Domains, ' + request.form['user_input'] + '\'\\n\\n###\\n\\n'
        # output = f'You entered {user_input}'

        response = openai.Completion.create(
            engine='curie:ft-personal:scs-faq-domains-2023-04-13-09-28-43',
            prompt=user_input,
            max_tokens=300,
            n=1,
            stop=[" ###"],
            frequency_penalty=1
        )

        output = response.choices[0].text.strip()

        return render_template('ai_template.html', output=output, user_input=user_input)
    else:
        return render_template('ai_template.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
