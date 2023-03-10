import pandas as pd
import tensorflow as tf
from tensorflow import keras
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

model = tf.keras.models.load_model('get-it-right/my_model.h5')

# Optional, good practice for dev purposes. Allow all middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# # http://127.0.0.1:8000/predict?pickup_datetime=2012-10-06 12:10:20&pickup_longitude=40.7614327&pickup_latitude=-73.9798156&dropoff_longitude=40.6513111&dropoff_latitude=-73.8803331&passenger_count=2
# @app.get("/predict")
# def predict(pickup_datetime: str,  # 2013-07-06 17:18:00
#             pickup_longitude: float,    # -73.950655
#             pickup_latitude: float,     # 40.783282
#             dropoff_longitude: float,   # -73.984365
#             dropoff_latitude: float,    # 40.769802
#             passenger_count: int):      # 1
#     """
#     Make a single course prediction.
#     Assumes `pickup_datetime` is provided as string by the user in "%Y-%m-%d %H:%M:%S" format
#     Assumes `pickup_datetime` implicitely refers to "US/Eastern" timezone (as any user in New York City would naturally write)
#     """
#     pickup_datetime_localized = pd.Timestamp(pickup_datetime, tz='US/Eastern')

#     X_pred = pd.DataFrame(dict(
#         pickup_datetime=[pickup_datetime_localized],
#         pickup_longitude=[pickup_longitude],
#         pickup_latitude=[pickup_latitude],
#         dropoff_longitude=[dropoff_longitude],
#         dropoff_latitude=[dropoff_latitude],
#         passenger_count=[passenger_count]))

#     model = app.state.model
#     assert model is not None

#     X_processed = preprocess_features(X_pred)
#     y_pred = model.predict(X_processed)

#     return dict(fare_amount=float(y_pred))


@app.get("/")
def root():
    return dict(greeting="Hello")
