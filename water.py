from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('proj_2(home).html')

@app.route('/proj_2(products)')
def products():
    return render_template('proj_2(products).html')

@app.route('/proj_2(order)')
def order():
    return render_template('proj_2(order).html')

@app.route('/proj_2(delivery)')
def delivery():
    return render_template('proj_2(delivery).html')

@app.route('/proj_2(about)')
def about():
    return render_template('proj_2(about).html')

@app.route('/proj_2(contact)')
def contact():
    return render_template('proj_2(contact).html')

@app.route('/proj_2(emergency)')
def emergency():
    return render_template('proj_2(emergency).html')

@app.route('/proj_2(reviews)')
def reviews():
    return render_template('proj_2(reviews).html')

@app.route('/proj_2(bulkorder)')
def bulkorder():
    return render_template('proj_2(bulkorder).html')

@app.route('/proj_2(thankyoubulk)')
def thankyoubulk():
    return render_template('proj_2(thankyoubulk).html')

if __name__ == '__main__':
    app.run(debug=True)