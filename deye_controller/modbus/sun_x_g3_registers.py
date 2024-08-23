from deye_controller.modbus.protocol import *



class SunXG3Registers:

    DeviceType = DeviceType()
    CommProtocol = IntType(1, 'modbus_address')
    SerialNumber = DeviceSerialNumber()
    RatedPower = IntType(8, 'rated_power')
    """ START OF WRITABLE Registers """
    DeviceTime = DeviceTime()  # RW 62
    """ Not defined here """
    CommAddress = IntType(74, 'comm_address')
    SwitchOnOff = BoolType(80, 'switch_on_off')
    ''' Switch On / Off the inverter '''
    ControlMode = InverterControlMode()

    ProductionToday = FloatType(60, 'day_energy',10,  suffix='kWh')
    ProductionTotal = LongUnsignedType (63, 'total_energy', 10, suffix='kWh')

    Phase1Voltage= FloatType(73, 'ac_l1_voltage',10,  suffix='V')
    Phase1Current = FloatType(76, 'ac_l1_current', 10, suffix='A')
    # ToDo: Phase1Power = to be calculated
    ACFreq = FloatType(79, 'ac_freq', 100, suffix='Hz')
    # ToDo: Uptime = ... 62, minutes

    PV1Voltage= FloatType(109, 'dc_pv1_voltage',10,  suffix='V')
    PV1Current = FloatType(110, 'dc_pv1_current', 10, suffix='A')
    # ToDo: PV1Power = to be calculated
    PV1ProductionToday = FloatType(65, 'dc_pv1_day_energy', 10, suffix='kWh')
    PV1Total = LongUnsignedType (69, 'dc_pv1_total_energy', 10, suffix='kWh')

    PV2Voltage= FloatType(111, 'dc_pv2_voltage',10,  suffix='V')
    PV2Current = FloatType(112, 'dc_pv2_current', 10, suffix='A')
    #ToDo: PV2Power = to be calculated
    PV2ProductionToday = FloatType(66, 'dc_pv2_day_energy', 10, suffix='kWh')
    PV2Total = LongUnsignedType (71, 'dc_pv2_total_energy', 10, suffix='kWh')

    PV3Voltage= FloatType(113, 'dc_pv3_voltage',10,  suffix='V')
    PV3Current = FloatType(114, 'dc_pv3_current', 10, suffix='A')
    # ToDo: PV3Power = to be calculated
    PV3ProductionToday = FloatType(67, 'dc_pv3_day_energy', 10, suffix='kWh')
    PV3Total = LongUnsignedType (74, 'dc_pv3_total_energy', 10, suffix='kWh')

    PV4Voltage= FloatType(115, 'dc_pv4_voltage',10,  suffix='V')
    PV4Current = FloatType(116, 'dc_pv4_current', 10, suffix='A')
    # ToDo: PV4Power = to be calculated
    PV4ProductionToday = FloatType(68, 'dc_pv4_day_energy', 10, suffix='kWh')
    PV4Total = LongUnsignedType (77, 'dc_pv4_total_energy', 10, suffix='kWh')

    # ToDo: DC Tootal Power

    OperatingPower = FloatType(80, 'operating_power', 10, suffix='W')
    ACActivePower = LongUnsignedType (86, 'ac_active_power', 10, suffix='kWh')



    # SellTimeOfUse = TimeOfUseSell()
    # InverterGridExportCutoff = MicroinverterExportCutoff()
    # RunState = RunState()
    # GridFrequency = GridFrequency()



    @staticmethod
    def as_list() -> List[Register]:
        """ Method for easy iteration over the registers defined here  """
        return [getattr(HoldingRegisters, x) for x in HoldingRegisters.__dict__ if not x.startswith('_')
                and not x.startswith('as_')]

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