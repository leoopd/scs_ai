from flask import Flask, request, render_template
import openai

app = Flask(__name__)

# Will display the configured webpage
@app.route('/scsai')
def page():
    return render_template('webapp/templates/ai_template.html')

# Will process the webapp with the model and settings specified.
@app.route('/scsai_processing', methods=['POST'])
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

    return render_template('webapp/templates/ai_template.html', output=ai_output)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8001, debug=False)