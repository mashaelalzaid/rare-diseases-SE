# -*- coding: utf-8 -*-

from scripts import tabledef
from flask import session
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import bcrypt
import sys, subprocess, ipaddress, time, datetime, json,  os, csv, copy
from watson_developer_cloud import DiscoveryV1


EnvID="5aec3469-82f9-49cb-9718-e3d0526a85f7"
ColID="ccc5a579-296d-445f-a4cf-9fd81c536e8d"
ConfID="e813ec51-af96-422f-943c-65d776818292"


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    s = get_session()
    s.expire_on_commit = False
    try:
        yield s
        s.commit()
    except:
        s.rollback()
        raise
    finally:
        s.close()

def get_session():
    return sessionmaker(bind=tabledef.engine)()
    

def get_natural_language_query(query):
    #with session_scope() as s:
        print("query is"+query)
        discovery = DiscoveryV1(version='2018-03-05', username="9e523dc4-1206-4898-a30f-faf75cd8526b", password="tQFEkjWAz6hr")
        my_query = discovery.query(environment_id=EnvID, collection_id=ColID, query=query, passages='true', passages_count='1', count=1, highlight='true')
        p_passage=my_query['passages'][0]["passage_text"]
        p_score=my_query['passages'][0]["passage_score"]
        p_id=my_query['passages'][0]["document_id"]
        querylist = [p_passage,p_score,p_id]

        return querylist



