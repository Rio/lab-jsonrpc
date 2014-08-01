from .base import JSONRPCBase
from .error import JSONRPCError


class JSONRPCResponse(JSONRPCBase):
    def __init__(self, id, result=None, error=None):
        JSONRPCBase.__init__(self)

        self["jsonrpc"] = "2.0"

        self["id"] = id

        if result and not error:
            self["result"] = result

        elif error and not result:
            if not isinstance(error, JSONRPCError):
                raise TypeError("Error object must be of type JSONRPCError.")

            self["error"] = error

        else:
            raise TypeError("Either result or error MUST be given.")
    # end __init__
# end JSONRPCResponse
