import enum


class InverterState(int, enum.Enum):

    StandBy     = 0
    SelfCheck   = 1
    Normal      = 2
    Alarm       = 3
    Fault       = 4

    @classmethod
    def _missing_(cls, value):
        return InverterState.Fault

    def __format__(self, format_spec):
        return self.name


class ControlMode(int, enum.Enum):

    LeadBattery = 0
    LithiumBattery = 1

    @classmethod
    def _missing_(cls, value):
        return ControlMode.LeadBattery

    def __format__(self, format_spec):
        return self.name


class BatteryControlMode(int, enum.Enum):

    ByVoltage = 0
    ByCapacity = 1
    NoBattery = 2
    Error = 99

    @classmethod
    def _missing_(cls, value: int):
        return BatteryControlMode.Error

    def __format__(self, format_spec):
        return self.name


class BMSMode(int, enum.Enum):

    PYLONTech_CAN   = 0
    SACRED_SUN_FOXX = 1
    KOK             = 2
    Keith           = 3
    TopPay          = 4
    PYLONTech_485   = 5
    VISIONGroup_CAN = 13
    WattSonic       = 14

    def __format__(self, format_spec):
        return self.name

    @classmethod
    def _missing_(cls, value):
        print(f'Unknown CAN/MODBUS protocol: {value}')
        return BMSMode.PYLONTech_CAN


class TimeOfUse(int, enum.Enum):
    """ Time of Use settings on the inverter screen """
    ENABLED = 1
    MONDAY = 2
    TUESDAY = 4
    WEDNESDAY = 8
    THURSDAY = 16
    FRIDAY = 32
    SATURDAY = 64
    SUNDAY = 128

    @staticmethod
    def from_int(val: int):
        """ List representation of the settings which are enabled """
        r = []
        for u in [TimeOfUse.ENABLED, TimeOfUse.MONDAY, TimeOfUse.TUESDAY, TimeOfUse.WEDNESDAY,
                  TimeOfUse.THURSDAY, TimeOfUse.FRIDAY, TimeOfUse.SATURDAY, TimeOfUse.SUNDAY]:
            if val & u == 0:
                continue
            r.append(u)
        return r

    def __format__(self, format_spec):
        return self.name


class ChargeGridGen(int, enum.Enum):
    """ Grid / Generator charge states """
    GridGenDisabled     = 0  # Only from PV
    GridEnabled         = 1
    GenEnabled          = 2
    GridGenEnabled      = 3

    @classmethod
    def _missing_(cls, value: object):
        return ChargeGridGen.GridGenDisabled

    def __format__(self, format_spec):
        return self.name


class TwoBitState(int, enum.Enum):
    """
    States as described for register 178
    00 / 01 (binary) - means not defined / not used
    10 (binary) - disabled
    11 (binary) - enabled   
    """
    Undefined_1 = 0
    Undefined_2 = 1
    Disabled = 2
    Enabled = 3

    @classmethod
    def _missing_(cls, value: object):
        return TwoBitState.Undefined_1

    def __format__(self, format_spec):
        return self.name
