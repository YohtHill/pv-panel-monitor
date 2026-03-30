# Photovoltaic Panel Parameter Monitor

## Project Overview
This project involves the development of a microcontroller-based parameter monitoring system for photovoltaic (PV) panels. The system uses an STM32F042K6 microcontroller to measure and display key parameters of a PV panel, including voltage and current, on an ST7735 LCD display.

## Team Members
- Xinze Jia (U2294252)
- Yuxin Chen (U2389495) 
- Shuaicheng Han (U2389497)
- Jiahui Li (U2389498)
- Penglin Xue (U2389499)
- Jiakun Pi (U2389501)
- Chenkun Gao (U2389502)
- Yuan Yin (U2389503)
- Jielong Su (U2389504)

## Project Structure
```
Group8_Project/
├── Code/                    # STM32 microcontroller source code
│   ├── Core/               # Core application files
│   │   ├── Inc/            # Header files
│   │   └── Src/            # Source files
│   ├── Drivers/            # HAL drivers and CMSIS
│   └── Debug/              # Compiled debug files
├── Poster/                  # Project presentation materials
├── Reflective Log/         # Individual reflective logs
├── Others/                 # Additional documentation and data
└── README.md              # This file
```

## Hardware Requirements
- STM32F042K6 microcontroller
- ST7735 LCD display (128x160 resolution)
- Photovoltaic panel for testing
- Voltage divider circuit (220kΩ + 33kΩ resistors)
- Load resistor (10kΩ for current measurement)
- Power supply and wiring components

## Software Requirements
- STM32CubeIDE or compatible development environment
- STM32 HAL libraries
- ST7735 display driver

## Key Features
1. **Real-time Monitoring**: Continuously measures PV panel voltage and current
2. **LCD Display**: Shows voltage (mV) and current (µA) on ST7735 display
3. **ADC Conversion**: 12-bit ADC for precise voltage measurement
4. **Voltage Divider**: Safely measures high PV voltages using resistor divider
5. **Current Calculation**: Calculates current using load resistance method

## Technical Specifications
- **Microcontroller**: STM32F042K6 (ARM Cortex-M0)
- **Display**: ST7735 (128x160 pixels, SPI interface)
- **ADC Resolution**: 12-bit (0-4095)
- **Voltage Measurement Range**: 0-3300mV (after divider)
- **Current Measurement**: Calculated via load resistance (I = V/R)
- **Communication**: SPI for display, UART for debugging (38400 baud)

## Code Architecture

### Main Components
1. **main.c**: Primary application logic
   - ADC initialization and reading
   - Voltage and current calculations
   - LCD display updates
   - Main control loop

2. **st7735.c/h**: LCD display driver
   - Display initialization
   - Text and graphics rendering
   - Screen management functions

3. **System Configuration**
   - Clock configuration (HSI48 at 48MHz)
   - GPIO initialization
   - SPI configuration for display
   - ADC configuration for voltage sensing

### Key Functions
- `HAL_ADC_Start()`: Initiates ADC conversion
- `ST7735_DrawString()`: Displays text on LCD
- `SystemClock_Config()`: Configures system clock
- `MX_ADC_Init()`: Initializes ADC peripheral

## Measurement Methodology

### Voltage Measurement
1. PV voltage is divided using 220kΩ (top) and 33kΩ (bottom) resistors
2. Divided voltage is measured by ADC on PA0 (Channel 0)
3. Raw ADC value converted to mV: `Vadc_mV = adc_raw × 3300 / 4096`
4. PV voltage calculated: `Vpv_mV = Vadc_mV × 253 / 33`

### Current Measurement
1. Current calculated using Ohm's Law: `I = V / R`
2. Using 10kΩ load resistor: `I_uA = Vpv_mV / 10`
3. Results displayed in microamperes (µA)

## Setup Instructions

### Hardware Setup
1. Connect PV panel to voltage divider circuit
2. Connect divider output to PA0 (ADC input)
3. Connect ST7735 display via SPI:
   - CS: PA4
   - DC: PA3  
   - RES: PA2
   - BL: PA1
4. Connect load resistor for current measurement
5. Provide appropriate power supply

### Software Setup
1. Import project into STM32CubeIDE
2. Configure project settings for STM32F042K6
3. Build project
4. Flash to microcontroller
5. Monitor output on display

### Calibration
1. Ensure PV+ is disconnected for zero current calibration
2. Verify voltage divider ratio matches calculations
3. Adjust load resistor value if needed for different current ranges

## Testing and Validation
- **Functional Testing**: Verify display shows correct readings
- **Accuracy Testing**: Compare with multimeter measurements
- **Stability Testing**: Monitor readings over extended periods
- **Environmental Testing**: Test under different lighting conditions

## Project Documentation

### Included Files
- **Poster**: Project overview and results presentation
- **Reflective Logs**: Individual learning reflections
- **Experimental Data**: Measurement results and analysis
- **Function Introduction**: Detailed system description
- **Peer Review**: Team evaluation and feedback

### Key Findings
1. Successful implementation of PV parameter monitoring
2. Accurate voltage measurement within expected range
3. Real-time display of key parameters
4. Robust system operation under varying conditions

## Future Enhancements
1. **Data Logging**: Add SD card for data storage
2. **Wireless Communication**: Implement Bluetooth or WiFi
3. **Maximum Power Point Tracking (MPPT)**: Add optimization algorithm
4. **Web Interface**: Remote monitoring capability
5. **Battery Integration**: Energy storage and management

## Troubleshooting

### Common Issues
1. **No Display Output**: Check SPI connections and initialization
2. **Incorrect Readings**: Verify voltage divider resistor values
3. **ADC Noise**: Add filtering capacitors to ADC input
4. **Current Calculation Errors**: Confirm load resistor value

### Debugging Tips
1. Use UART output for debugging values
2. Verify ADC raw values before conversion
3. Check display initialization sequence
4. Monitor power supply stability

## License
This project is developed for educational purposes as part of an embedded systems course.

## Acknowledgments
- Course instructors for guidance and support
- STMicroelectronics for development tools and libraries
- Team members for collaborative effort

## Contact
For questions or contributions, please refer to the team members listed above.