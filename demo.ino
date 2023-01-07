#include <ESP32Servo.h>
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SH1106.h>

//######################
// FIREBASE
#include<WiFi.h>;
#include<Firebase_ESP_Client.h>;
#include "addons/TokenHelper.H";
#include "addons/RTDBHelper.H";

#define WIFI_SSID "Sathappan_lap"
#define WIFI_PASSWORD "12345678"
#define API_KEY "AIzaSyB5bJqmsRRqf5OQpTGBtNFFhcrjGBXTEb4"
#define DATABASE_URL "https://smartparking-d872f-default-rtdb.firebaseio.com/"

FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config; 

unsigned long sendDataPrevMillis = 0;
bool singupOK = false; 
// #######################################################################################

#define OLED_SDA 22
#define OLED_SCL 21

Adafruit_SH1106 display(22, 21);
Servo myservo; 
int pos = 0,IR_in = 4,IR_out = 23,Car_slot_1 = 26,Car_slot_2 = 27;    // variable to store the servo position

void setup() {
  Serial.begin(9600);

//##################################################################################
  WiFi.begin(WIFI_SSID,WIFI_PASSWORD);
  Serial.print("Connecting to WiFi :");
  while(WiFi.status()!= WL_CONNECTED){
    Serial.print(" Not connetcted with a WIFI");
    delay(300);
  }  
  Serial.println();Serial.print("Connetcted with WIFI");
  Serial.println(WiFi.localIP());
  Serial.println();
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;
  if(Firebase.signUp(&config, &auth, "", "")){
    Serial.print("Singup OK");
    singupOK = true;    
  }
  else{
    Serial.printf("%s\n",config.signer.signupError.message.c_str());
  }
  config.token_status_callback = tokenStatusCallback;
  Firebase.begin(&config,&auth);
  Firebase.reconnectWiFi(true);      
//##################################################################################
  
  pinMode(IR_in,INPUT);
  pinMode(IR_out,INPUT);
  pinMode(Car_slot_2,INPUT);
  pinMode(Car_slot_1,INPUT);
  myservo.attach(5); 
  myservo.write(90);
  
  display.begin(SH1106_SWITCHCAPVCC, 0x3C); 
  display.println("IOT");
  display.println("Parking Slot");
  display.clearDisplay();
  }


void loop() {
  // to check avaiable slot
  if ((digitalRead(Car_slot_1)==0) and (digitalRead(Car_slot_2)==0)){
      display.println("Slots Filled");  
  }
  else if (((digitalRead(Car_slot_1)==0) or (digitalRead(Car_slot_2)==0))){
    display.println("Avaiable slots : 1");  
  }    
  else{
    display.println("Avaiable slots : 2");  
  }
  display.display();
  // delay(2000);
  display.clearDisplay();  

// to open servo  
  if ((digitalRead(IR_in)==0) or (digitalRead(IR_out)==0))
  {
    if ((digitalRead(Car_slot_1)==0) and (digitalRead(Car_slot_2)==0)) // 0 1 open 1 0 open 11 close
    {
      Serial.println("car parking full");
    }
    else
    {
      Serial.println("car parking free");
      myservo.write(0);
      delay(1000);
      Serial.println("Object Detected in");
    }
  }
  else
  {
    Serial.println("Object not Detected");    
    myservo.write(90);
  }  

// pirticular slot
  if (digitalRead(Car_slot_1)==0){
      display.println("Slot 1 : Full");  
  }
  else{
    display.println("Slot 1 : Free");
  }  
  if (digitalRead(Car_slot_2)==0){
      display.println("Slot 2 : Full");  
  }
  else{
    display.println("Slot 2 : Free");
  }  
//###############################################################################
  if(Firebase.ready() && singupOK){
    int park = digitalRead(Car_slot_1);
    if(Firebase.RTDB.setInt(&fbdo,"Parking/Slot_One",park)){
      Serial.println();
      Serial.print(park);
      Serial.print("Successfully save to: " + fbdo.dataPath());
      Serial.print("(" + fbdo.dataType() + ")");                  
    }
    else{
      Serial.println("Failed: "+fbdo.errorReason());
    }
  }

  if(Firebase.ready() && singupOK){
    int park2 = digitalRead(Car_slot_2);
    if(Firebase.RTDB.setInt(&fbdo,"Parking/Slot_Two",park2)){
      Serial.println();
      Serial.print(park2);
      Serial.print("Successfully save to: " + fbdo.dataPath());
      Serial.print("(" + fbdo.dataType() + ")");                  
    }
    else{
      Serial.println("Failed: "+fbdo.errorReason());
    }
  }
//###############################################################################
  display.setTextSize(2);
  display.setTextColor(WHITE);
  display.setCursor(0,0);
  display.setTextSize(1.95);
  display.println("Total Slots : 2");
} 
  