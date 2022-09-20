# -*- coding: utf-8 -*-
import os
from lms.envs.devstack import *

####### Settings common to LMS and CMS
import json
import os

from xmodule.modulestore.modulestore_settings import update_module_store_settings

# Mongodb connection parameters: simply modify `mongodb_parameters` to affect all connections to MongoDb.
mongodb_parameters = {
    "host": "mongodb",
    "port": 27017,
    
    "user": None,
    "password": None,
    
    "db": "openedx",
}
DOC_STORE_CONFIG = mongodb_parameters
CONTENTSTORE = {
    "ENGINE": "xmodule.contentstore.mongo.MongoContentStore",
    "ADDITIONAL_OPTIONS": {},
    "DOC_STORE_CONFIG": DOC_STORE_CONFIG
}
# Load module store settings from config files
update_module_store_settings(MODULESTORE, doc_store_settings=DOC_STORE_CONFIG)
DATA_DIR = "/openedx/data/"
for store in MODULESTORE["default"]["OPTIONS"]["stores"]:
   store["OPTIONS"]["fs_root"] = DATA_DIR

# Behave like memcache when it comes to connection errors
DJANGO_REDIS_IGNORE_EXCEPTIONS = True

DEFAULT_FROM_EMAIL = ENV_TOKENS.get("DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
DEFAULT_FEEDBACK_EMAIL = ENV_TOKENS.get("DEFAULT_FEEDBACK_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
SERVER_EMAIL = ENV_TOKENS.get("SERVER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
TECH_SUPPORT_EMAIL = ENV_TOKENS.get("TECH_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
CONTACT_EMAIL = ENV_TOKENS.get("CONTACT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BUGS_EMAIL = ENV_TOKENS.get("BUGS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
UNIVERSITY_EMAIL = ENV_TOKENS.get("UNIVERSITY_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PRESS_EMAIL = ENV_TOKENS.get("PRESS_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
PAYMENT_SUPPORT_EMAIL = ENV_TOKENS.get("PAYMENT_SUPPORT_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
BULK_EMAIL_DEFAULT_FROM_EMAIL = ENV_TOKENS.get("BULK_EMAIL_DEFAULT_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_MANAGER_EMAIL = ENV_TOKENS.get("API_ACCESS_MANAGER_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])
API_ACCESS_FROM_EMAIL = ENV_TOKENS.get("API_ACCESS_FROM_EMAIL", ENV_TOKENS["CONTACT_EMAIL"])

# Get rid completely of coursewarehistoryextended, as we do not use the CSMH database
INSTALLED_APPS.remove("lms.djangoapps.coursewarehistoryextended")
DATABASE_ROUTERS.remove(
    "openedx.core.lib.django_courseware_routers.StudentModuleHistoryExtendedRouter"
)

# Set uploaded media file path
MEDIA_ROOT = "/openedx/media/"

# Add your MFE and third-party app domains here
CORS_ORIGIN_WHITELIST = []

# Video settings
VIDEO_IMAGE_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT
VIDEO_TRANSCRIPTS_SETTINGS["STORAGE_KWARGS"]["location"] = MEDIA_ROOT

GRADES_DOWNLOAD = {
    "STORAGE_TYPE": "",
    "STORAGE_KWARGS": {
        "base_url": "/media/grades/",
        "location": "/openedx/media/grades",
    },
}

ORA2_FILEUPLOAD_BACKEND = "filesystem"
ORA2_FILEUPLOAD_ROOT = "/openedx/data/ora2"
ORA2_FILEUPLOAD_CACHE_NAME = "ora2-storage"

# Change syslog-based loggers which don't work inside docker containers
LOGGING["handlers"]["local"] = {
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "all.log"),
    "formatter": "standard",
}
LOGGING["handlers"]["tracking"] = {
    "level": "DEBUG",
    "class": "logging.handlers.WatchedFileHandler",
    "filename": os.path.join(LOG_DIR, "tracking.log"),
    "formatter": "standard",
}
LOGGING["loggers"]["tracking"]["handlers"] = ["console", "local", "tracking"]

# Email
EMAIL_USE_SSL = False
# Forward all emails from edX's Automated Communication Engine (ACE) to django.
ACE_ENABLED_CHANNELS = ["django_email"]
ACE_CHANNEL_DEFAULT_EMAIL = "django_email"
ACE_CHANNEL_TRANSACTIONAL_EMAIL = "django_email"
EMAIL_FILE_PATH = "/tmp/openedx/emails"

LOCALE_PATHS.append("/openedx/locale/contrib/locale")
LOCALE_PATHS.append("/openedx/locale/user/locale")

# Allow the platform to include itself in an iframe
X_FRAME_OPTIONS = "SAMEORIGIN"


JWT_AUTH["JWT_ISSUER"] = "http://local.overhang.io/oauth2"
JWT_AUTH["JWT_AUDIENCE"] = "openedx"
JWT_AUTH["JWT_SECRET_KEY"] = "DKaiZnAwNvLq3CjjYxwTOhCa"
JWT_AUTH["JWT_PRIVATE_SIGNING_JWK"] = json.dumps(
    {
        "kid": "openedx",
        "kty": "RSA",
        "e": "AQAB",
        "d": "F-R25vGidBburs_urnnq6GKNSYzV88oET0IVx3jp89OwKb3D9Yysm9QTfcFhB6isMsVt6UNJebRShGPjUidfCgGxRjJBBnUM__WP3GAOsES4ZSj0qC3zEraUsZ5ItmliZW2fiZJ3MxoIBqU1eB5rCO9_7UYhqkA6H2WbQgYGahrwA6Q_2e066DAVL6RJ9wUyq2AgagONRaAk3stQRe6wiW4znTCdC62ntC8Gi2LdQS_-NojSY98BQYN5shKkB2saDPQaaAJZlbEksKUdBzpj_yN2ST4ePJsyF6zXSNpilyYLJenX9sAfxtqFBnqeT44IarY6Kjw3XWp_eT2rkAeGbQ",
        "n": "xXhVeGPeaksFl9Z3PWiIkr94BVz6vd07lwYFszewN3QDmPIPP5rTUX335CJgRgw7MRveDx2Ujo_Vqm1GEyrEXdenR1FASQeurPdbq3n9M6b7Ep-Tj4pUxKqB85oe6zIdkQntJvOMBSQEeiPOpcb9ku2LgpveHRW5MBx-_sxoSH84LnI4NIr3F6t28jggPVHGm3s_i98zmCEOyF6TSRgyipAa41A8veYzmPLwG0IAkTIn99nRxjLwR-1m_pATRJDjJ-X6x__mDWlMlY-E262POZNh35UaHK5vIClhZaqIr3zTgdbY5vcTsURmr_AWHgqEBwC6SmsFxzHbQw-pqfZoRw",
        "p": "192yjtl3OpcYeKD5vkC7vrkGm-Lt67g8FYrR-G3ADQRBVzHd5HufQILccVgeVUx6l2yPjb5AENlcDIATydIjzBYAO6HYcbZm8bNeifhBs1UtqTwm6HxypJlyihRYSq7kmZvvv9lBjuDaUfhV7_FeWhkSLPGVTp6LNfMrybo57is",
        "q": "6i8RQsg-mXGkl7GdHkKKlG7NjsBNK1yUdMdyUrmsO4nulmKmIz0CH28raH0iIYZgMJf6Dqy3UeViKbXsW_nzyDaVdap2wiDHroX-PUU62ARgYW5sINjMVq1s7VAzs-_BAhA6XRLvsdHG4vujGUVwlWmseEATkcC_aVoeo47Y_FU",
    }
)
JWT_AUTH["JWT_PUBLIC_SIGNING_JWK_SET"] = json.dumps(
    {
        "keys": [
            {
                "kid": "openedx",
                "kty": "RSA",
                "e": "AQAB",
                "n": "xXhVeGPeaksFl9Z3PWiIkr94BVz6vd07lwYFszewN3QDmPIPP5rTUX335CJgRgw7MRveDx2Ujo_Vqm1GEyrEXdenR1FASQeurPdbq3n9M6b7Ep-Tj4pUxKqB85oe6zIdkQntJvOMBSQEeiPOpcb9ku2LgpveHRW5MBx-_sxoSH84LnI4NIr3F6t28jggPVHGm3s_i98zmCEOyF6TSRgyipAa41A8veYzmPLwG0IAkTIn99nRxjLwR-1m_pATRJDjJ-X6x__mDWlMlY-E262POZNh35UaHK5vIClhZaqIr3zTgdbY5vcTsURmr_AWHgqEBwC6SmsFxzHbQw-pqfZoRw",
            }
        ]
    }
)
JWT_AUTH["JWT_ISSUERS"] = [
    {
        "ISSUER": "http://local.overhang.io/oauth2",
        "AUDIENCE": "openedx",
        "SECRET_KEY": "DKaiZnAwNvLq3CjjYxwTOhCa"
    }
]


######## End of settings common to LMS and CMS

######## Common LMS settings
LOGIN_REDIRECT_WHITELIST = ["studio.local.overhang.io"]

# Better layout of honor code/tos links during registration
REGISTRATION_EXTRA_FIELDS["terms_of_service"] = "required"
REGISTRATION_EXTRA_FIELDS["honor_code"] = "hidden"

# This url must not be None and should not be used anywhere
LEARNING_MICROFRONTEND_URL = "http://learn.openedx.org"

# Fix media files paths
PROFILE_IMAGE_BACKEND["options"]["location"] = os.path.join(
    MEDIA_ROOT, "profile-images/"
)

COURSE_CATALOG_VISIBILITY_PERMISSION = "see_in_catalog"
COURSE_ABOUT_VISIBILITY_PERMISSION = "see_about_page"

# Allow insecure oauth2 for local interaction with local containers
OAUTH_ENFORCE_SECURE = False

# Create folders if necessary
for folder in [DATA_DIR, LOG_DIR, MEDIA_ROOT, STATIC_ROOT_BASE, ORA2_FILEUPLOAD_ROOT]:
    if not os.path.exists(folder):
        os.makedirs(folder)



######## End of common LMS settings

# Setup correct webpack configuration file for development
WEBPACK_CONFIG_PATH = "webpack.dev.config.js"

SESSION_COOKIE_DOMAIN = ".local.overhang.io"

LMS_BASE = "local.overhang.io:8000"
LMS_ROOT_URL = "http://{}".format(LMS_BASE)
LMS_INTERNAL_ROOT_URL = LMS_ROOT_URL
SITE_NAME = LMS_BASE
CMS_BASE = "studio.local.overhang.io:8001"
CMS_ROOT_URL = "http://{}".format(CMS_BASE)
LOGIN_REDIRECT_WHITELIST.append(CMS_BASE)

FEATURES['ENABLE_COURSEWARE_MICROFRONTEND'] = False
COMMENTS_SERVICE_URL = "http://forum:4567"

LOGGING["loggers"]["oauth2_provider"] = {
    "handlers": ["console"],
    "level": "DEBUG"
}


