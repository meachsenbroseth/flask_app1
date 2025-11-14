from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email", "")
        password = request.form.get("password", "")

        # Dummy auth check
        if email and password:
            flash("Logged in successfully (demo).", "success")
            return redirect(url_for("main.home"))
        
        flash("Invalid credentials (demo).", "danger")

    return render_template("auth/login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Handle registration (demo)
        flash("Registered successfully (demo).", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("auth/register.html")
