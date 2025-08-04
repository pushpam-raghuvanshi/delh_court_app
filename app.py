from flask import Flask, render_template, request, send_file
from scraper import fetch_case_data
from generate_pdf import generate_case_pdf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    case_type = request.form["case_type"]
    case_number = request.form["case_number"]
    year = request.form["year"]

    case_data = fetch_case_data(case_type, case_number, year)

    if case_data:
        return render_template("result.html", case_data=case_data)
    else:
        return render_template("result.html", case_data=None)

@app.route("/download-pdf", methods=["POST"])
def download_pdf():
    case_data = request.form.to_dict()
    pdf_file = generate_case_pdf(case_data)
    return send_file(pdf_file, download_name="case_summary.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
