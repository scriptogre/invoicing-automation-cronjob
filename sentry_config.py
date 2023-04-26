import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from config import SENTRY_DSN

sentry_sdk.init(
    dsn=SENTRY_DSN,
    integrations=[SentryAsgiMiddleware()],
)
