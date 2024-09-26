from fastapi import FastAPI


def create_app():
    return FastAPI(
        title='Integration with an external API',
        docs_url='/api/docs',
        description='Simple integration with an external API',
        debug=True,
    )