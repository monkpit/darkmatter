from enum import IntEnum, unique


@unique
class ReversibleEnum(IntEnum):
    @classmethod
    def get_name(cls, value):
        if isinstance(value, bytes):
            value = int.from_bytes(value, byteorder='little')
        elif isinstance(value, str):
            value = int(value)
        return '{clsname}.{value}'.format(clsname=cls.__name__,
                                          value=cls._value2member_map_[value].name)


class LOGIN_ACTIONS(ReversibleEnum):
    AUTHENTICATE = 0x10
    CREATE_USER = 0x20


class LOGIN_STATUS(ReversibleEnum):
    SUCCESS = 0x01
    ERROR = 0x02


class CREATE_ACCOUNT_STATUS(ReversibleEnum):
    SUCCESS = 0x03
    ERROR = 0x04
