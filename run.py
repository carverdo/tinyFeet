"""
Simple form-filler.
"""
from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

# ==================
# OUR TWO PAGES
# ==================
@app.route('/')
def home():
    return render_template('home.html')


@app.route('/admin')
def admin():
    with open('./static/data/records.txt') as fileObj:
        rows = fileObj.readlines()
        rows = [row.strip().split('|') for row in rows]
    return render_template('admin.html', rows=list(enumerate(rows)))


# ==================
# OUR TWO AJAX PASSES
# ==================
@app.route('/_stamp', methods=['GET', 'POST'])
def _stamp():
    # just tidy data for file writing / presentation in table
    tmp = '|'.join((request.form['name'],
                    request.form['email'],
                    request.form['phone'],
                    request.form['shoe_type'],
                    request.form['rubber'],
                    request.form['rand'],
                    request.form['return'],
                    request.form['address'],
                    request.form['comments']
                    ))
    tmp = tmp.replace('\r\n', ',')
    tmp = tmp.replace('\n', ',')
    tmp += '\n'
    with open('./static/data/records.txt', 'a') as fileObj:
        fileObj.write(tmp)
    return jsonify(**request.form)


@app.route('/_clear')
def _clear():
    with open('./static/data/records.txt', 'w'): pass
    return 'cleared'


# ==================
# AND RUN!
# ==================
if __name__ == '__main__':
    app.run(debug=True)
