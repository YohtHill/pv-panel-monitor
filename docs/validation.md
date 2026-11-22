# Bench Evidence and Calibration Plan

[简体中文](validation.zh-CN.md) · [Project home](../README.md) · [Wiring and ADC conversion](measurement.md)

## Existing evidence

The [original bench photograph](prototype-reading.jpg) shows the LCD reporting **1395 mV** and **139 µA** with the 10 kΩ load. This is one prototype display reading. The current is calculated from the displayed voltage, with integer truncation in the firmware. Independent voltage and current readings for this trial are unavailable in the project record. STM32CubeIDE 1.19.0 produced the firmware's Debug build.

| Quantity | Current evidence |
| --- | --- |
| Panel voltage under load | One LCD reading of 1395 mV. |
| Load current | Estimated 139 µA from 10 kΩ, rounded down by integer division. |
| ADC and display timing | One ADC conversion per loop. Each loop includes a 300 ms delay after drawing the screen, so the sample-to-sample period also includes conversion and display time. |
| Measurement error and repeatability | No calibrated reference or repeated observations are available. |

## Reproduce and record

1. Measure the actual 220 kΩ, 33 kΩ and 10 kΩ resistances with the board disconnected from power. Measure the ADC reference supply while operating.
2. In the same test condition, measure the panel terminals and divider midpoint with a multimeter. Confirm the midpoint is within the ADC input range before connecting PA0. Record the LCD voltage and current and, when using the debugger, the raw ADC code.
3. Repeat across several in-range reference voltages and take repeated readings at each. For a panel trial, record lighting and the connected load. Use independently measured load resistance to calculate a separate reference current.
4. Log timestamps if measuring sampling cadence. Report the mean signed error, maximum absolute error and variation. Separate conversion uncertainty from reference-voltage drift, divider tolerance and display rounding.

| Condition | Panel reference (mV) | ADC midpoint (mV) | LCD panel reading (mV) | Signed error (mV) |
| --- | ---: | ---: | ---: | ---: |
| Archived 10 kΩ load example | — | — | 1395 | — |
| Reference-voltage trial | | | | |

Signed voltage error = LCD panel reading − multimeter panel reading. When comparing different load values, use the measured load resistance rather than the firmware's fixed 10 kΩ. An I–V curve or maximum-power-point estimate needs a separate load sweep.
