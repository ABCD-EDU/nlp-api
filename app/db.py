from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# engine = create_engine("your_database_connection_string")
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()


# class AnalysisResult(Base):
#     __tablename__ = "analysis_results"
#     id = Column(Integer, primary_key=True, index=True)
#     model = Column(String)
#     result = Column(String)


# def store_results(model_name, result):
#     db = SessionLocal()
#     db_result = AnalysisResult(model=model_name, result=result)
#     db.add(db_result)
#     db.commit()
#     db.refresh(db_result)
#     db.close()

def store_results():
    pass

def fetch_metrics():
    db = SessionLocal()

