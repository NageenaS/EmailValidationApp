from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

# API key and URL for email validation
api_key = '' #use your API key generated from RapidApi website
url = 'https://emailvalidation.abstractapi.com/v1/'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/validator', methods=['GET', 'POST'])
def validator():
    if request.method == 'POST':
        email = request.form['email']
        params = {
            'api_key': api_key,
            'email': email
        }

        # Send GET request to AbstractAPI for email validation
        response = requests.get(url, params=params)
       
        if response.status_code == 200:
            data = response.json()
           
            # Extract the relevant parameters
            email_info = {
                'email': email,
                'auto_correct': data.get("auto_correct", ""),
                'deliverability': data.get("deliverability", "UNKNOWN"),
                'quality_score': data.get("quality_score", "N/A"),
                'is_valid_format': data.get("is_valid_format", {}).get("value", "Unknown"),
                'is_free_email': data.get("is_free_email", {}).get("value", "Unknown"),
                'is_disposable_email': data.get("is_disposable_email", {}).get("value", "Unknown"),
                'is_role_email': data.get("is_role_based_email", {}).get("value", "Unknown"),
                'is_catchall_email': data.get("is_catchall_email", {}).get("value", "Unknown")
            }
           
            return render_template('index.html', email_info=email_info)
        else:
            return render_template('index.html', error=f"Error: {response.status_code}")
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
