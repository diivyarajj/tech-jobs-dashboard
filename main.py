from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Browser Security Block Hatane Ke Liye (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "API Active"}


# Cleaned data.csv se top jobs load karega
@app.get("/api/jobs")
def get_jobs():
    df = pd.read_csv("data.csv")
    return df.to_dict(orient="records")


# Dashboard ke charts ke liye stats calculation
@app.get("/api/stats")
def get_stats():
    df = pd.read_csv("data.csv")
    title_counts = df["JobTitle"].value_counts().to_dict()
    location_counts = df["Location"].value_counts().head(5).to_dict()

    return {"jobs_by_title": title_counts, "top_locations": location_counts}