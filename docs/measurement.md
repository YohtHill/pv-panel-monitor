# Measurement and Display

[简体中文](measurement.zh-CN.md) · [Project home](../README.md)

| Connection | Pin or value |
| --- | --- |
| Divider | 220 kΩ high side, 33 kΩ low side |
| Load across panel | 10 kΩ |
| Divider midpoint | PA0 / ADC_IN0 |
| Display SPI clock and data | PA5 / PA7 |
| Display CS, DC, reset and backlight | PA4, PA3, PA6 and PA1 |

See the [CubeMX project](../firmware/lab5_4.ioc) and [firmware](../firmware/Core/Src/main.c). After HAL ADC calibration, the loop uses nominal Vref of 3300 mV and integer calculations.

~~~text
Vadc_mV = ADC_raw × 3300 / 4096
Vpv_mV  = Vadc_mV × 253 / 33
I_uA    = Vpv_mV / 10
~~~

The firmware refreshes the screen with a 300 ms delay per iteration. Connect the divider and load with a shared reference ground. Before attaching PA0, measure the divider midpoint with a multimeter. Compare multimeter readings across the panel and the load with the display under the same illumination and load. Use measured resistor values and supply voltage if calibrating. One archived reading demonstrates the display chain. Calibrated accuracy is not established.

[ST7735 GPLv3 text](../firmware/LCD-DRIVER-LICENSE.txt) and [vendor HAL/CMSIS notices](../firmware/Drivers/) are included.
