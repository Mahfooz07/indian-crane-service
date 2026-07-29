from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "indian-crane-service-dev-key"  # only needed for flash messages


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/contact", methods=["POST"])
def contact():
    # In a real deployment you'd email/save this. For now we just confirm receipt.
    name = request.form.get("name", "").strip()
    phone = request.form.get("phone", "").strip()
    location = request.form.get("location", "").strip()
    message = request.form.get("message", "").strip()

    if not name or not phone:
        flash("Please share your name and phone number so we can call you back.", "error")
        return redirect(url_for("home") + "#contact")

    print(f"New enquiry -> Name: {name}, Phone: {phone}, Location: {location}, Message: {message}")
    flash("Thanks! Our dispatch team will call you back shortly.", "success")
    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
