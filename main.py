from starlette.responses import FileResponse

from generate_pdf import generate_pdf
from fastapi import FastAPI

app = FastAPI()


@app.get("/generate_cancellation_pdf")
async def generate_cancellation(vorname, nachname, strasse, plz, stadt, rufnummer):
    return FileResponse(generate_pdf(vorname, nachname, strasse, plz, stadt, rufnummer), media_type="application/pdf")

