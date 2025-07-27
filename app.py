from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        message = f"Hello {name}, Welcome to the Kubernetes test application!!!"
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=True)  


# To run the application, use the command: python app.py
# Access it in your browser at: http://localhost:5005/
# Find the process using port 5005 with: lsof -i :5005
# To stop the process, use: kill -9 <PID>
# Make sure to have Flask installed in your environment.
# You can install Flask using: pip install Flask   
