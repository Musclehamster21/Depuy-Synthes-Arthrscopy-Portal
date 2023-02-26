import json
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/create_profile', methods=['POST'])
def create_profile():
    username = request.form['username']
    profile_picture = request.form['profile_picture']
    social_media_link_1 = request.form['social_media_link_1']
    social_media_link_2 = request.form['social_media_link_2']
    social_media_link_3 = request.form['social_media_link_3']
    # Save the user profile data to a database or file
    return redirect('/profile')

@app.route('/profile')
def profile():
    # Retrieve user profile data from a database or file
    username = 'Alice'
    profile_picture = 'alice.jpg'
    social_media_link_1 = 'https://twitter.com/alice'
    social_media_link_2 = 'https://facebook.com/alice'
    social_media_link_3 = 'https://instagram.com/alice'
    return render_template('profile.html',
                           username=username,
                           profile_picture=profile_picture,
                           social_media_link_1=social_media_link_1,
                           social_media_link_2=social_media_link_2,
                           social_media_link_3=social_media_link_3)

@app.route('/evaluation', methods=['GET', 'POST'])
def evaluation():
    with open('products_list.json') as f:
        products = json.load(f)

    if request.method == 'POST':
        product_name = request.form['product-name']
        quantity = request.form['quantity']
        name = request.form['name']
        email = request.form['email']
        territory_name = request.form['territory-name']
        phone_number = request.form['phone-number']
        territory_number = request.form['territory-number']
        regional_manager = request.form['regional-manager']
        regional_manager_email = request.form['regional-manager-email']
        regional_manager_phone = request.form['regional-manager-phone']
        account_name = request.form['account-name']
        ucn_number = request.form['ucn-number']
        hcp_evaluating = request.form['hcp-evaluating']
        address = request.form['address']
        city = request.form['city']
        state = request.form['state']
        zip_code = request.form['zip']
        shipping_method = request.form['shipping-method']
        delivery_date = request.form['delivery-date']
        attention_line = request.form['attention-line']
        customer_contact_name = request.form['customer-contact-name']
        customer_contact_email = request.form['customer-contact-email']
        customer_contact_phone = request.form['customer-contact-phone']

        # Save the evaluation to a database or file
        return redirect('/evaluation_confirmation')
    return render_template('evaluation.html', products=products)

@app.route('/evaluation_confirmation')
def evaluation_confirmation():
    return render_template('evaluation_confirmation.html')
