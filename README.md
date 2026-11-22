# STM32 Photovoltaic Panel Monitor

[简体中文](README.zh-CN.md)

This breadboard instrument measures a loaded photovoltaic panel with an STM32F042K6T6. A resistor divider scales the panel voltage into PA0. The firmware calculates panel terminal voltage and estimates current through a fixed 10 kΩ load, then shows both values on an ST7735 SPI display.

**What worked.** The original coursework photo shows the prototype reporting approximately **1395 mV and 139 µA** on the display. The current value is calculated from the load resistance. The complete CubeIDE firmware also passed a Debug build in STM32CubeIDE 1.19.0.

<img src="docs/prototype-reading.jpg" alt="Prototype display showing the loaded photovoltaic panel reading" width="440">

## From the panel to the screen

~~~mermaid
flowchart LR
    P["PV panel under 10 kΩ load"] --> D["220 kΩ / 33 kΩ divider"]
    D --> A["PA0, 12-bit ADC"]
    A --> M["Voltage reconstruction and load-current estimate"]
    M --> T["ST7735 display"]
~~~

Open **File → Import → Existing Projects into Workspace** in STM32CubeIDE and select [firmware](firmware/). Build **lab5_4 → Debug**. The [measurement and wiring note](docs/measurement.md) explains the ADC conversion, pin map and bench comparison against a multimeter.

The firmware estimates current at this fixed test load. The panel I–V curve and maximum power point require measurements at multiple loads.
