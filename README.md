# Space-Invaders-Remake
A remake of the 1978 arcade classic originally released by Taito, built in Python with networking. 

Classics always return in time — just look at how often Resident Evil gets remastered. I believe creativity is less about strict originality and more about sincerity. Videogames, like other art forms, keep circling back to the same timeless themes — survival, challenge, and connection.

This project is my way of keeping that cycle alive.

<img width="1114" height="864" alt="image" src="https://github.com/user-attachments/assets/2351f3b4-6a17-4205-8a2e-ca0c3b775cbf" />

## 🌐 Features

* **Local Network Multiplayer** – Supports several players connected to one host
* **2-Player Split Mode** – Two players in one window, each starting with **10 lives**
* **Dead Reckoning** – Smooths gameplay and handles network surprises
  
<img width="1105" height="860" alt="image" src="https://github.com/user-attachments/assets/6b909813-b2d4-456a-9784-5dcbbfde3d8c" />

---

## 🎮 How to Play

1. Change the `local_ip` variable in your code to match your LAN IP
2. Run the **host**:

   ```bash
   python3 p2p.py
   ```
3. Add several clients in configuration (up to 4 supported)
4. Run each **client** in a new terminal:

   ```bash
   python3 client.py
   ```
5. Survive, shoot, and win!

---

## ⚙️ Requirements

* Python **3.9+**
* **Pygame** (for graphics)

Install pygame:

```bash
pip install pygame
```
