import time
import sqlite3
from pathlib import Path

# import adafruit_dht
# import board

db_path = Path(__file__).parents[1] / "db.sqlite3"
print(db_path)


conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS climate (id INT, location VARCHAR(50),temperature VARCHAR(50),humidity VARCHAR(100), log_time VARCHAR(100));")


# def log_pi_climate():
#     """
#     Uses raspberry pi board inputs to log data from a DHT22 sensor
#     :return:
#     """
#     dht_device = adafruit_dht.DHT22(board.D4, use_pulseio=False)
#     while True:
#         try:
#             log_time = time.ctime(time.time())
#             temperature_c = dht_device.temperature
#             temperature_f = temperature_c * (9/5) + 32
#             humidity = dht_device.humidity
#             print("{:.1f} F Humidity: {}% at {}".format(temperature_f, humidity, log_time))
#             # add data to db
#         except RuntimeError as err:
#             print(err.args[0])
#
#         time.sleep(2.0)

def log_test_climate():
    """
    Generic climate values for testing off of pi
    :return:
    """
    while True:
        try:
            id = time.time()
            log_time = time.ctime(id)
            location = "garage"
            temperature_c = 28.333
            temperature_f = temperature_c * (9 / 5) + 32
            humidity = 54

            print("{} is {:.1f} F Humidity: {}% at {}".format(location, temperature_f, humidity, log_time))
            # add data to db
            # query =
            cursor.execute("INSERT INTO climate (id, temperature, humidity, log_time) values (?, ?, ?, ?)", (id, location, temperature_f, humidity, log_time))
            conn.commit()
            print("Record added to climate", cursor.rowcount)
        except RuntimeError as err:
            print(err.args[0])

        time.sleep(2.0)

log_test_climate()