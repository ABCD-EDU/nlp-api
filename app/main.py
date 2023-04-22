from fastapi import FastAPI

# import gensim
from gensim.models.ldamodel import LdaModel
from gensim.corpora import Dictionary

app = FastAPI()

LDA_model = None

@app.get("/")
def read_root():
    return {"Hello": hatdog}


@app.post("/load-model/{model_id}")
def load_model(model_id: str):
    try:
        LDA_model = LdaModel.load(f"../res/{model_id}/model")
    except:
        return {"status" : "failed"}
    return {"status": LDA_model.print_topics()}
    

@app.get("/inference")
def LDA_inference():
    return {}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}