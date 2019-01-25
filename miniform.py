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
   mac = TextField('MAC address:', validators=[validators.DataRequired()])

def multicast_mac_to_ip(mac_address):

    mac_bytes = mac_address.split(":")
    ip_mask = 0xe0000000
    ip_mask |= int(mac_bytes[3], 16) << 16
    ip_mask |= int(mac_bytes[4], 16) << 8
    ip_mask |= int(mac_bytes[5], 16)
    result = list()

    for i in range(0,31):
        temp_ip = ip_mask
        temp_ip |= i << 23
        o4 = (temp_ip & 0xff000000) >> 24
        o3 = (temp_ip & 0x00ff0000) >> 16
        o2 = (temp_ip & 0x0000ff00) >> 8
        o1 = (temp_ip & 0x000000ff)
        result.append(str(o4) + "." + str(o3) + "." + str(o2) + "." + str(o1))
    return result
 
@app.route("/", methods=['GET', 'POST'])
def hello():
   # We instantiate our form
   form = MyForm()
   print(form.errors)
   # This should return true when properly validated
   if form.validate_on_submit():
      ips = multicast_mac_to_ip(form.mac.data)
      return render_template('hello.html', form=form, ips=ips)
   # This is executed when regular GET request is issued
   return render_template('hello.html', form=form)

@app.route("/health", methods=['GET'])
def health():
   return render_template('health.html')

 
if __name__ == "__main__":
   app.run(host="0.0.0.0", debug=True)

