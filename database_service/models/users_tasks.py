import sqlalchemy
from db_session import SqlAlchemyBase
from sqlalchemy import orm

class UserTask(SqlAlchemyBase):
    __tablename__ = 'users_tasks'

    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"))
    user = orm.relationship('User')
    task_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("tasks.id"))
    task = orm.relationship('Task')