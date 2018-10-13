import base64

from apistar import annotate, http
from apistar.backends.sqlalchemy_backend import Session
from apistar.interfaces import Auth
from apistar.permissions import IsAuthenticated

from .models import Admin, Publisher, Culinary

auth = annotate(permissions=[IsAuthenticated()])


def get_token(session: Session, auth: Auth, authorization: http.Header):
    if authorization is None:
        return {'message': 'not authorization and please login'}

    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    username, password = decode.split(':')

    query_admin = session.query(Admin).filter_by(username=auth.get_user_id()).first()
    query_publisher = session.query(Publisher).filter_by(username=auth.get_user_id()).first()

    if query_admin:
        if query_admin.password == password:
            return {'username': auth.get_user_id(),
                    'user_id': query_admin.id,
                    'basic_token': ba[5:],
                    }
        else:
            return {'message': 'auth Password wrong !'}
    elif query_publisher:
        if query_publisher.password == password:
            return {'username': auth.get_user_id(),
                    'user_id': query_publisher.id,
                    'token': ba[5:],
                    }
        else:
            return {'message': 'auth Password wrong !'}

    else:
        return {'message': 'error authorization'}


@auth
def add_admin(session: Session, username: str, full_name: str, img_url: str, email: str, password: str,
              authorization: http.Header):
    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    usernamex, passwordx = decode.split(':')

    isAdmin = session.query(Admin).filter_by(username=usernamex).first() and session.query(Admin).filter_by(
        password=passwordx).first()

    if isAdmin:
        add_Admin = Admin(username, full_name, img_url, email, password)
        session.add(add_Admin)
        session.commit()
        return {'message': 'success add admin'}
    else:
        return {'message': 'not authorized'}


@auth
def add_publisher(session: Session, username: str, full_name: str, img_url: str, email: str, password: str,
                  authorization: http.Header):
    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    usernamex, passwordx = decode.split(':')

    isAdmin = session.query(Admin).filter_by(username=usernamex).first() and session.query(Admin).filter_by(
        password=passwordx).first()

    if isAdmin:
        addPublisher = Publisher(username, full_name, img_url, email, password)
        session.add(addPublisher)
        session.commit()
        return {'message': 'success add publisher'}
    else:
        return {'message': 'not authorized'}


@auth
def put_publisher(session: Session, username: str, full_name: str, img_url: str, email: str, password: str,
                  authorization: http.Header):
    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    usernamex, passwordx = decode.split(':')

    isAdmin = session.query(Admin).filter_by(username=usernamex).first() and session.query(Admin).filter_by(
        password=passwordx).first()
    queryset = session.query(Publisher).filter_by(email=email).first()

    if isAdmin:
        if email is not None:
            if queryset:
                if queryset and username is not None:
                    queryset.username = username
                if queryset and full_name is not None:
                    queryset.full_name = full_name
                if queryset and email is not None:
                    queryset.email = email
                if queryset and img_url is not None:
                    queryset.img_url = img_url
                if queryset and password is not None:
                    queryset.password = password
                return {'message': 'success edit publisher'}
            else:
                return {'message': 'email not found !'}
        else:
            return {'message': 'please input your email !'}
    else:
        return {'massage': 'not authorized'}


@auth
def delete_publisher(session: Session, email: str, authorization: http.Header):
    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    username, password = decode.split(':')

    isAdmin = session.query(Admin).filter_by(username=username).first() and session.query(Admin).filter_by(
        password=password).first()
    queryset = session.query(Publisher).filter_by(email=email).first()

    if isAdmin:
        if queryset:
            session.delete(queryset)
            return {"message": "success delete publisher"}
        else:
            return {"message": "error delete publisher"}
    else:
        return {'massage': 'not authorized'}


def get_publisher(session: Session):
    queryset = session.query(Publisher).all()

    publisher_data = [{'id': data.id,
                       'username': data.username,
                       'full_name': data.full_name,
                       'img_url': data.img_url,
                       'email': data.email,
                       'at_register': str(data.at_register)} for data in queryset]

    return {'publisher': publisher_data,
            'total': len(publisher_data)}


@auth
def add_culinary(session: Session, auth: Auth, culinary_name: str, description: str, location: str, img_url: str,
                 authorization: http.Header):
    ba = "".join(authorization.split())
    decode = base64.b64decode(ba[5:]).decode('utf-8')
    username, password = decode.split(':')

    isPublisher = session.query(Publisher).filter_by(username=username).first() and session.query(Publisher).filter_by(
        password=password).first()
    query = session.query(Publisher).filter_by(username=auth.get_user_id()).first()

    if isPublisher:
        if query:
            addCulinary = Culinary(publisher=auth.get_user_id(), culinary_name=culinary_name, description=description,
                                   location=location,
                                   img_url=img_url)
            session.add(addCulinary)
            session.commit()
            return {'message': 'success add culinary'}
        else:
            return {'message': 'error add culinary'}
    else:
        return {'message': 'not authorized'}


def get_culinary(session: Session, count: str):
    queryset = session.query(Culinary).all()

    if count is not None:
        countx = int(count) * 10
        data_page = []

        culinary_data = [{'id': data.id,
                          'publisher': data.publisher,
                          'culinary_name': data.culinary_name,
                          'description': data.description,
                          'img_url': data.img_url,
                          'at_created': str(data.at_created)} for data in queryset]

        if countx > len(culinary_data) and len(culinary_data) < countx:
            for s in range((countx - 10), len(culinary_data)):
                data_page.append(culinary_data[s])
        else:
            for s in range((countx - 10), countx):
                data_page.append(culinary_data[s])

        return {'culinarys': data_page,
                'total': len(data_page)}

    else:
        return {'message': 'input count !'}
