from datetime import datetime

from app import db
from app.exceptions import InvalidListIDException
from app.models.list import List as ListModel
from .base import BaseInterface

class List(BaseInterface):

    def __init__(self, list):
        self._model = list

        self._id = list.id
        self._name = list.name
        self._created_at = list.created_at
        self._updated_at = list.updated_at

    def update(self, name=None):
        changes_made = False

        if name:
            changes_made = True
            self._model.name = name

        if changes_made:
            self._model.updated_at = datetime.now()
            self = cls(self)
            db.session.commit()

        return self

    @classmethod
    def for_id(id):
        list = ListModel.query.filter_by(id=id).first()

        if list:
            return cls(list)
        raise InvalidListIDException
