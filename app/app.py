from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai
import os
import getpass
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware


class Prompt(BaseModel):
    prompt: str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
load_dotenv()

if "GOOGLE" not in os.environ:
    os.environ["GOOGLE"] = getpass.getpass("Provide your Google API Key")

genai.configure(api_key=os.environ["GOOGLE"])

model = genai.GenerativeModel("gemini-pro")


@app.post("/generate")
async def generate(prompt: Prompt):
    response = model.generate_content(prompt.prompt)
    response.resolve()
    return {"text": response.text}
