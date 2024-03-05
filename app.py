from flask import Flask, render_template, request, flash, redirect, url_for
from dotenv import load_dotenv
from pymongo import MongoClient
from bson import ObjectId
import os

load_dotenv()

app = Flask(__name__)
app.secret_key = 'ghfghffghgfh'  # Replace with a secure secret key

mongo_uri = os.getenv('PRIMARY_KEY')  # Replace with your Cosmos DB connection string
mongo_client = MongoClient(mongo_uri)

cosmos_db_database_name = 'countries_db'
cosmos_db_database = mongo_client[cosmos_db_database_name]
db = cosmos_db_database['countries']

@app.route('/')
def index():
    # Retrieve all countries from the database
    countries = list(db.find())
    return render_template('index.html', countries=countries)

@app.route('/create', methods=['GET', 'POST'])
def create():
    try:
        if request.method == 'POST':
            new_data = {
                "_id": str(request.form.get("_id")),
                "name": request.form.get("name"),
                "capital": request.form.get("capital"),
                "population": int(request.form.get("population")),
                "continent": request.form.get("continent"),
                "gnp": float(request.form.get("gnp")),
                "governmentForm": request.form.get("governmentForm"),
                "headOfState": request.form.get("headOfState"),
                "lifeExpectancy": float(request.form.get("lifeExpectancy")),
                "localName": request.form.get("localName"),
                "region": request.form.get("region"),
                "surfaceArea": float(request.form.get("surfaceArea")),
                # Add other fields as needed
            }
            db.insert_one(new_data)
            flash('Country created successfully', 'success')
            return redirect(url_for('index'))

    except Exception as e:
        flash(f'Error creating country: {str(e)}', 'error')

    return render_template('create.html')
@app.route('/update/<country_id>', methods=['GET', 'POST'])
def update(country_id):
    if request.method == 'POST':
        updated_fields = {
            "name": request.form.get("name"),
            "capital": request.form.get("capital"),
            "population": int(request.form.get("population")),
            "continent": request.form.get("continent"),
            "gnp": float(request.form.get("gnp")),
            "governmentForm": request.form.get("governmentForm"),
            "headOfState": request.form.get("headOfState"),
            "lifeExpectancy": float(request.form.get("lifeExpectancy")),
            "localName": request.form.get("localName"),
            "region": request.form.get("region"),
            "surfaceArea": float(request.form.get("surfaceArea")),
            # Add other fields as needed
        }

        try:
            # Use update_one to update the document with the specified _id
            db.update_one({"_id": country_id}, {"$set": updated_fields})
            flash('Country updated successfully', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            flash(f'Error updating country: {str(e)}', 'error')

    # If it's a GET request, render the update form
    country = db.find_one({"_id": country_id})
    return render_template('update.html', country=country)

    
@app.route('/delete/<country_id>', methods=['POST'])
def delete(country_id):
    try:
        db.delete_one({"_id": country_id})
        flash('Country deleted successfully', 'success')
    except Exception as e:
        flash(f'Error deleting country: {str(e)}', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
