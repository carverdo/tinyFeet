"""
AND RUN.
"""
__author__ = 'donal'
__project__ = 'tinyFeet'


from app import create_app
app = create_app()
app.run(debug=False)