
#include<LedControl.h>
int DIN = 12;
int CS =  11;
int CLK = 10;
byte up[8]={0x18,0x3C,0x7E,0xFF,0x18,0x18,0x18,0x18};
byte down[8]={0x18,0x18,0x18,0x18,0x18,0xFF,0x7E,0x3C};


LedControl lc=LedControl(DIN,CLK,CS,0);
void setup(){
 lc.shutdown(0,false);       //The MAX72XX is in power-saving mode on startup
 lc.setIntensity(0,10);      // Set the brightness to maximum value
 lc.clearDisplay(0);         // and clear the display
}

void loop(){

  if(Serial.available()>0){
    getByte=Serial.parseInt();
  }
  switch(getByte){
    case 1:
    printbyte(up);
    break
    case 2:
    printbyte(down);
    
  }
  
}

printbyte(i,character[]){
  int i = 0;
    for(i=0;i<8;i++)
    {
       lc.setRow(0,i,character[i]);
    }

}
