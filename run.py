"""
AND RUN.
"""
__author__ = 'donal'
__project__ = 'tinyFeet'


from app import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=False)