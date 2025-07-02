from flask import Flask, render_template, request, send_file
from score_logic import calculate_scores
from pdf_generator import generate_pdf
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answers = request.form.to_dict()
        ga_score, rs_score = calculate_scores(answers)

        # PDF erzeugen
        pdf_path = generate_pdf(ga_score, rs_score)

        return send_file(pdf_path, as_attachment=True)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
