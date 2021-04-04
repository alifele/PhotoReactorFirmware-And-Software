#include "stm32f4xx_hal.h"
typedef struct{

	GPIO_TypeDef * RedLED_Port;
	GPIO_TypeDef * WhiteLED_Port;
	GPIO_TypeDef * GreenLED_Port;
	GPIO_TypeDef * BlueLED_Port;
	GPIO_TypeDef * OrangeLED_Port;


	uint16_t RedLED_Pin;
	uint16_t GreenLED_Pin;
	uint16_t BlueLED_Pin;
	uint16_t OrangeLED_Pin;
	uint16_t WhiteLED_Pin;


} LEDsConf_TypeDef;

void LEDs_TurnOffAll(void);
void LEDs_ConfigLEDs(LEDsConf_TypeDef * InitLEDs);
void LEDs_TurnOnLED(int color);
void LEDs_TurnOffLED(int color);
