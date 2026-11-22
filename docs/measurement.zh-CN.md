# 测量与屏幕显示

[English](measurement.md) · [项目首页](../README.zh-CN.md)

| 连接 | 引脚或器件值 |
| --- | --- |
| 分压网络 | 上臂 220 kΩ，下臂 33 kΩ |
| 光伏板负载 | 10 kΩ |
| 分压中点 | PA0 / ADC_IN0 |
| 彩屏 SPI 时钟、数据 | PA5 / PA7 |
| 彩屏片选、数据命令、复位与背光 | PA4、PA3、PA6 和 PA1 |

引脚见 [CubeMX 工程](../firmware/lab5_4.ioc)，换算见[固件](../firmware/Core/Src/main.c)。程序启动时执行 HAL ADC 校准，随后以标称 3300 mV 参考电压进行整数计算。

~~~text
Vadc_mV = ADC_raw × 3300 / 4096
Vpv_mV  = Vadc_mV × 253 / 33
I_uA    = Vpv_mV / 10
~~~

主循环每次刷新后延迟 300 毫秒。负载、分压器和单片机共地。接入 PA0 前用万用表测量分压中点，在相同光照和负载条件下比较光伏板两端、负载两端和屏幕读数。校准时可代入实测电阻及参考电压。已有一张实物读数用于确认显示链路，精度仍需标定。

[ST7735 GPLv3 原文](../firmware/LCD-DRIVER-LICENSE.txt)以及 [HAL/CMSIS 原厂许可](../firmware/Drivers/)随工程提供。
