# -*- coding: utf-8 -*-
'''
Created on Mar 12, 2012

@author: moloch

    Copyright [2012] [Redacted Labs]

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
'''

from sqlalchemy.types import Unicode, Integer
from sqlalchemy import Column, ForeignKey
from models import dbsession
from models.BaseObject import BaseObject


class Permission(BaseObject):
    ''' Permission definition '''

    permission_name = Column(Unicode(64), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    @classmethod
    def by_user_id(cls, user_id):
        ''' Return all permissions whose user id is user_id '''
        return dbsession.query(cls).filter_by(user_id=user_id).all()

    def __repr__(self):
        return ('<Permission - name: %s, user_id: %d>' % (self.permission_name, self.user_id)).encode('utf-8')

    def __unicode__(self):
        return self.permission_name
