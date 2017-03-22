from flask import flash, render_template, redirect, request, session, url_for

from transik import app

@app.route('/')
def dashboard():
    projects = [
        {'id': 'first', 'name': 'first project'}
    ]
    return render_template('dashboard.html', session=session, projects=projects)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('dashboard'))

@app.route('/project/<id>')
def project(id):
    segments = [
        {'key': 's1', 'src': 'src1', 'target': 'targ1'},
        {'key': 's2', 'src': 'src2', 'target': 'targ2'},
    ]
    return render_template('project.html', segments=segments)

@app.route('/import/<project_id>')
@app.route('/import/<project_id>/<lang>')
def import_segments(project_id, lang=None):
    segments = [
        {'key': 's1', 'src': 'src1', 'target': 'targ1'},
        {'key': 's2', 'src': 'src2', 'target': 'targ2'},
    ]
    return render_template('project.html', segments=segments)

@app.route('/export/<project_id>')
@app.route('/export/<project_id>/<lang>')
def export_segments(project_id, lang=None):
    segments = [
        {'key': 's1', 'src': 'src1', 'target': 'targ1'},
        {'key': 's2', 'src': 'src2', 'target': 'targ2'},
    ]
    return render_template('project.html', segments=segments)
