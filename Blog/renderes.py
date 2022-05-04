from rest_framework import renderers
import json


class commonResponse(renderers.JSONRenderer):
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = ''
        if 'ErrorDetail' in str(data):
            response = json.dumps({
                'message' : 'something went wrong',
                'status' : 404,
                'errors': data,
                })
        else:
            response = json.dumps({
                'message' : 'success',
                'status' : 200,
                'data': data
                })
        return response