import flask
from flask import jsonify, make_response, request
from . import db_session
from .users import User

blueprint = flask.Blueprint(
    'user_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/user')
def get_user():
    db_sess = db_session.create_session()
    users = db_sess.query(User).all()
    return jsonify(
        {
            'users':
                [item.to_dict(only=('name', 'email'))
                 for item in users]
        }
    )

@blueprint.route('/api/user/<int:news_id>', methods=['GET'])
def get_one_user(news_id):
    db_sess = db_session.create_session()
    users = db_sess.query(User).get(news_id)
    if not users:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify(
        {
            'user': users.to_dict(only=(
                'name', 'email'))
        }
    )
