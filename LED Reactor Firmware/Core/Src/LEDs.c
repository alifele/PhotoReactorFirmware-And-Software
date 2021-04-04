#include "LEDs.h"

	LEDsConf_TypeDef LEDsConf;

void LEDs_ConfigLEDs(LEDsConf_TypeDef * InitLEDs){
	LEDsConf = *InitLEDs;
	HAL_GPIO_WritePin(InitLEDs->RedLED_Port, InitLEDs->RedLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(InitLEDs->GreenLED_Port, InitLEDs->GreenLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(InitLEDs->BlueLED_Port, InitLEDs->BlueLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(InitLEDs->OrangeLED_Port, InitLEDs->OrangeLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(InitLEDs->WhiteLED_Port, InitLEDs->WhiteLED_Pin, GPIO_PIN_RESET);
}

void LEDs_TurnOffAll(void){
	HAL_GPIO_WritePin(LEDsConf.RedLED_Port, LEDsConf.RedLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(LEDsConf.GreenLED_Port, LEDsConf.GreenLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(LEDsConf.BlueLED_Port, LEDsConf.BlueLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(LEDsConf.OrangeLED_Port, LEDsConf.OrangeLED_Pin, GPIO_PIN_RESET);
	HAL_GPIO_WritePin(LEDsConf.WhiteLED_Port, LEDsConf.WhiteLED_Pin, GPIO_PIN_RESET);
}


void LEDs_TurnOnLED(int color){
	//  1-> R, 2-> G, 3-> B, 4-> O, 5-> W

	if (color == 1){
			HAL_GPIO_WritePin(LEDsConf.RedLED_Port, LEDsConf.RedLED_Pin, GPIO_PIN_SET);
	}
	if (color == 2){
			HAL_GPIO_WritePin(LEDsConf.GreenLED_Port, LEDsConf.GreenLED_Pin, GPIO_PIN_SET);
	}
	if (color == 3){
			HAL_GPIO_WritePin(LEDsConf.BlueLED_Port, LEDsConf.BlueLED_Pin, GPIO_PIN_SET);
	}
	if (color == 4){
			HAL_GPIO_WritePin(LEDsConf.OrangeLED_Port, LEDsConf.OrangeLED_Pin, GPIO_PIN_SET);
	}
	if (color == 5){
			HAL_GPIO_WritePin(LEDsConf.WhiteLED_Port, LEDsConf.WhiteLED_Pin, GPIO_PIN_SET);
	}

}

void LEDs_TurnOffLED(int color){
	//  1-> R, 2-> G, 3-> B, 4-> O, 5-> W
//	HAL_GPIO_WritePin(LEDsConf->RedLED_Port, LEDsConf->RedLED_Pin, GPIO_PIN_RESET);
//	HAL_GPIO_WritePin(LEDsConf->GreenLED_Port, LEDsConf->GreenLED_Pin, GPIO_PIN_RESET);
//	HAL_GPIO_WritePin(LEDsConf->BlueLED_Port, LEDsConf->BlueLED_Pin, GPIO_PIN_RESET);
//	HAL_GPIO_WritePin(LEDsConf->OrangeLED_Port, LEDsConf->OrangeLED_Pin, GPIO_PIN_RESET);
//	HAL_GPIO_WritePin(LEDsConf->WhiteLED_Port, LEDsConf->WhiteLED_Pin, GPIO_PIN_RESET);

	if (color == 1){
			HAL_GPIO_WritePin(LEDsConf.RedLED_Port, LEDsConf.RedLED_Pin, GPIO_PIN_RESET);
	}
	if (color == 2){
			HAL_GPIO_WritePin(LEDsConf.GreenLED_Port, LEDsConf.GreenLED_Port, GPIO_PIN_RESET);
	}
	if (color == 3){
			HAL_GPIO_WritePin(LEDsConf.BlueLED_Port, LEDsConf.BlueLED_Pin, GPIO_PIN_RESET);
	}
	if (color == 4){
			HAL_GPIO_WritePin(LEDsConf.OrangeLED_Port, LEDsConf.OrangeLED_Pin, GPIO_PIN_RESET);
	}
	if (color == 5){
			HAL_GPIO_WritePin(LEDsConf.WhiteLED_Port, LEDsConf.WhiteLED_Pin, GPIO_PIN_RESET);
	}

}
