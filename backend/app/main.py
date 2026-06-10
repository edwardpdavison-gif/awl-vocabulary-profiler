from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


from app.tokenizer import tokenize
from app.data_loader import load_awl_data, load_gsl_data
from app.analyser import analyse_text_against_awl



app = FastAPI(title="AWL Vocabulary Profiler")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

awl_lookup = load_awl_data()
gsl_lookup = load_gsl_data()


class AnalyseRequest(BaseModel):
    text: str


@app.get("/")
def root():
    return {"message": "AWL Vocabulary Profiler API is running"}


@app.get("/awl-test")
def awl_test():
    return {
        "total_awl_entries": len(awl_lookup)
    }


@app.get("/gsl-test")
def gsl_test():
    return {
        "total_gsl_entries": len(gsl_lookup)
    }


@app.post("/analyse")
def analyse_text(request: AnalyseRequest):
    return analyse_text_against_awl(
        text=request.text,
        awl_lookup=awl_lookup,
        gsl_lookup=gsl_lookup,
        tokenize=tokenize
    )