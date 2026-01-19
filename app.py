from flask import Flask

app = Flask(__name__)

# --- Η Αρχική Σελίδα ---
@app.route('/')
def hello():
    return """
    <div style="text-align: center; margin-top: 50px; font-family: sans-serif;">
        <h1>🔥 AUTOMATIC DEPLOYMENT SUCCESS 🔥</h1>
        <h2>Αυτό το site τρέχει στον δικό μου Cloud Server.</h2>
        <p>Έρχεται ζωντανά από τη Γερμανία (AWS Frankfurt).</p>
        <br>
        <hr>
        <br>
        <a href="/bio" style="font-size: 20px; color: blue; text-decoration: none;">
            👉 Δες το Βιογραφικό μου (Click here) 👈
        </a>
    </div>
    """

# --- Η Σελίδα Bio (Η Άσκηση) ---
@app.route('/bio')
def bio():
    return """
    <div style="background-color: #f0f0f0; padding: 20px; font-family: sans-serif; max-width: 600px; margin: 50px auto; border-radius: 10px;">
        <h1>👨‍💻 Kostas Cloud Engineer</h1>
        <h3>My Skills:</h3>
        <ul>
            <li>Python 🐍</li>
            <li>Linux 🐧</li>
            <li>AWS Cloud ☁️</li>
            <li>Git & GitHub 🐙</li>
        </ul>
        <br>
        <p><i>Αυτή η σελίδα φτιάχτηκε με Python Code!</i></p>
        <br>
        <a href="/" style="background-color: black; color: white; padding: 10px; text-decoration: none; border-radius: 5px;">
            🔙 Πίσω στην Αρχικήηη
        </a>
    </div>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)