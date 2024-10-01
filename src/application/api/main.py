from fastapi import FastAPI

from src.application.api.users.handlers import router as user_router


def create_app():
    app =  FastAPI(
        title='Integration with an external API',
        docs_url='/api/docs',
        description='Simple integration with an external API',
        debug=True,
    )
    
    app.include_routers(user_router, prefix='user')
    
    return app