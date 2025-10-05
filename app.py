
from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Serve a simple HTML page with JS to get location
    return render_template_string("""
        <h2>Deals Logger</h2>
        <p id="status">Detecting personalized deals...</p>
        <script>
            navigator.geolocation.getCurrentPosition(function(pos) {
                fetch('/log-location', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        latitude: pos.coords.latitude,
                        longitude: pos.coords.longitude,
                        accuracy: pos.coords.accuracy
                    })
                }).then(() => {
                    document.getElementById('status').innerText = "Deals on the way to server!";
                });
            }, function(err) {
                document.getElementById('status').innerText = "Location access denied.";
            });
        </script>
    """)

@app.route('/log-location', methods=['POST'])
def log_location():
    data = request.get_json()
    print(f"Received location: {data}")
    return '', 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
