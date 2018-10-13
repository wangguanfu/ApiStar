from apistar import annotate
from apistar.permissions import IsAuthenticated
from core.auth import BasicAuthentication

from app.models import Base

settings = {
    "DATABASE": {
        "URL": "mysql+pymysql://root:password@localhost/KulinerApi", # update database
        "METADATA": Base.metadata
    },
    'AUTHENTICATION': [BasicAuthentication()]
}
