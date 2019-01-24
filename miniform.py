from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from wtforms.validators import DataRequired
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
 
class MyForm(FlaskForm):
   name = TextField('Name:', validators=[validators.DataRequired()])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
   form = MyForm()
   if form.validate_on_submit():
      flash("test")
#   print(form.errors)
#   if request.method == 'POST':
#      name=request.form['name']
#      print(name)
 
#   if form.validate():
#   # Save the comment here.
#      flash('Hello ' + name)
#   else:
#      flash('All the form fields are required. ')
 
   return render_template('hello.html', form=form)
 
if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)

