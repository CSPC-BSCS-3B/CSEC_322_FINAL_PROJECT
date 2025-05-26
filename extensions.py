from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize SQLAlchemy
db = SQLAlchemy()

# Initialize Login Manager
login_manager = LoginManager()
login_manager.login_view = 'login'

# Initialize Bcrypt
bcrypt = Bcrypt()

# Initialize rate limiter
storage_uri = os.environ.get('REDIS_URL', 'memory://')

# Enhanced limiter configuration with better storage and security settings
limiter = Limiter(
    key_func=get_remote_address,  # Base rate limits on client IP address
    default_limits=["200 per day", "50 per hour"],
    storage_uri=storage_uri,
    strategy="moving-window",  # More accurate than fixed-window for security-critical applications
    headers_enabled=True,      # Send rate limit headers to clients
    header_name_mapping={      # Standardized header names for rate limiting
        "X-RateLimit-Limit": "X-RateLimit-Limit",
        "X-RateLimit-Remaining": "X-RateLimit-Remaining",
        "X-RateLimit-Reset": "X-RateLimit-Reset",
    },
    swallow_errors=False,      # Don't hide rate limiting errors
)