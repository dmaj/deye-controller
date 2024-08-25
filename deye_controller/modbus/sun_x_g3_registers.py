#import deye_controller.modbus.sun_x_g3_registers
from deye_controller.modbus.sun_x_g3_registers import *
from deye_controller.modbus.protocol import *
from functools import partial

class PVPower (FloatType):
    def __init__(self, inv, registerCurrent, registerVoltage, address, name, scale, suffix):
        super().__init__(address, name, scale, suffix)
        resCurrent = inv.read_holding_registers(registerCurrent.address, registerCurrent.len)
        resVoltage = inv.read_holding_registers(registerVoltage.address, registerVoltage.len)
        self.value = resCurrent[0] * resVoltage[0]
        pass

class PVVoltage (FloatType):
    def __init__ (self, inv , address, name, scale, suffix):
        super().__init__(address, name, scale, suffix)
        resVoltage = inv.read_holding_registers(self.address, self.len)
        self.value = resVoltage[0]

class PVCurrent (FloatType):
    def __init__ (self, inv , address, name, scale, suffix):
        super().__init__(address, name, scale, suffix)
        resCurrent = inv.read_holding_registers(self.address, self.len)
        self.value = resCurrent[0]

class PVProductionToday (FloatType):
    def __init__ (self, inv , address, name, scale, suffix):
        super().__init__(address, name, scale, suffix)
        resCurrent = inv.read_holding_registers(self.address, self.len)
        self.value = resCurrent[0]

class _PV1Voltage (PVVoltage):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV2Voltage (PVVoltage):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV3Voltage (PVVoltage):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV4Voltage (PVVoltage):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)


class _PV1Current (PVCurrent):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV2Current (PVCurrent):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV3Current (PVCurrent):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV4Current (PVCurrent):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV1Power (PVPower):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, SunXG3Registers.PV1Current(inv), SunXG3Registers.PV1Voltage(inv), address, name, scale, suffix)

class _PV2Power (PVPower):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, SunXG3Registers.PV2Current(inv), SunXG3Registers.PV2Voltage(inv), address, name, scale, suffix)

class _PV3Power (PVPower):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, SunXG3Registers.PV3Current(inv), SunXG3Registers.PV3Voltage(inv), address, name, scale, suffix)

class _PV4Power (PVPower):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, SunXG3Registers.PV4Current(inv), SunXG3Registers.PV4Voltage(inv), address, name, scale, suffix)

class _PV1ProductionToday (PVProductionToday):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV2ProductionToday (PVProductionToday):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV3ProductionToday (PVProductionToday):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _PV4ProductionToday (PVProductionToday):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(inv, address, name, scale,  suffix)

class _ProductionToday (FloatType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resProductionToday = inv.read_holding_registers(self.address, self.len)
        self.value = resProductionToday[0]

class _ProductionTotal (LongUnsignedType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resProductionTtal = inv.read_holding_registers(self.address, self.len)
        self.value = resProductionTtal

class _Phase1Voltage (FloatType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resPhase1Voltage = inv.read_holding_registers(self.address, self.len)
        self.value = resPhase1Voltage[0]

class _Phase1Current (FloatType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resPhase1Current = inv.read_holding_registers(self.address, self.len)
        self.value = resPhase1Current[0]

class _ACFreq (FloatType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resACFreq = inv.read_holding_registers(self.address, self.len)
        self.value = resACFreq[0]

class _OperatingPower (FloatType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resOperatingPower = inv.read_holding_registers(self.address, self.len)
        self.value = resOperatingPower[0]

class _ACActivePower (LongUnsignedType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address, name, scale,  suffix)
        resACActivePower = inv.read_holding_registers(self.address, self.len)
        self.value = resACActivePower

class _ActivePowerRegulation (IntType):
    def __init__(self, inv, address, name, scale, suffix):
        super().__init__(address=address, name=name, suffix=suffix)
        resActivePowerRegulation = inv.read_holding_registers(self.address, self.len)
        self.value = resActivePowerRegulation[0]

class _DeviceTime(DeviceTime):

    def __init__(self, inv, address, length, name):
        super().__init__()
        self.address = address
        self.len = length
        self.descriptio = name
        self.suffix = ''
        self.value = [0, 0, 0]
        res = inv.read_holding_registers(self.address, self.len)
        self.value = res[0] if self.len == 1 else res

#=============== Writeable Registers =================
class _DeviceTimeWriteable(WritableRegister):
    """
    Adjustments of the system time of the inverter
    """
    def __init__(self, inv, dt, address, length):
        super(_DeviceTimeWriteable, self).__init__(22, length=length)
        self.set(dt)
        inv.write_multiple_holding_registers(address + 0, [self.modbus_value[0]])
        inv.write_multiple_holding_registers(address + 1, [self.modbus_value[1]])
        inv.write_multiple_holding_registers(address + 2, [self.modbus_value[2]])

    def set(self, x: datetime.datetime):
        """ Set the time of the inverter """
        as_ints = [int(u) for u in x.strftime('%y %m %d %H %M %S').split(' ')]
        self.modbus_value = to_inv_time(as_ints)
        self.value = x

class _ActivePowerRegulationWriteable(IntWritable):
    """
    Adjustments of the system time of the inverter
    """
    def __init__(self, inv, val, address, signed, low_limit, high_limit):
        super().__init__(address=address, signed=signed, low_limit=low_limit, high_limit=high_limit)
        self.set(val)
        inv.write_multiple_holding_registers(self.address, [self.modbus_value])


class SunXG3Registers:

    DeviceType = DeviceType()
    CommProtocol = IntType(1, 'modbus_address')
    SerialNumber = DeviceSerialNumber()
    RatedPower = IntType(8, 'rated_power')
    """ START OF WRITABLE Registers """

    """ Not defined here """
    CommAddress = IntType(74, 'comm_address')
    SwitchOnOff = BoolType(80, 'switch_on_off')
    ''' Switch On / Off the inverter '''
    ControlMode = InverterControlMode()

    DeviceTime = partial(_DeviceTime, address=22, length=3, name='inverter_time')

    ProductionToday = partial(_ProductionToday, address=60, name='day_energy', scale=10,  suffix='kWh')
    ProductionTotal = partial(_ProductionTotal, address=63, name='total_energy', scale=10, suffix='kWh')

    Phase1Voltage = partial(_Phase1Voltage, address=73, name='ac_l1_voltage', scale=10,  suffix='V')
    Phase1Current = partial(_Phase1Current, address=76, name='ac_l1_current', scale=10, suffix='A')
    ACFreq = partial(_ACFreq,address=79, name='ac_freq', scale=100, suffix='Hz')
    # ToDo: Uptime = ... 62, minutes

    PV1Voltage = partial(_PV1Voltage, address=109, name='dc_pv1_voltage',scale=10, suffix='V')
    PV1Current = partial(_PV1Current, address=110, name='dc_pv1_current', scale=10, suffix='A')
    PV1Power = partial(_PV1Power,address=0xffff, name='dc_pv1_power', scale=100,  suffix='W')
    PV1ProductionToday = partial(_PV1ProductionToday,address=65, name='dc_pv1_day_energy', scale=10, suffix='kWh')
    PV1Total = LongUnsignedType (69, 'dc_pv1_total_energy', 10, suffix='kWh')

    PV2Voltage= partial(_PV2Voltage, address=111, name='dc_pv2_voltage',scale=10, suffix='V')
    PV2Current = partial(_PV2Current,address=112, name='dc_pv2_current', scale=10, suffix='A')
    PV2Power = partial(_PV2Power,address=0xffff, name='dc_pv2_power', scale=100,  suffix='W')
    PV2ProductionToday = partial(_PV2ProductionToday, address=66, name= 'dc_pv2_day_energy', scale=10, suffix='kWh')
    PV2Total = LongUnsignedType (71, 'dc_pv2_total_energy', 10, suffix='kWh')

    PV3Voltage= partial(_PV3Voltage, address=113, name='dc_pv3_voltage',scale=10, suffix='V')
    PV3Current = partial(_PV3Current,address=114, name='dc_pv3_current', scale=10, suffix='A')
    PV3Power = partial(_PV3Power,address=0xffff, name='dc_pv3_power', scale=100,  suffix='W')
    PV3ProductionToday = partial(_PV3ProductionToday, address=67, name='dc_pv3_day_energy', scale=10, suffix='kWh')
    PV3Total = LongUnsignedType (74, 'dc_pv3_total_energy', 10, suffix='kWh')

    PV4Voltage= partial(_PV4Voltage, address=115, name='dc_pv4_voltage',scale=10, suffix='V')
    PV4Current = partial(_PV4Current, address=116, name='dc_pv4_current', scale=10, suffix='A')
    PV4Power = partial(_PV4Power,address=0xffff, name='dc_pv4_power', scale=100,  suffix='W')
    PV4ProductionToday = partial(_PV4ProductionToday, address=68, name='dc_pv4_day_energy', scale=10, suffix='kWh')
    PV4Total = LongUnsignedType (77, 'dc_pv4_total_energy', 10, suffix='kWh')


    OperatingPower = partial(_OperatingPower, address=80, name='operating_power', scale=10, suffix='W')
    ACActivePower = partial(_ACActivePower, address=86, name='ac_active_power', scale=10, suffix='W')

    ActivePowerRegulation = partial(_ActivePowerRegulation, address=40, name='active_power_regulation', scale=1, suffix='%')



    # SellTimeOfUse = TimeOfUseSell()
    # InverterGridExportCutoff = MicroinverterExportCutoff()
    # RunState = RunState()
    # GridFrequency = GridFrequency()



    @staticmethod
    def as_list() -> List[Register]:
        """ Method for easy iteration over the registers defined here  """
        return [getattr(SunXG3Registers, x) for x in SunXG3Registers.__dict__ if not x.startswith('_')
                and not x.startswith('as_')]

class SunXG3RegistersWrite:
    DeviceTime = partial(_DeviceTimeWriteable, address=22, length=3)

    ActivePowerRegulation = partial(_ActivePowerRegulationWriteable, address=40, signed=False, low_limit=0, high_limit=120)


class Sun600G3Registers (SunXG3Registers):
    pass

class Sun800G3Registers (SunXG3Registers):
    pass

class Sun1000G3Registers (SunXG3Registers):
    pass

class Sun1600G3Registers (SunXG3Registers):
    pass

class Sun2000G3Registers (SunXG3Registers):
    pass