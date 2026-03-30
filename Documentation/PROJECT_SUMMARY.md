# Project Summary: Photovoltaic Panel Parameter Monitor

## Project Description
This embedded systems project involves developing a microcontroller-based monitoring system for photovoltaic (PV) panels. The system uses an STM32F042K6 microcontroller to measure and display key PV parameters including voltage and current on an ST7735 LCD display.

## Key Components
- **Microcontroller**: STM32F042K6 (ARM Cortex-M0)
- **Display**: ST7735 LCD (128x160 pixels, SPI interface)
- **Sensors**: ADC for voltage measurement, resistive divider for high voltage scaling
- **Software**: STM32 HAL libraries, custom display drivers

## Measurement Capabilities
1. **Voltage Measurement**: 0-3300mV range using voltage divider (220kΩ + 33kΩ)
2. **Current Calculation**: Using load resistance method (10kΩ load)
3. **Display**: Real-time showing of Vpv (mV) and I (µA)

## Team Members
1. Xinze Jia (U2294252)
2. Yuxin Chen (U2389495)
3. Shuaicheng Han (U2389497)
4. Jiahui Li (U2389498)
5. Penglin Xue (U2389499)
6. Jiakun Pi (U2389501)
7. Chenkun Gao (U2389502)
8. Yuan Yin (U2389503)
9. Jielong Su (U2389504)

## Project Files (Original Location)
The complete project includes:
- **Code**: STM32CubeIDE project with full source
- **Poster**: Presentation materials (PPTX, PDF, JPG)
- **Reflective Logs**: Individual learning reflections (DOCX, PDF)
- **Experimental Data**: Measurement results (XLSX)
- **Video**: Demonstration video (MP4)

## Technical Achievements
- Successful implementation of real-time PV parameter monitoring
- Accurate voltage measurement using ADC and voltage divider
- Stable display interface with ST7735 LCD
- Robust system operation under varying conditions

## Learning Outcomes
- Embedded system design and implementation
- STM32 microcontroller programming
- ADC interfacing and calibration
- LCD display driver development
- Team collaboration and project management

## Note on Large Files
Due to GitHub file size limitations, large binary files (PPTX, MP4, PDF) are not included in this repository. These files are available in the original project folder and can be shared via alternative means if needed.