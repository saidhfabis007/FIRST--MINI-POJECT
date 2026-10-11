
from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and preprocessing pipeline
model = joblib.load("food_delivery_model.pkl")

# anaconda3/condabin/python programs/MINI PROJECT-1/food_delivery_model.pkl


@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Collect input values from web form
            input_data = pd.DataFrame([{
                "Quantity": int(request.form["quantity"]),
                "Total_Price": float(request.form["total_price"]),
                "City": request.form["city"],
                "Payment_Method": request.form["payment_method"],
                "Driver_Vehicle": request.form["driver_vehicle"],
                "Delivery_Distance_km": float(
                    request.form["distance"]
                ),
                "Traffic_Level": request.form["traffic"],
                "Driver_Availability": request.form["availability"],
                "Order_Hour": int(request.form["order_hour"]),
                "Order_DayOfWeek": int(request.form["day_of_week"])
            }])

            # Predict delivery duration
            result = model.predict(input_data)

            prediction = round(max(0, float(result[0])), 2)

        except (ValueError, KeyError) as exc:
            error = f"Please check your input values: {exc}"

    return render_template(
        "index.html",
        prediction=prediction,
        error=error
    )


if __name__ == "__main__":
    app.run(debug=True)
