from flask import Flask, request, render_template
import openai

app = Flask(__name__)

@app.route('/scsai', methods=['POST'])
def scs_ai():
    user_input = request.form['user_input']

    response = openai.Completion.create(
        engine='scs-faq-domains-2023-04-13-09-28-43',
        prompt=user_input,
        temperature=0,
        max_tokens=1000,
        n=1,
        stop=[" ###"]
    )

    ai_output = response.choices[0].text.strip()

    return render_template('ai_template.html', output=ai_output)

if __name__ == '__main__':
    app.run()