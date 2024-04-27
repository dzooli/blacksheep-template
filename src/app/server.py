"""The application entry point.

This is the entry point of the backend server.
Initializes the application, creates the documentation binding and initializes the XSRF protection.
Contains an example of blacksheep.server.env usage and for logging with uvicorn.
"""

import logging

import uvicorn
from app import BaseApplication, docs
from blacksheep.server import env


def setup_logging():
    logging.getLogger().setLevel(logging.DEBUG)


def create_app() -> BaseApplication:
    """Creates the application instance.

    Returns:
        BaseApplication: The initialized application
    """
    setup_logging()
    logger = logging.getLogger("uvicorn.error")
    app = BaseApplication(show_error_details=False)
    # use_anti_forgery(app)

    if env.is_development():
        logger.info("Running in development.")

    from app.api.v1.home import Home

    docs.bind_app(app)
    return app


if __name__ == "__main__":
    if env.is_development():
        uvicorn.run(factory=True, app="app.server:create_app", port=8080, reload=True, timeout_graceful_shutdown=5)
    else:
        print("Run this directly only for development!")
