
## Valencia Walker's for Jewel.technology


from flask import Flask, render_template, request, jsonify
import sqlite3
from ai_routes import ai
from werkzeug.security import generate_password_hash
import re
from models import db, User  
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from jewel_tech.models import db, User
from flask import Flask, render_template


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'your-secret-key'

# Initialize DB and Login manager
db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)

# Register your blueprint
app.register_blueprint(ai)

# User loader for flask-login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()

    new_user = User(
    first_name=data['firstName'],
    last_name=data['lastName'],
    email=data['email'],
    phone=data['phone'],
    address=data['address'],
)
new_user.set_password(data['password'])
db.session.add(new_user)
db.session.commit()

@app.route('/')
def home():
    return render_template('index.html')

# Signup route, now storing user in DB, with validation and hashed password
@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    required_fields = ['firstName', 'lastName', 'email', 'phone', 'address', 'password']
    if not all(field in data for field in required_fields):
        return jsonify({"error": "Missing fields"}), 400

    # Simple email regex validation
    if not re.match(r"[^@]+@[^@]+\.[^@]+", data['email']):
        return jsonify({"error": "Invalid email"}), 400

    # Check if user already exists in DB
    existing_user = User.query.filter_by(email=data['email']).first()
    if existing_user:
        return jsonify({"error": "Email already registered"}), 400

    # Hash password
    hashed_password = generate_password_hash(data['password'])

    # Create new user
    new_user = User(
        first_name=data['firstName'],
        last_name=data['lastName'],
        email=data['email'],
        phone=data['phone'],
        address=data['address'],
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@app.route("/")
def index():
    return render_template("index.html", project_name="Jewel.Technology")

@app.route("/api/hello", methods=["GET"])
def hello():
    return jsonify({"msg": "Hello, world!"})

@app.route("/api/search", methods=["GET"])
def search():
    query = request.args.get("q", "").lower()
    conn = sqlite3.connect("jewel.db")
    cursor = conn.cursor()
    cursor.execute("""
        SELECT name, material, price, rating FROM jewelry
        WHERE LOWER(name) LIKE ? OR LOWER(material) LIKE ?
    """, (f"%{query}%", f"%{query}%"))
    results = cursor.fetchall()
    conn.close()
    jewelry = [
        {"name": row[0], "material": row[1], "price": row[2], "rating": row[3]}
        for row in results
    ]
    return jsonify(jewelry)

if __name__ == "__main__":
    app.run(debug=True)
