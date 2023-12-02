// Pines de señales PWM
const int ena = 10;
const int enb = 5;

// Pines de control de dirección
const int in1 = 9;
const int in2 = 8;
const int in3 = 7;
const int in4 = 6;

// Pines del sensor ultrasónico HC-SR04
const int triggerPin = 11;
const int echoPin = 12;

// Distancia de activación en centímetros
const int distanciaActivacion = 5;  // Cambiado a 5 cm

void setup() {
  Serial.begin(9600);
  pinMode(ena, OUTPUT);
  pinMode(enb, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(in3, OUTPUT);
  pinMode(in4, OUTPUT);
  pinMode(triggerPin, OUTPUT);
  pinMode(echoPin, INPUT);
  detenerMotores();
  delay(1000);
}

void detenerMotores() {
  digitalWrite(ena, LOW);
  digitalWrite(enb, LOW);
  digitalWrite(in1, LOW);
  digitalWrite(in2, LOW);
  digitalWrite(in3, LOW);
  digitalWrite(in4, LOW);
}

int medirDistancia() {
  digitalWrite(triggerPin, LOW);
  delayMicroseconds(2);
  digitalWrite(triggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  return pulseIn(echoPin, HIGH) * 0.034 / 2;
}

void controlarVelocidad() {
  if (Serial.available() > 0) {
    int velocidad = Serial.parseInt();
    analogWrite(ena, velocidad);
    analogWrite(enb, velocidad);
  }
}

void loop() {
  int distancia = medirDistancia();

  if (distancia < distanciaActivacion) {
    Serial.println(F("Objeto cercano. Activando motores."));

    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    digitalWrite(in3, HIGH);
    digitalWrite(in4, LOW);

    controlarVelocidad();  // Añadido: Controlar velocidad desde Python
  } else {
    Serial.println(F("No se detecta un objeto cercano. Deteniendo motores."));
    detenerMotores();
  }
}
