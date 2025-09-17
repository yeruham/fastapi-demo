from fastapi import FastAPI
from fastapi.responses import Response
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import time

cars = [
    {"model": "Hongqi HS5", "color": "black", "number": 37989403, "type": "commercial",
     "original_details": {"color": ["כחול"], "model": ["WEY COFFEE 01"]}, "score": 72,
     "is_off_road": "False", "Description": "commercial black Hongqi HS5"},

    {"model": "Toyota Corolla", "color": "white", "number": 48219374, "type": "private",
     "original_details": {"color": ["אדום"], "model": ["Mazda 3"]}, "score": 15,
     "is_off_road": "False", "Description": "private white Toyota Corolla"},

    {"model": "Kia Sportage", "color": "silver", "number": 83920147, "type": "jeep",
     "original_details": {"color": ["שחור"], "model": ["Hyundai Tucson"]}, "score": 61,
     "is_off_road": "True", "Description": "jeep silver Kia Sportage"},

    {"model": "BMW X5", "color": "blue", "number": 10923874, "type": "luxury",
     "original_details": {"color": ["לבן"], "model": ["Mercedes GLE"]}, "score": 94,
     "is_off_road": "False", "Description": "luxury blue BMW X5"},

    {"model": "Skoda Octavia", "color": "green", "number": 65738291, "type": "taxi",
     "original_details": {"color": ["כסוף"], "model": ["Toyota Prius"]}, "score": 33,
     "is_off_road": "False", "Description": "taxi green Skoda Octavia"},

    {"model": "Hyundai i20", "color": "red", "number": 48392011, "type": "private",
     "original_details": {"color": ["כחול"], "model": ["Honda Civic"]}, "score": 28,
     "is_off_road": "False", "Description": "private red Hyundai i20"},

    {"model": "Mazda CX-5", "color": "gray", "number": 93847201, "type": "jeep",
     "original_details": {"color": ["צהוב"], "model": ["Nissan Qashqai"]}, "score": 87,
     "is_off_road": "True", "Description": "jeep gray Mazda CX-5"},

    {"model": "Mercedes C200", "color": "black", "number": 12938475, "type": "luxury",
     "original_details": {"color": ["ירוק"], "model": ["Audi A4"]}, "score": 76,
     "is_off_road": "False", "Description": "luxury black Mercedes C200"},

    {"model": "Honda Accord", "color": "white", "number": 56473829, "type": "private",
     "original_details": {"color": ["שחור"], "model": ["Toyota Camry"]}, "score": 55,
     "is_off_road": "False", "Description": "private white Honda Accord"},

    {"model": "Jeep Cherokee", "color": "brown", "number": 83746291, "type": "jeep",
     "original_details": {"color": ["כסוף"], "model": ["Ford Edge"]}, "score": 20,
     "is_off_road": "True", "Description": "jeep brown Jeep Cherokee"},

    {"model": "Audi Q7", "color": "gray", "number": 92837465, "type": "luxury",
     "original_details": {"color": ["כחול"], "model": ["BMW X7"]}, "score": 99,
     "is_off_road": "False", "Description": "luxury gray Audi Q7"},

    {"model": "Volkswagen Golf", "color": "blue", "number": 39485720, "type": "private",
     "original_details": {"color": ["אדום"], "model": ["Seat Leon"]}, "score": 44,
     "is_off_road": "False", "Description": "private blue Volkswagen Golf"},

    {"model": "Peugeot 3008", "color": "silver", "number": 83920193, "type": "jeep",
     "original_details": {"color": ["לבן"], "model": ["Citroen C5"]}, "score": 70,
     "is_off_road": "True", "Description": "jeep silver Peugeot 3008"},

    {"model": "Ford Focus", "color": "black", "number": 83910284, "type": "private",
     "original_details": {"color": ["צהוב"], "model": ["Opel Astra"]}, "score": 11,
     "is_off_road": "False", "Description": "private black Ford Focus"},

    {"model": "Chevrolet Malibu", "color": "white", "number": 12039487, "type": "private",
     "original_details": {"color": ["שחור"], "model": ["Chrysler 200"]}, "score": 64,
     "is_off_road": "False", "Description": "private white Chevrolet Malibu"},

    {"model": "Nissan Altima", "color": "gray", "number": 38475620, "type": "private",
     "original_details": {"color": ["אדום"], "model": ["Honda Accord"]}, "score": 31,
     "is_off_road": "False", "Description": "private gray Nissan Altima"},

    {"model": "Subaru Forester", "color": "green", "number": 57483920, "type": "jeep",
     "original_details": {"color": ["כסוף"], "model": ["Toyota RAV4"]}, "score": 52,
     "is_off_road": "True", "Description": "jeep green Subaru Forester"},

    {"model": "Mitsubishi Outlander", "color": "red", "number": 93847561, "type": "jeep",
     "original_details": {"color": ["לבן"], "model": ["Kia Sorento"]}, "score": 81,
     "is_off_road": "True", "Description": "jeep red Mitsubishi Outlander"},

    {"model": "Jaguar XF", "color": "black", "number": 12938476, "type": "luxury",
     "original_details": {"color": ["כחול"], "model": ["Lexus ES"]}, "score": 66,
     "is_off_road": "False", "Description": "luxury black Jaguar XF"},

    {"model": "Volvo XC60", "color": "white", "number": 39485721, "type": "luxury",
     "original_details": {"color": ["אדום"], "model": ["BMW X3"]}, "score": 39,
     "is_off_road": "False", "Description": "luxury white Volvo XC60"},

    {"model": "Tesla Model 3", "color": "silver", "number": 83920194, "type": "private",
     "original_details": {"color": ["שחור"], "model": ["Polestar 2"]}, "score": 100,
     "is_off_road": "False", "Description": "private silver Tesla Model 3"},

    {"model": "Renault Clio", "color": "blue", "number": 12039488, "type": "private",
     "original_details": {"color": ["צהוב"], "model": ["Peugeot 208"]}, "score": 25,
     "is_off_road": "False", "Description": "private blue Renault Clio"},

    {"model": "Seat Ibiza", "color": "red", "number": 38475621, "type": "private",
     "original_details": {"color": ["לבן"], "model": ["Skoda Fabia"]}, "score": 58,
     "is_off_road": "False", "Description": "private red Seat Ibiza"},

    {"model": "Suzuki Vitara", "color": "green", "number": 57483921, "type": "jeep",
     "original_details": {"color": ["כסוף"], "model": ["Hyundai Kona"]}, "score": 42,
     "is_off_road": "True", "Description": "jeep green Suzuki Vitara"},

    {"model": "Opel Mokka", "color": "gray", "number": 93847562, "type": "jeep",
     "original_details": {"color": ["כחול"], "model": ["Nissan Juke"]}, "score": 7,
     "is_off_road": "True", "Description": "jeep gray Opel Mokka"},

    {"model": "Fiat Tipo", "color": "white", "number": 12938477, "type": "private",
     "original_details": {"color": ["אדום"], "model": ["Ford Fiesta"]}, "score": 48,
     "is_off_road": "False", "Description": "private white Fiat Tipo"},

    {"model": "Lexus RX", "color": "black", "number": 39485722, "type": "luxury",
     "original_details": {"color": ["שחור"], "model": ["Acura MDX"]}, "score": 74,
     "is_off_road": "False", "Description": "luxury black Lexus RX"},

    {"model": "Cadillac XT5", "color": "blue", "number": 83920195, "type": "luxury",
     "original_details": {"color": ["לבן"], "model": ["Lincoln Corsair"]}, "score": 83,
     "is_off_road": "False", "Description": "luxury blue Cadillac XT5"},

    {"model": "Infiniti Q50", "color": "red", "number": 12039489, "type": "luxury",
     "original_details": {"color": ["צהוב"], "model": ["Genesis G70"]}, "score": 9,
     "is_off_road": "False", "Description": "luxury red Infiniti Q50"},

    {"model": "Porsche Cayenne", "color": "gray", "number": 38475622, "type": "luxury",
     "original_details": {"color": ["ירוק"], "model": ["Maserati Levante"]}, "score": 62,
     "is_off_road": "False", "Description": "luxury gray Porsche Cayenne"}
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        app.state.current_message = consume_generator(cars)
    except Exception as e:
        pass
    yield


def consume_generator(lst):
        for n in lst:
            time.sleep(0.2)
            yield n


app = FastAPI(lifespan=lifespan)
# app.state.current_message = None


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def get_results():
    try:
        current_message = next(app.state.current_message)
        print(current_message)
        return current_message
    except:
        return {"app can't works nwo"}



@app.get('/file/{num}')
def get_file(num):
    path = "../Pictures/1NL.jpg"
    with open(path, "rb") as f:
        file_data = f.read()
    return Response(content=file_data, media_type="image/jpeg")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8081)
