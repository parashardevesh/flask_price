from flask import Flask, url_for, redirect, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

#this route gets triggered if the price is expensive
@app.route('/expensive/<int:price>')
def expensive(price):
    result = "Expensive!!"
    return render_template('expensive.html', res = result, price = price) 

#this route gets triggered if the price is cheap
@app.route('/cheap/<int:price>')
def cheap(price):
    result1 = "Cheap:)"
    return render_template('cheap.html', res1 = result1, price = price)

# @app.route('/value/<int:prices>')
# def value(prices):
#     values = ""
#     if prices < 10000:
#         values = "cheap"
#     else:
#         values = "expensive"
#     return redirect(url_for(values, price = prices))

#total price checker page
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_price = 0
    if request.method == 'POST':
        price=float(request.form['price'])
        quantity = float(request.form['quantity'])
        total_price = price*quantity
    res2 = ""
    if total_price<=10000:
        res2 = "cheap"
    else:
        res2 = "expensive"
    return redirect(url_for(res2, price=total_price))

if __name__ == '__main__':
    app.run(debug=True)