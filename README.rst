DEYE-controller
===================

* A library and simple tools for interaction with DEYE hybrid inverters
* The communication with the inverter requires a SOLARMAN datalogger
* `pysloarmanv5 <https://github.com/jmccrohan/pysolarmanv5>`_  based library
* Command line tools (exposed after install):
    - deye-read - read everything from the inverter (use --help for filters/options)
    - deye-regcheck - for quick check on specific register(s)
    - deye-scan is a scanner for dataloggers in the local network (not DEYE related)
    - deye-regwrite - for writing to individual registers

* Tested with:
    - SUN-12K-SG04LP3 / LSW-3

INSTALL
========

.. code-block:: console

  pip install deye-controller


TODO List
=============


Examples
==============
* Basic usage:

    * read a register from the inverter

    .. code-block:: python

        >>> from deye_controller import HoldingRegisters, WritableRegisters
        >>> from pysolarmanv5 import PySolarmanV5
        >>> inv = PySolarmanV5('192.168.1.100', 2712345678)
        >>> register = HoldingRegisters.BMSBatteryCapacity
        >>> res = inv.read_holding_registers(register.address, register.len)
        >>> register.value = res[0] if register.len == 1 else res
        >>> print(register.description, register.format(), register.suffix)
        bms_battery_SOC 24 %
        >>> inv.disconnect()
    ..

    * write

    .. code-block:: python

        >>> from deye_controller import HoldingRegisters, WritableRegisters
        >>> from pysolarmanv5 import PySolarmanV5
        >>> inv = PySolarmanV5('192.168.1.100', 2712345678)
        >>> register = WritableRegisters.SellModeSOC3
        >>> register.set(23)

        >>> inv.write_multiple_holding_registers(register.address, [register.modbus_value])
        1
        >>> inv.disconnect()



* SellMode programming:

  .. code-block:: python

    >>> from deye_controller import SellProgrammer
    >>> prog = SellProgrammer('192.168.1.108', 2799999999)
    >>> prog.show_as_screen()
    ____________________________________________________
    | Grid  |  Gen  |      Time     |   Pwr    |  SOC % |
    |       |       | 00:00 | 03:00 |     3500 |   100% |
    |       |       | 03:00 | 04:00 |     3500 |    30% |
    |       |       | 04:00 | 05:00 |     3500 |    30% |
    |       |       | 05:00 | 10:00 |     3500 |    30% |
    |       |       | 10:00 | 23:00 |     3500 |   100% |
    |       |       | 23:00 | 00:00 |     3500 |    30% |
    ----------------------------------------------------
    >>> prog.update_program(3, start_t='6:30', power=2500, soc=35, grid_ch=True)
    Program updated
     >>> prog.show_as_screen()  # For visual confirmation of the settings
    ____________________________________________________
    | Grid  |  Gen  |      Time     |   Pwr    |  SOC % |
    |       |       | 00:00 | 03:00 |     3500 |   100% |
    |       |       | 03:00 | 04:00 |     3500 |    30% |
    |       |       | 04:00 | 06:30 |     3500 |    30% |
    |   ✓   |       | 06:30 | 10:00 |     2500 |    35% |
    |       |       | 10:00 | 23:00 |     3500 |   100% |
    |       |       | 23:00 | 00:00 |     3500 |    30% |
    ----------------------------------------------------
    >>> prog.upload_settings()  # In order to upload the settings to the inverter
    >>> prog.disconnect()  # Needed if PySolarmanV5 >= 3.0.0


Notes
=========
* It is possible the inverter to be completely deactivated by writing 0 to register 80
  WritableRegisters.SwitchOnOff.set(False) but it will raise an alarm and will show error F19.
  The normal state is restored as soon as the register is set to its default value 1.
* The WritableRegisters.GridExportLimit register can be used if the grid export is not desired
  when the battery is charged and the PV generation exceeds the load.

Deye SUN*G3
=========
* Tested with my SUN2000G3
* As usual: use at your own risk, at least it worked for me.
* I have not changed the original project, but only inserted the file sun_x_g3_registers.py (https://github.com/dmaj/deye-controller/blob/master/deye_controller/modbus/sun_x_g3_registers.py)
* The placeholder ‘xxxxxxxxx’ is the serial number of the inverter, which can be found under ‘Device information’ in the web interface, for example.
* The API can also be used for the smaller inverters. They then only have 2 strings and not 4 strings
* The power of the individual strings is not read from the registers, as these are not available in these inverters. Therefore, the actual current and voltage are read out and the product is returned.
* I cannot guarantee that all registers are correctly addressed. I have collected the information to the best of my knowledge and belief :-). But I think most of the values are correct.
Example: all previously implemented registers that can be read out

    .. code-block:: python

        def print_reg(register):
            print(register.description, register.format(), register.suffix)
        
        if __name__ == '__main__':
            from pysolarmanv5 import PySolarmanV5
            from deye_controller.modbus.sun_x_g3_registers import SunXG3Registers, SunXG3RegistersWrite
        
            inv = PySolarmanV5('192.168.0.100', xxxxxxxxx)
        
            print_reg(SunXG3Registers.Phase1Voltage(inv))
            print_reg(SunXG3Registers.Phase1Current(inv))
            print_reg(SunXG3Registers.ACFreq(inv))
            print()
            print_reg(SunXG3Registers.OperatingPower(inv))
            print_reg(SunXG3Registers.ACActivePower(inv))
            print ()
            print_reg(SunXG3Registers.ProductionToday(inv))
            print_reg(SunXG3Registers.ProductionTotal(inv))
            print()
            print_reg(SunXG3Registers.PV1Voltage(inv))
            print_reg(SunXG3Registers.PV2Voltage(inv))
            print_reg(SunXG3Registers.PV3Voltage(inv))
            print_reg(SunXG3Registers.PV4Voltage(inv))
            print()
            print_reg(SunXG3Registers.PV1Current(inv))
            print_reg(SunXG3Registers.PV2Current(inv))
            print_reg(SunXG3Registers.PV3Current(inv))
            print_reg(SunXG3Registers.PV4Current(inv))
            print()
            print_reg(SunXG3Registers.PV1ProductionToday(inv))
            print_reg(SunXG3Registers.PV2ProductionToday(inv))
            print_reg(SunXG3Registers.PV3ProductionToday(inv))
            print_reg(SunXG3Registers.PV4ProductionToday(inv))
            print()
            print_reg(SunXG3Registers.PV1Power(inv))
            print_reg(SunXG3Registers.PV2Power(inv))
            print_reg(SunXG3Registers.PV3Power(inv))
            print_reg(SunXG3Registers.PV4Power(inv))
        
            print_reg(SunXG3Registers.ActivePowerRegulation(inv))
    
            inv.disconnect()

Example: Writing the ActivePowerRegulation register. It is also read out before and after for checking purposes.

    .. code-block:: python

        def print_reg(register):
            print(register.description, register.format(), register.suffix)
        
        if __name__ == '__main__':
            from pysolarmanv5 import PySolarmanV5
            from deye_controller.modbus.sun_x_g3_registers import SunXG3Registers, SunXG3RegistersWrite
        
            inv = PySolarmanV5('192.168.0.100', xxxxxxxx)

            print_reg(SunXG3Registers.ActivePowerRegulation(inv))
            register = SunXG3RegistersWrite.ActivePowerRegulation
            register.set(100)
            inv.write_multiple_holding_registers(register.address, [register.modbus_value])
            print_reg(SunXG3Registers.ActivePowerRegulation(inv))

            inv.disconnect()

