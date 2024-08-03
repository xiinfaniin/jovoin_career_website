from flask import Flask, render_template

app = Flask(__name__)

jobs = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'mogadishu, somalia',
    'salary': '$. 10,000'
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Kismayo, Somalia',
    'salary': '$. 15,000'
}, {
    'id': 3,
    'title': 'Back-End Engineer',
    'location': 'Bosaaso, Bomalia',
    'salary': '$. 5,000'
}, {
    'id': 4,
    'title': 'Fron-End Engineer',
    'location': 'Mogadishu, Somalia',
    'salary': '$. 1,000'
}]


@app.route("/")
def hello():
  return render_template(
      'home.html',
      jobs=jobs,
      company_name='Hormuud',
  )


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
