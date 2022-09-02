from rest_framework.response import Response as res


class Response:

    @staticmethod
    def error_response(message):
        return res({"success": False,
                    "message": message})
