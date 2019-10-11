class TypeUtil(object):
    @staticmethod
    def is_empty(value):
        if value is None:
            return True
        elif isinstance(value, str):
            if value and value.strip():
                return False
            else:
                return True

        return False
