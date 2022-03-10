from fastapi import APIRouter, responses, status

router = APIRouter()

@router.get("/", include_in_schema=False)
async def index() -> None:
    return responses.RedirectResponse(
        '/docs', 
        status_code=status.HTTP_302_FOUND
    )