from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy data - replace with database integration
users = {
    'ravali@gmail.com': {'password': '12345'}
}
properties = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email not in users:
            users[email] = {'password': password}
            return redirect(url_for('login'))
        else:
            return render_template('register.html', error='User already exists. Please try with a different email.')
    
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        if email in users and users[email]['password'] == password:
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error='Invalid credentials. Please try again.')
    
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # Dummy property listing - replace with database retrieval
    return render_template('dashboard.html', properties=properties)


@app.route('/list_property', methods=['GET', 'POST'])
def list_property():
    if request.method == 'POST':
        # Dummy property creation - replace with database storage
        property_data = {
            'location': request.form['location'],
            'area': request.form['area'],
            'bedrooms': request.form['bedrooms'],
            'bathrooms': request.form['bathrooms'],
            'amenities': request.form.getlist('amenities')
        }
        properties.append(property_data)
        return redirect(url_for('dashboard'))
    
    return render_template('list_property.html')


if __name__ == '__main__':
    app.run(debug=True)
