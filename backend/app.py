from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Body
from fastapi.responses import FileResponse

from agent import ask_gemini
from database import engine, SessionLocal
from models import Base, ChatHistory,User

from idea_agent import generate_startup_idea
from market_agent import market_research
from business_agent import business_plan
from finance_agent import finance_analysis
from marketing_agent import marketing_strategy
from mentor_agent import mentor_advice
from legal_agent import legal_guide
from report_generator import generate_report
from pdf_generator import generate_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "LaunchMate AI is running!"}


@app.get("/test")
def test():
    return {"message": "Working"}


@app.get("/ask")
def ask(question: str):
    answer = ask_gemini(question)

    db = SessionLocal()

    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.close()

    return {
        "question": question,
        "answer": answer
    }


@app.get("/idea")
def idea(topic: str):
    try:
        result = generate_startup_idea(topic)
        return {"idea": result}
    except Exception as e:
        return {"error": str(e)}


@app.get("/market")
def market(startup_idea: str):
    try:
        result = market_research(startup_idea)
        return {
            "startup_idea": startup_idea,
            "market_research": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/business")
def business(startup_idea: str):
    try:
        result = business_plan(startup_idea)
        return {
            "startup_idea": startup_idea,
            "business_plan": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/finance")
def finance(startup_idea: str):
    try:
        result = finance_analysis(startup_idea)
        return {
            "startup_idea": startup_idea,
            "finance_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/marketing")
def marketing(startup_idea: str):
    try:
        result = marketing_strategy(startup_idea)
        return {
            "startup_idea": startup_idea,
            "marketing_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/mentor")
def mentor(startup_idea: str):
    try:
        result = mentor_advice(startup_idea)
        return {
            "startup_idea": startup_idea,
            "mentor_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/legal")
def legal(startup_idea: str):
    try:
        result = legal_guide(startup_idea)

        return {
            "startup_idea": startup_idea,
            "legal_report": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
@app.get("/report")
def report(startup_idea: str):
    try:
        idea = generate_startup_idea(startup_idea)
        market = market_research(startup_idea)
        business = business_plan(startup_idea)
        finance = finance_analysis(startup_idea)
        marketing = marketing_strategy(startup_idea)
        mentor = mentor_advice(startup_idea)

        final_report = generate_report(
            idea,
            market,
            business,
            finance,
            marketing,
            mentor
        )

        return {
            "report": final_report
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.post("/download-report")
async def download_report(data: dict = Body(...)):
    try:
        report = data.get("report")

        if not report:
            return {"error": "Report content is missing"}

        pdf_file = generate_pdf(report)

        return FileResponse(
            path=pdf_file,
            filename="startup_report.pdf",
            media_type="application/pdf"
        )
    

    except Exception as e:
        return {"error": str(e)}

from fastapi.responses import FileResponse

from agent import ask_gemini
from database import engine, SessionLocal
from models import Base, ChatHistory,User

from idea_agent import generate_startup_idea
from market_agent import market_research
from business_agent import business_plan
from finance_agent import finance_analysis
from marketing_agent import marketing_strategy
from mentor_agent import mentor_advice
from legal_agent import legal_guide
from report_generator import generate_report
from pdf_generator import generate_pdf

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "LaunchMate AI is running!"}


@app.get("/test")
def test():
    return {"message": "Working"}


@app.get("/ask")
def ask(question: str):
    answer = ask_gemini(question)

    db = SessionLocal()

    chat = ChatHistory(
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.close()

    return {
        "question": question,
        "answer": answer
    }


@app.get("/idea")
def idea(topic: str):
    try:
        result = generate_startup_idea(topic)
        return {"idea": result}
    except Exception as e:
        return {"error": str(e)}


@app.get("/market")
def market(startup_idea: str):
    try:
        result = market_research(startup_idea)
        return {
            "startup_idea": startup_idea,
            "market_research": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/business")
def business(startup_idea: str):
    try:
        result = business_plan(startup_idea)
        return {
            "startup_idea": startup_idea,
            "business_plan": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/finance")
def finance(startup_idea: str):
    try:
        result = finance_analysis(startup_idea)
        return {
            "startup_idea": startup_idea,
            "finance_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/marketing")
def marketing(startup_idea: str):
    try:
        result = marketing_strategy(startup_idea)
        return {
            "startup_idea": startup_idea,
            "marketing_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }


@app.get("/mentor")
def mentor(startup_idea: str):
    try:
        result = mentor_advice(startup_idea)
        return {
            "startup_idea": startup_idea,
            "mentor_report": result
        }
    except Exception as e:
        return {
            "error": str(e)
        }

@app.get("/legal")
def legal(startup_idea: str):
    try:
        result = legal_guide(startup_idea)

        return {
            "startup_idea": startup_idea,
            "legal_report": result
        }

    except Exception as e:
        return {
            "error": str(e)
        }
    
@app.get("/report")
def report(startup_idea: str):
    try:
        idea = generate_startup_idea(startup_idea)
        market = market_research(startup_idea)
        business = business_plan(startup_idea)
        finance = finance_analysis(startup_idea)
        marketing = marketing_strategy(startup_idea)
        mentor = mentor_advice(startup_idea)

        final_report = generate_report(
            idea,
            market,
            business,
            finance,
            marketing,
            mentor
        )

        return {
            "report": final_report
        }

    except Exception as e:
        return {
            "error": str(e)
        }


@app.post("/download-report")
async def download_report(data: dict = Body(...)):
    try:
        report = data.get("report")

        if not report:
            return {"error": "Report content is missing"}

        pdf_file = generate_pdf(report)

        return FileResponse(
            path=pdf_file,
            filename="startup_report.pdf",
            media_type="application/pdf"
        )
    except Exception as e:
            return {
                "error": str(e)
            }
    
@app.post("/signup")
def signup(data: dict = Body(...)):
    try:
        username = data.get("username")
        password = data.get("password")

        db = SessionLocal()

        existing_user = db.query(User).filter(
            User.username == username
        ).first()

        if existing_user:
            db.close()
            return {"message": "Username already exists"}

        user = User(
            username=username,
            password=password
        )

        db.add(user)
        db.commit()
        db.close()

        return {"message": "Signup Successful"}

    except Exception as e:
        return {"error": str(e)}


@app.post("/login")
def login(data: dict = Body(...)):
    try:
        username = data.get("username")
        password = data.get("password")

        db = SessionLocal()

        user = db.query(User).filter(
            User.username == username,
            User.password == password
        ).first()

        db.close()

        if user:
            return {"message": "Login Successful"}

        return {"message": "Invalid Username or Password"}

    except Exception as e:
        return {"error": str(e)}