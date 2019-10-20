import first_site.data.db_session as db_session
from first_site.data.users import User


def get_user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()
