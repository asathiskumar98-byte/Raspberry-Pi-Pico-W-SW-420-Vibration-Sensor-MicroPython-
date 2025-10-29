# 🌍 Raspberry Pi Pico W – SW-420 Vibration Sensor (MicroPython)

This project reads analog vibration levels from an **SW-420 sensor** using the **ADC** on Raspberry Pi Pico W.

---

## ⚙️ Hardware Setup
| SW-420 Pin | Pico W Pin | Description |
|-------------|-------------|-------------|
| VCC | 3.3V | Power |
| GND | GND | Ground |
| AO | GPIO26 (ADC0) | Analog signal |
| DO | (optional) GPIO16 | Digital signal (threshold output) |

---

## 🧠 Working Principle
The **SW-420** sensor detects vibrations or knocks using a spring-based mechanism.  
The onboard comparator circuit can also generate digital threshold signals.

The analog output (AO) gives continuous vibration intensity, read via **ADC0**.

---

## 🚀 Run the Code
1. Open **Thonny IDE**  
2. Connect Pico W  
3. Save code as `main.py`  
4. Tap or shake the sensor — view analog readings in the shell  

---

## 💡 Try These Next
- Blink LED when vibration > 30,000  
- Send vibration alerts over Wi-Fi  
- Plot vibration levels on SSD1306 OLED
