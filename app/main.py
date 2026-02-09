from fastapi import FastAPI, HTTPException
from app.menu_client import fetch_live_menu
from app.recommender import choose_primary
from app.upsell import choose_upsells
from app.llm import explain
from app.models import RecommendationRequest, RecommendationResponse

app = FastAPI(title="Dispensary Kiosk Agent")


@app.post("/recommend", response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest):
    try:
        menu = await fetch_live_menu()
        primary = choose_primary(menu, request.intent, request.budget)
        upsells = choose_upsells(menu, primary)
        explanation = explain(primary, upsells)

        return RecommendationResponse(
            primary=primary,
            upsells=upsells,
            explanation=explanation
        )

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
