__author__ = 'donal'
__project__ = 'tinyFeet'

from flask import render_template, request
from . import proj
from .. import mc

# ==================
# OUR TWO PAGES
# ==================
@proj.route('/')
def home():
    return render_template('home.html')


@proj.route('/admin')
def admin():
    rows = mc.get('records')
    if rows: rows = [row.strip().split('|') for row in rows]
    else: rows = []
    return render_template('admin.html', rows=list(enumerate(rows)))


# ==================
# OUR TWO AJAX PASSES
# ==================
@proj.route('/_stamp', methods=['GET', 'POST'])
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
    # to ensure no confusion on storage
    tmp = tmp.replace('\r\n', ',')
    tmp = tmp.replace('\n', ',')
    tmp += '\n'
    # memcache access
    curr = mc.get('records')
    if not curr: curr = [tmp]
    else: curr.append(tmp)
    mc.set('records', curr)
    return jsonify(**request.form)


@proj.route('/_clear')
def _clear():
    mc.flush_all()
    return 'cleared'
