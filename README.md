# Automation Workshop

This repository serves as an educational resource for learning different approaches to automation, using Minecraft as a practical example. The Minecraft world simulates the SAUVC competition pool setup, providing a safe and accessible environment for testing automation algorithms. The Answer to this workshop can be found [here](https://github.com/Leung-Kam-Ho/Automation-Workshop) with limited access. The workshop covers three progressive levels of automation complexity:

## Setup

### Prerequisites
- Python 3.12+
- Minecraft Java Edition
- UV package manager (recommended)
- ROS 2

### Installation
```bash
# Clone the repository
git clone https://github.com/Leung-Kam-Ho/Automastion-Workshop-Exercises.git
cd automation-workshop-exercises

# Install dependencies
uv sync
```

### Minecraft Server Setup
The project communicates with a local Minecraft server running on port 25565. The server simulates ROS-like control by translating commands into keyboard inputs for Minecraft. The CurseForge modpack will be ready later this year to facilitate the setup. ***Right now, the server and the modpack will only be available to participants of the workshop.***


![Minecraft Virtual Environment](Media/Minecraft_Screenshoot.png)

## Getting Started

1. **Start the Minecraft Command Server:**

2. **Run Script-Based Automation:**
   ```bash
   uv run python Script_Based_Auto.py
   ```

3. **Explore Behaviour Trees:**
   Implement your own behaviour tree logic using the `py-trees` library.

4. **Add Computer Vision:**
   Integrate YOLO for object detection and combine with behaviour trees for advanced automation.

## Workshop Levels

### 1. Script-Based Automation

Learn the fundamentals of automation through direct scripting. This approach involves writing sequential commands to control game actions.

**Key Files:**
- `Script_Based_Auto.py` - Demonstrates basic script-based automation with movement sequences
- `Minecraft_Tool/minecraft_override_config.py` - Client library for sending commands to Minecraft

**Challenges:**
- **Implement additional movement patterns**
- **The arena environment is fixed**
- **Use Behaviour Tree based logic to walk through the Gate, perform a 180 degrees U-turn, then pass through the gate one more time**

### 2. Behaviour Tree Based Automation (SAUVC Qualification Round)
Advance to more sophisticated automation using behaviour trees. This approach provides better structure and modularity for complex decision-making processes.

***Behaviour Tree for this level:***

<img width="576" height="155" alt="behavior_tree_based" src="https://github.com/user-attachments/assets/db6adc3d-1165-46dc-8b4d-691dbd428b95" />

***Minecraft Environment for this level:***

https://github.com/user-attachments/assets/95f5334a-2764-4df0-9867-4677f162c2c7

***SAUVC 2025 Qualification Round Footage:***

https://github.com/user-attachments/assets/66ffdf3e-b37d-47a9-95f1-b71e3dbc51e9



**Key Files:**
- `BehaviourTree_Based_Auto.py` - Demonstrates behaviour tree-based automation
   
**Challenges:**
- **Implement additional action nodes and composite nodes**
- **The arena environment is fixed**
- **Use Behaviour Tree based logic to walk through the Gate, perform a 180 degrees U-turn, then pass through the gate one more time**

**Dependencies:**
- `py-trees` - For behaviour tree logic


### 3. YOLO + Behaviour Tree Automation
Combine computer vision with behaviour trees for intelligent automation. Use YOLO (You Only Look Once) object detection to perceive the game environment and make decisions accordingly.

***Behaviour Tree for this level:***

<img width="2738" height="688" alt="behavior_tree_based" src="https://github.com/user-attachments/assets/8d9343b5-18b3-4983-ac16-4a01091c0a8c" />

***Minecraft Environment for this level:***

https://github.com/user-attachments/assets/31a0e1be-5e8b-4d7f-99fe-687d278e4884


***SAUVC 2025 Competition Rounds Footage:***

https://github.com/user-attachments/assets/701894db-2eab-4a89-bbbf-bb3235ea5838

**Key Files:**
- `YOLO_BehaviourTree_Based_Auto.py` - Demonstrates YOLO + behaviour tree automation

**Challenges:**
- **Integrate YOLO object detection into the behaviour tree**
- **Implement additional action nodes and composite nodes**
- **The arena environment may vary, requiring dynamic decision-making**
- **Use YOLO + Behaviour Tree based logic to walk through the Gate, go to the blue pail (bucket), and hit all 3 colored poles in the target area**

**Dependencies:**
- `ultralytics` - YOLO implementation for object detection
- `py-trees` - For behaviour tree logic

## Project Structure
```
├── Minecraft_Tool/
│   ├── minecraft_command_server.py    # Flask server for Minecraft control
│   └── minecraft_override_config.py    # Client library for server communication
├── Script_Based_Auto.py                # Level 1: Script-based automation example
├── BehaviourTree_Based_Auto.py         # Level 2: Behaviour tree-based automation example
├── YOLO_BehaviourTree_Based_Auto.py    # Level 3: YOLO + behaviour tree-based automation example
├── custom_action.py                     # Custom action definitions for behaviour trees
├── main.py                            # Project entry point
├── pyproject.toml                     # Project configuration
└── README.md                          # This file
```


## Learning Objectives

By completing this workshop, you'll learn:
- Basic scripting for automation tasks
- Behaviour tree design patterns
- Computer vision integration with YOLO
- ROS-like message passing concepts
- Modular automation architecture

## Contributing

This is an educational repository. Feel free to enhance the examples or add new automation levels while maintaining the progressive learning structure.
