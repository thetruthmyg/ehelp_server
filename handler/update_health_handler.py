__author__ = 'hanks'

from tornado.web import RequestHandler
from tornado.escape import json_encode


from utils import utils
from utils import KEY
from utils import STATUS
from database import db

class Update_Health_Handler(RequestHandler):
  def post(self):
    params = utils.decode_params(self.request)

    resp = {}
    if KEY.HEALTH_ID in params:
      if db.update_health_record(params):
        resp = db.get_health_record(params[KEY.HEALTH_ID])
        if resp is None:
          resp = {}
        resp[KEY.STATUS] = STATUS.OK
      else:
        resp[KEY.STATUS] = STATUS.ERROR
    else:
      resp[KEY.STATUS] = STATUS.ERROR

    self.write(json_encode(resp))