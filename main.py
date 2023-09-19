from flask import Flask, request, jsonify

app = Flask(__name__)


def extract_data_and_find_highest(input_data):
    # Extract numbers and alphabets
    numbers = [item for item in input_data if isinstance(item, int)]
    alphabets = [
        item for item in input_data if isinstance(item, str) and len(item) == 1
    ]

    # Find the highest alphabet based on the criteria (last in A-Z series, case-insensitive)
    highest_alphabet = max(alphabets, key=lambda x: x.lower(), default=None)

    return numbers, alphabets, highest_alphabet


@app.route("/bfhl", methods=["POST"])
def post_endpoint():
    try:
        # Extract data from the request
        data = request.json

        # Extract numbers, alphabets, and find the highest alphabet
        numbers, alphabets, highest_alphabet = extract_data_and_find_highest(data)

        # Construct the response
        response = {
            "is_success": True,
            "user_id": "Mansi_Sahu_13122001",  # Placeholder, replace with actual value
            "college_email_id": "mansi.sahu2020@vitbhopal.ac.in",  # Placeholder
            "college_roll_number": "20BAI10158",  # Placeholder
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet,
        }
        return jsonify(response)

    except Exception as e:
        # Handle errors
        return jsonify({"is_success": False, "error": str(e)})


@app.route("/bfhl", methods=["GET"])
def get_endpoint():
    # Hardcoded response for GET
    return jsonify({"status": True})


if __name__ == "__main__":
    app.run()
