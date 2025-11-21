import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///livingwithmama.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# --- MAIN ROUTES ---

@app.route("/")
def index():
    """Homepage: The Welcome Mat"""
    return render_template("index.html")

# --- AUTHENTICATION ---

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password:
            return apology("Must provide username and password")
        if password != confirmation:
            return apology("Passwords do not match")

        hash_pw = generate_password_hash(password)

        try:
            db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hash_pw)
        except ValueError:
            return apology("Username already taken")

        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""
    session.clear()
    if request.method == "POST":
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("Invalid username/password")
        
        session["user_id"] = rows[0]["id"]
        session["username"] = rows[0]["username"] # Store name for display
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out"""
    session.clear()
    return redirect("/")

# --- MARKETPLACE ---

@app.route("/market")
@login_required
def market():
    """Display items for sale"""
    items = db.execute("SELECT * FROM market_items ORDER BY created_at DESC")
    return render_template("market.html", items=items)

@app.route("/market/sell", methods=["GET", "POST"])
@login_required
def sell():
    """List a new item"""
    if request.method == "POST":
        title = request.form.get("title")
        price = request.form.get("price")
        category = request.form.get("category")
        desc = request.form.get("description")
        contact = request.form.get("contact")

        if not title or not price or not contact:
            return apology("Missing required fields")

        db.execute("""
            INSERT INTO market_items (user_id, title, description, price, category, contact_info)
            VALUES (?, ?, ?, ?, ?, ?)
        """, session["user_id"], title, desc, price, category, contact)

        flash("Item listed successfully!")
        return redirect("/market")
    return render_template("sell.html")

# --- QUIZ ---

@app.route("/quiz", methods=["GET", "POST"])
@login_required
def quiz():
    """The Homemaker Quiz"""
    if request.method == "POST":
        score = 0
        # Simple Logic: 20 points per correct answer
        # Q1: Flip Mattress -> 6 months
        if request.form.get("q1") == "6months": score += 20
        # Q2: Baking Soda -> Cleaning
        if request.form.get("q2") == "cleaning": score += 20
        # Q3: Aloe Vera -> Burns
        if request.form.get("q3") == "burns": score += 20
        # Q4: Cast Iron -> No Soap
        if request.form.get("q4") == "nosoap": score += 20
        # Q5: Peace -> Communication
        if request.form.get("q5") == "comm": score += 20

        # Save to DB
        db.execute("INSERT INTO quiz_scores (user_id, score) VALUES (?, ?)", session["user_id"], score)
        
        # Get message based on score
        msg = "You are a Home Expert!" if score >= 80 else "Good start, keep learning!"
        
        return render_template("quiz_result.html", score=score, msg=msg)
    
    return render_template("quiz.html")

# --- INSPIRATION ---

@app.route("/inspiration")
def inspiration():
    """Static Inspiration Page"""
    return render_template("inspiration.html")