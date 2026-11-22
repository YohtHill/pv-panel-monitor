# STM32 光伏板参数监测仪

[English](README.md)

这套面包板仪器用 STM32F042K6T6 测量接入固定负载的光伏板。电阻分压后由 PA0 采样，固件反算光伏板端电压，并按 10 kΩ 负载估算电流，最后在 ST7735 彩屏显示两个读数。

**实际效果。** 课程报告的原始实物图显示，原型测得约 **1395 mV**，按负载阻值计算的电流为 **139 µA**。完整固件已在 STM32CubeIDE 1.19.0 通过 Debug 构建。

<img src="docs/prototype-reading.jpg" alt="光伏板负载测量原型的彩屏读数" width="440">

## 从光伏板到读数

~~~mermaid
flowchart LR
    P["光伏板接 10 kΩ 负载"] --> D["220 kΩ / 33 kΩ 电阻分压"]
    D --> A["PA0 的 12 位 ADC"]
    A --> M["反算端电压与负载电流"]
    M --> T["ST7735 彩屏"]
~~~

在 STM32CubeIDE 选择 **File → Import → Existing Projects into Workspace**，导入 [firmware](firmware/)，构建 **lab5_4 → Debug**。[测量与接线说明](docs/measurement.zh-CN.md)给出 ADC 换算及引脚。[台架记录与标定方案](docs/validation.zh-CN.md)列明历史读数、采样节奏和与万用表对照的步骤。

当前固件估算固定负载下的电流。若要画出光伏板 I–V 曲线或定位最大功率点，需要在多种负载下测量。
