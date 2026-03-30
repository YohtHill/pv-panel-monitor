# Build Instructions

## Prerequisites
1. **STM32CubeIDE** or compatible development environment
2. **STM32CubeMX** for project configuration (optional)
3. **STM32F0 HAL Libraries**

## Project Setup

### Option 1: Using STM32CubeIDE
1. Open STM32CubeIDE
2. Select "File" → "Import" → "Existing Projects into Workspace"
3. Browse to the project directory
4. Select the project and click "Finish"
5. Build the project using the hammer icon or Ctrl+B

### Option 2: Manual Project Creation
1. Create a new STM32 project for STM32F042K6
2. Copy the source files from `Code/Core/` to your project
3. Configure the following peripherals:
   - SPI1 for display communication
   - ADC1 for voltage measurement
   - USART2 for debugging (optional)
4. Set up the correct pin assignments
5. Build the project

## Hardware Configuration

### Pin Connections
| Pin | Function | Connection |
|-----|----------|------------|
| PA0 | ADC Input | Voltage divider output |
| PA1 | GPIO Output | ST7735 Backlight |
| PA2 | GPIO Output | ST7735 Reset |
| PA3 | GPIO Output | ST7735 DC |
| PA4 | GPIO Output | ST7735 Chip Select |
| PA5 | SPI1 SCK | ST7735 SCK |
| PA6 | SPI1 MISO | ST7735 MISO (if used) |
| PA7 | SPI1 MOSI | ST7735 MOSI |

### External Components
1. **Voltage Divider**: 220kΩ (top) + 33kΩ (bottom) resistors
2. **Load Resistor**: 10kΩ for current measurement
3. **ST7735 Display**: 128x160 LCD with SPI interface
4. **Power Supply**: Appropriate for STM32 and display

## Building and Flashing
1. Connect ST-Link programmer to SWD pins
2. Build the project (should produce `.elf` file)
3. Flash to microcontroller using ST-Link Utility or IDE
4. Reset the microcontroller

## Testing
1. Power on the system
2. Verify display shows initialization message
3. Connect PV panel to voltage divider
4. Observe voltage and current readings on display
5. Compare with multimeter for accuracy verification

## Troubleshooting
- **No display output**: Check SPI connections and initialization sequence
- **Incorrect readings**: Verify voltage divider resistor values
- **ADC noise**: Add 0.1µF capacitor to ADC input pin
- **Build errors**: Ensure all HAL libraries are included