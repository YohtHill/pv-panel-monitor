# Photovoltaic Panel Monitor | 光伏板参数监测仪

[English](#english) · [简体中文](#简体中文)

## English

An STM32F042K6T6 coursework prototype that samples an analog measurement circuit and displays photovoltaic panel readings on an ST7735 SPI TFT.

1. Install STM32CubeIDE. Open **File → Import → Existing Projects into Workspace** and select [firmware/](firmware/).
2. Build the Debug configuration of lab5_4. It uses STM32Cube FW_F0 V1.11.5 and includes the required HAL and CMSIS source files.
3. Open firmware/lab5_4.ioc for clock and pin assignments. Review the ADC front end and scale factors in firmware/Core/Src/main.c before applying a panel input.

The Debug build was verified with STM32CubeIDE 1.19.0. The build verifies the firmware toolchain. Check ADC scaling and panel readings on the actual hardware.

## 简体中文

基于 STM32F042K6T6 的课程原型，通过模拟前端采样光伏板信号，并在 ST7735 SPI 彩屏上显示读数。

1. 安装 STM32CubeIDE。在 **File → Import → Existing Projects into Workspace** 中选择 [firmware/](firmware/)。
2. 构建 lab5_4 的 Debug 配置。工程使用 STM32Cube FW_F0 V1.11.5，包含构建所需的 HAL 和 CMSIS 源文件。
3. 通过 firmware/lab5_4.ioc 核对时钟与引脚。接入光伏板信号前，先核对 ADC 前端及 firmware/Core/Src/main.c 中的量程换算。

已用 STM32CubeIDE 1.19.0 完成 Debug 构建。测量换算和光伏板读数需要在实际硬件上验证。

## Credits | 来源

- ST7735 driver / 屏幕驱动：Andriy Honcharenko, ST7735_SPI_STM32_HAL. [Upstream GPLv3 text / 上游 GPLv3 许可原文](firmware/LCD-DRIVER-LICENSE.txt).
- STM32 HAL and CMSIS / STM32 HAL 与 CMSIS：[Vendor notices / 原厂许可](firmware/Drivers/).
