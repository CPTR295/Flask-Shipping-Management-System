from werkzeug.exceptions import HTTPException
from flask import make_response,render_template,Response




class DuplicateRecordException(HTTPException):
    code = 500 
    description = 'Record Already Exists'

    def get_response(self,environ=None):
        resp=Response()
        resp.response = render_template('/error/generic.html',ex_message=self.description)
        return resp